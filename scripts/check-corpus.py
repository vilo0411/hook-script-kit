#!/usr/bin/env python3
"""Validate the frozen corpus and recompute baselines. No network or dependencies."""
import datetime
import json
from pathlib import Path
import re
import statistics
import sys


def validate(root):
    errors = []
    def require(condition, message):
        if not condition:
            errors.append(message)

    c = Path(root)
    try:
        data = {n: json.loads((c / (n + '.json')).read_text(encoding='utf-8'))
                for n in ['collection', 'channels', 'channel-videos', 'videos', 'analyses', 'patterns']}
    except (OSError, ValueError) as exc:
        return [str(exc)]
    collection, channels, records, videos, analyses, patterns = (
        data[n] for n in ['collection', 'channels', 'channel-videos', 'videos', 'analyses', 'patterns'])
    require(len(records) == collection['channelRecords'], 'Channel record count differs')
    require(len(channels) == collection['channels'], 'Channel count differs')
    require(len(videos) == collection['videosAnalyzed'] == collection['videosDownloaded'], 'Video count differs')
    require(len(patterns) == collection.get('hookGroups'), 'Hook group count differs')
    require(len(analyses) == collection.get('mindmaps'), 'Story diagram count differs')
    require(len({v['id'] for v in videos}) == len(videos), 'Duplicate selected video ID')
    require(len({v['id'] for v in records}) == len(records), 'Duplicate channel record ID')
    require(len({ch['handle'] for ch in channels}) == len(channels), 'Duplicate channel handle')
    require(all(v['handle'] in {ch['handle'] for ch in channels} for v in videos), 'Unknown selected channel')
    require(all(v.get('deliveryStyle') for v in videos), 'Missing observed delivery style')
    by = {v['id']: v for v in videos}
    by_channel = {v['handle']: v for v in channels}
    require({v['id'] for v in analyses} == set(by), 'Analysis/video IDs differ')
    require(len(analyses) == len(videos), 'Duplicate or missing analysis')
    study_ids = {a['id'] for a in analyses if a.get('hookStudy')}
    require(len(study_ids) == collection.get('hookStudies', 0), 'Hook study count differs')
    require(study_ids == set(collection.get('hookStudyVideoIds', [])), 'Hook study/video IDs differ')

    for ch in channels:
        rr = [v for v in records if v['handle'] == ch['handle']]
        asof = datetime.datetime.fromisoformat(ch['collectedAt']).timestamp()
        eligible = [v['views'] for v in rr if v['views'] is not None and v['timestamp']
                    and asof - v['timestamp'] >= 48 * 3600]
        require(len(rr) == ch['videoCountCollected'], 'Channel size differs: ' + ch['handle'])
        require(len(eligible) == ch['baselineCount'], 'Baseline size differs: ' + ch['handle'])
        require(bool(eligible) and statistics.median(eligible) == ch['baselineMedianViews'],
                'Baseline median differs: ' + ch['handle'])

    covered = set()
    for p in patterns:
        require(bool(p['videos']), 'Empty pattern: ' + p['id'])
        for vid in p['videos']:
            require(vid in by, 'Pattern references missing video: ' + vid)
            covered.add(vid)
    require(covered == set(by), 'Some analyses have no pattern reference')
    require(len({p['id'] for p in patterns}) == len(patterns), 'Duplicate pattern ID')

    for v in videos:
        vid, dur = v['id'], v['durationSeconds']
        median = by_channel[v['handle']]['baselineMedianViews']
        require(v['views'] >= 100000 and v['views'] >= 3 * median, 'Selection threshold fails: ' + vid)
        require(abs(v['timesBaselineMedian'] - v['views'] / median) < 1e-6,
                'Multiplier differs: ' + vid)
        require(v['baselineMedianViews'] == median, 'Video baseline differs: ' + vid)
        require(v['url'] == f"https://www.tiktok.com/@{v['handle']}/video/{vid}", 'Source URL differs: ' + vid)
        require((c / v['casePath']).is_file(), 'Missing case page: ' + vid)
        require(len((v['hookExcerpt'] or '').split()) <= 25, 'Hook excerpt too long: ' + vid)
        ev = v['evidence']
        for name in ['sourceMediaSha256', 'metadataSha256', 'contactSheetSha256', 'transcriptSha256']:
            require(bool(re.fullmatch('[0-9a-f]{64}', ev[name])), 'Invalid hash: ' + vid + '/' + name)
        require(ev['audioListened'] is False and ev['continuousVideoWatched'] is False,
                'Review scope changed without updating corpus validator: ' + vid)
        require(ev['durationDifferenceSeconds'] < 1, 'Media/ASR duration differs too much: ' + vid)
        require(all(0 <= t <= dur for t in ev['observedFrameTimes']), 'Frame outside duration: ' + vid)

    for a in analyses:
        if a['id'] not in by:
            continue
        dur = by[a['id']]['durationSeconds']
        require(bool(a['beats']) and bool(a['visualEvidence']), 'Missing analysis evidence: ' + a['id'])
        for b in a['beats']:
            require(0 <= b['start'] < b['end'] <= dur, 'Beat outside duration: ' + a['id'])
        for f in a['visualEvidence']:
            if by[a['id']]['evidence']['status'] == 'sampled-frames-plus-fresh-asr':
                require(f['time'] in by[a['id']]['evidence']['observedFrameTimes'], 'Observation not in extracted frames: ' + a['id'])
            require(0 <= f['time'] <= dur, 'Observation outside duration: ' + a['id'])
        require(bool(a['limitations']), 'Missing limitations: ' + a['id'])
        detail = a.get('detail', {})
        study = a.get('hookStudy')
        if study:
            for key in ['window', 'layers', 'attentionMethod', 'stopReason', 'unresolvedQuestion',
                        'withheldDetail', 'retentionBridge', 'payoff', 'twoSentenceBlueprint',
                        'crossNicheTransfer', 'doNotTransfer', 'evidenceScope']:
                require(bool(study.get(key)), 'Missing hook study field: ' + a['id'] + '/' + key)
            for key in ['window', 'payoff']:
                span = study.get(key, {})
                require(0 <= span.get('start', -1) < span.get('end', -1) <= dur,
                        'Hook study outside duration: ' + a['id'] + '/' + key)
            require(all(study.get('layers', {}).get(k) for k in ['speech', 'visual', 'screenText']),
                    'Missing hook observation layer: ' + a['id'])
            require(len(study.get('twoSentenceBlueprint', [])) == 2, 'Hook blueprint must have two parts: ' + a['id'])
            require(bool(by[a['id']].get('contentNiche')), 'Missing content niche: ' + a['id'])
        for key in ['promise', 'centralQuestion', 'emotionalArc', 'informationDesign',
                    'strengths', 'weaknesses', 'shareabilityHypotheses', 'adaptationRules', 'mindmapBranches']:
            require(bool(detail.get(key)), 'Missing detailed field: ' + a['id'] + '/' + key)
        for key in ['emotionalArc', 'informationDesign']:
            for item in detail.get(key, []):
                require(0 <= item['start'] < item['end'] <= dur, 'Detailed beat outside duration: ' + a['id'])
        branches = detail.get('mindmapBranches', [])
        require(len(branches) >= 5, 'Mindmap needs clip-specific branches: ' + a['id'])
        for branch in branches:
            require(bool(branch['label']) and bool(branch['children']), 'Empty mindmap branch: ' + a['id'])
        mmd = c / 'mindmaps' / (a['id'] + '.mmd')
        if mmd.is_file():
            diagram = mmd.read_text(encoding='utf-8')
            require('\nflowchart TD\n' in diagram and diagram.startswith('%%{init:'), 'Invalid story diagram type: ' + a['id'])
            case = (c / by[a['id']]['casePath']).read_text(encoding='utf-8')
            require('```mermaid\n' + diagram.rstrip() + '\n```' in case,
                    'Standalone/inline mindmaps differ: ' + a['id'])
        else:
            require(False, 'Missing standalone mindmap: ' + a['id'])
    return errors


if __name__ == '__main__':
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else (
        Path(__file__).resolve().parents[1] / 'skills/hook-script/references/corpus')
    errors = validate(root)
    for error in errors:
        print(error, file=sys.stderr)
    print(f'Corpus checks: {len(errors)} errors; no network calls.')
    sys.exit(bool(errors))
