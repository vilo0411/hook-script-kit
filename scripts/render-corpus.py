#!/usr/bin/env python3
"""Render the frozen analysis JSON into Markdown and Mermaid. No collection/network."""
from pathlib import Path
import json
import re
import textwrap

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / 'skills/hook-script/references/corpus'


def timestamp(seconds):
    minutes, secs = divmod(float(seconds), 60)
    return f'{int(minutes):02d}:{secs:05.2f}'


def cell(text):
    return str(text).replace('|', '/').replace('\n', ' ')


def label(text):
    # Labels are data, never Mermaid directives or syntax.
    value = re.sub(r'\s+', ' ', str(text)).strip()
    value = value.replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')
    return '<br/>'.join(textwrap.wrap(value, width=38, break_long_words=False))


def mindmap(analysis):
    center = label(analysis['title']).replace('(', ' ').replace(')', ' ')
    lines = ['mindmap', f'  root(({center}))']
    for i, branch in enumerate(analysis['detail']['mindmapBranches']):
        lines.append(f'    b{i}["{label(branch["label"])}"]')
        for j, child in enumerate(branch['children']):
            lines.append(f'      b{i}c{j}["{label(child)}"]')
    return '\n'.join(lines) + '\n'


def render_case(v, a):
    d, ev = a['detail'], v['evidence']
    out = [f'# {a["title"]}',
           f'[Video gốc — @{v["handle"]}]({v["url"]}) · ID `{v["id"]}`',
           '**Tóm tắt cách kể:** ' + a['mechanism'],
           '[Mindmap](#mindmap) · [Diễn biến](#dien-bien) · [Nhịp cảm xúc](#cam-xuc) · [Cách áp dụng](#ap-dung)',
           '## Dữ liệu và nguồn',
           f'- Đăng: {v["publishedAt"]}. Metadata lấy: {v["collectedAt"]}.\n'
           f'- **{v["views"]:,} view**; thích {v["likes"]:,}; bình luận {v["comments"]:,}; chia sẻ {v["shares"]:,}; lưu {v["saves"]:,}. Dấu phẩy tách hàng nghìn.\n'
           f'- Thời lượng media: {v["durationSeconds"]:.2f}s.\n'
           f'- **{v["timesBaselineMedian"]:.2f}× P50** {v["baselineMedianViews"]:,.0f} của {v["baselineCount"]} bài đủ 48h trong snapshot kênh. '
           f'Clip {"có" if v["inChannelSnapshot"] else "không có"} trong cửa sổ baseline. Không phải thống kê toàn bộ kênh.',
           '## Phạm vi kiểm',
           f'Đã tải lại media, xem khung chọn lọc và đọc ASR có mốc lưu lúc {ev["transcriptCacheAt"]}. '
           f'Đối chiếu cùng ID và thời lượng, lệch {ev["durationDifferenceSeconds"]}s. '
           '**Chưa nghe toàn âm hoặc xem chuyển động liên tục; chưa xác nhận toàn văn ASR hay mọi dữ kiện kinh tế trong clip.**',
           f'Media SHA256: `{ev["sourceMediaSha256"]}`. [Metadata và các hash khác](../videos.json). '
           'Video/ASR đầy đủ giữ ở bộ nghiên cứu cục bộ; bản chia sẻ giữ link gốc, trích ngắn và phân tích riêng.',
           '## Lời hứa và câu hỏi trung tâm',
           '**Lời hứa:** ' + d['promise'] + '\n\n**Câu hỏi:** ' + d['centralQuestion'],
           '## Mở đầu: lời và hình', a['openingObservation']]
    if v['hookExcerpt']:
        out += ['> ' + v['hookExcerpt'],
                f'Trích ASR ngắn từ segment {timestamp(v["openingSegment"]["start"])}–{timestamp(v["openingSegment"]["end"])}. '
                + v['hookExcerptStatus'] + ' Dấu … nghĩa là bỏ bớt, không khẳng định toàn câu vừa ba giây.']
    else:
        out += ['Không dùng câu ASR mở làm nguyên văn vì nhận dạng lỗi; xem diễn giải và đối chiếu nguồn.']
    table = '| Mốc khung đã xem | Điều quan sát được |\n|---|---|\n'
    table += '\n'.join(f'| {timestamp(e["time"])} | {cell(e["observation"])} |' for e in a['visualEvidence'])
    out += [table, 'Không suy chuyển động giữa các khung từ ảnh tĩnh.', '<a id="dien-bien"></a>\n\n## Diễn biến và nhiệm vụ từng beat']
    table = '| Mốc ASR | Diễn giải riêng | Vai trò |\n|---|---|---|\n'
    table += '\n'.join(f'| {timestamp(b["start"])}–{timestamp(b["end"])} | {cell(b["summary"])} | {cell(b["role"])} |' for b in a['beats'])
    out += [table, '<a id="cam-xuc"></a>\n\n## Nhịp cảm xúc — giả thuyết biên tập',
            'Các trạng thái dưới đây là cách đọc câu chuyện từ bằng chứng, không phải cảm xúc người xem đã đo hoặc biểu đồ retention.']
    table = '| Mốc | Cảm xúc có thể gợi | Bằng chứng | Cách diễn giải |\n|---|---|---|---|\n'
    table += '\n'.join(f'| {timestamp(e["start"])}–{timestamp(e["end"])} | {cell(e["emotion"])} | {cell(e["evidence"])} | {cell(e["interpretation"])} |' for e in d['emotionalArc'])
    out += [table, '## Cách phân phối thông tin']
    table = '| Mốc | Động tác viết | Vì sao đáng chú ý |\n|---|---|---|\n'
    table += '\n'.join(f'| {timestamp(e["start"])}–{timestamp(e["end"])} | {cell(e["move"])} | {cell(e["reason"])} |' for e in d['informationDesign'])
    out += [table, '## Giải đáp và cách kết', a['ending'], '## Điểm mạnh có dẫn chứng']
    out += ['- **' + s['point'] + '** — ' + s['evidence'] for s in d['strengths']]
    out += ['## Điểm yếu và điều không nên bắt chước']
    out += ['- **' + s['point'] + '** — ' + s['evidence'] for s in d['weaknesses']]
    out += ['## Khả năng được chia sẻ — chưa kiểm chứng',
            'Không có dữ liệu phân phối/retention để kết luận vì sao viral. Các ý sau chỉ là giả thuyết để thử:']
    out += ['- ' + s for s in d['shareabilityHypotheses']]
    out += ['<a id="ap-dung"></a>\n\n## Chuyển cơ chế sang bài mới', a['transfer']]
    out += ['- ' + s for s in d['adaptationRules']]
    out += ['Không dùng bài chuyển thể chưa được người dùng duyệt làm mẫu giọng lâu dài.',
            '## Mindmap', f'[Mã Mermaid riêng](../mindmaps/{a["id"]}.mmd)',
            '```mermaid\n' + mindmap(a).rstrip() + '\n```', '## Giới hạn còn lại']
    out += ['- ' + s for s in a['limitations']]
    for flag in v.get('promotionFlags', []):
        out += [f'- Đoạn tự quảng bá cộng đồng {timestamp(flag["start"])}–{timestamp(flag["end"])} theo ASR; chưa đủ xác định tài trợ bên thứ ba. Không coi đoạn này là mẹo giữ chân mặc định.']
    return '\n\n'.join(out).rstrip() + '\n'


def main():
    load = lambda name: json.loads((CORPUS / (name + '.json')).read_text(encoding='utf-8'))
    videos, analyses, patterns, collection = [load(n) for n in ['videos', 'analyses', 'patterns', 'collection']]
    by = {v['id']: v for v in videos}
    (CORPUS / 'mindmaps').mkdir(exist_ok=True)
    for a in analyses:
        v = by[a['id']]
        v['title'] = a['title']
        (CORPUS / v['casePath']).write_text(render_case(v, a), encoding='utf-8')
        (CORPUS / 'mindmaps' / (a['id'] + '.mmd')).write_text(mindmap(a), encoding='utf-8')
    (CORPUS / 'videos.json').write_text(json.dumps(videos, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    chunks = [f'# {len(patterns)} nhóm hook có clip đối chiếu',
              'Nhóm được rút từ corpus đã lưu, không phải công thức đặt trước. Nhóm ít ca là quan sát ca cụ thể, chưa chứng minh hiệu quả chung.',
              'Khi được yêu cầu tạo hook, mặc định trình **10 lựa chọn khác nhau**, dẫn về nhóm/clip/đoạn; chọn 3 hướng đáng phát triển. Số lượng người dùng yêu cầu được ưu tiên. Không cào trong tác vụ viết.']
    for p in patterns:
        chunks += [f'## {p["id"]} — {p["name"]}', '**Cơ chế:** ' + p['principle'], '**Bằng chứng:** ' + p['proof']]
        links = []
        for vid in p['videos']:
            v = by[vid]
            links.append(f'- [Phân tích {vid}](cases/{vid}.md) · [Video @{v["handle"]}]({v["url"]}) · {v["views"]:,} view · [Mindmap](cases/{vid}.md#mindmap).')
        chunks += ['\n'.join(links), '**Không học máy móc:** ' + p['limit']]
    (CORPUS / 'patterns.md').write_text('\n\n'.join(chunks).rstrip() + '\n', encoding='utf-8')
    intro = (f'# Kho TikTok tiếng Việt đã thu thập trước\n\n'
             f'**{collection["channelRecords"]} bản ghi · {collection["channels"]} kênh · {len(videos)} clip phân tích · {len(patterns)} nhóm hook · {len(analyses)} mindmap.**\n\n'
             '[Chọn nhóm hook](patterns.md) · [Metadata clip](videos.json) · [Phân tích JSON](analyses.json) · [Dữ liệu kênh](channel-videos.json) · [Baseline](channels.json) · [Phạm vi thu thập](collection.json)\n\n'
             'Skill đọc corpus tại chỗ. Chọn các ca phù hợp để đưa mặc định 10 lựa chọn hook, không tự cào. '
             'Mỗi ca có diễn biến, nhịp cảm xúc giả thuyết, phân phối thông tin, điểm mạnh/yếu, cách chuyển thể và mindmap Mermaid.\n\n'
             'Tiêu chí Việt Nam là kênh/lời tiếng Việt, không có analytics địa lý người xem. Mẫu có chủ đích, không đại diện toàn TikTok VN. '
             'Đã kiểm khung trích và ASR có mốc; chưa nghe toàn âm/xem liên tục. Không có retention.\n\n'
             '| Clip/chủ đề | Kênh | View lúc lấy | So P50 | Phân tích / sơ đồ |\n|---|---|---:|---:|---|\n')
    for v in videos:
        intro += f'| [{cell(v["title"])}]({v["url"]}) | @{v["handle"]} | {v["views"]:,} | {v["timesBaselineMedian"]:.2f}× | [Ca](cases/{v["id"]}.md) · [Mindmap](cases/{v["id"]}.md#mindmap) |\n'
    intro += ('\nP50 dùng bài >=48h trong tối đa 150 bài thu được mỗi kênh, không phải cả lịch sử. Có clip cũ ngoài cửa sổ baseline. '
              'Request danh sách và clip có timestamp riêng. Xem metadata từng ca; không suy causal uplift từ tỷ lệ view.\n')
    (CORPUS / 'index.md').write_text(intro, encoding='utf-8')
    print(f'Rendered {len(analyses)} cases and mindmaps, {len(patterns)} hook groups; no network.')


if __name__ == '__main__':
    main()
