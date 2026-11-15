# Hook & Script Kit — kho TikTok tiếng Việt

**Dữ liệu được cào và phân tích trước. Skill đọc kho có sẵn để viết.**

Đợt đầu đã cào **525 bản ghi từ 4 kênh**, tải lại và phân tích **12 clip**, rút ra **10 nhóm hook**. Mỗi nhóm có video gốc, chỉ số lúc thu thập và bản phân tích mở/nối/diễn biến/kết để đối chiếu. Không dùng kịch bản AI chưa duyệt làm mẫu.

## Mở kho

- [10 nhóm hook, từng nhóm kèm ca thực](skills/hook-script/references/corpus/patterns.md).
- [Mục lục 12 video và phân tích](skills/hook-script/references/corpus/index.md).
- [Dữ liệu 12 clip](skills/hook-script/references/corpus/videos.json), [525 bản ghi kênh](skills/hook-script/references/corpus/channel-videos.json), [baseline 4 kênh](skills/hook-script/references/corpus/channels.json).

Các kênh: **Long và Sóc, Người Quan Sát, Tình Báo Thị Trường, Lóng**. Clip có lời tiếng Việt và hướng tới ngữ cảnh người Việt; một số chủ đề nói về nước ngoài. Không có analytics vị trí người xem để khẳng định toàn bộ view ở Việt Nam.

Ví dụ có thể mở ngay: [CEO và chủ tịch](skills/hook-script/references/corpus/cases/7697361245959114000.md), [lương và mua trước trả sau](skills/hook-script/references/corpus/cases/7644506205179612423.md), [giả định tăng lương và lạm phát](skills/hook-script/references/corpus/cases/7359542441285930247.md).

## Dùng để viết

[Cài skill](INSTALL.md), hoặc dùng prompt kèm các bản phân tích được chọn:

- [Tạo hook từ kho](prompts/01-tao-hook.md).
- [Viết kịch bản từ kho](prompts/02-viet-kich-ban.md).
- [Sửa bài bằng đối chiếu](prompts/03-sua-bai.md).

```text
Dùng hook-script và kho đã lưu để đề xuất hook cho [chủ đề].
Khán giả / mục tiêu / giọng: [điền].
Chỉ rõ học từ nhóm và video/đoạn nào; không cào thêm khi viết.
```

## Phạm vi bằng chứng

Metadata và media của 12 clip được lấy lại ngày **2026-11-15**. Lượt xem từ **389.600 đến 7.600.000**. Cả 12 vượt 100.000 view và 3× P50 của snapshot kênh đủ tuổi 48 giờ; tỷ lệ thực tế từ khoảng 6,57× đến 71,15×. Đây là tiêu chí tuyển mẫu, không chứng minh một kỹ thuật gây viral hay đại diện toàn TikTok Việt Nam.

Đã xem các khung trích mới tải và đọc ASR có mốc từ bản lưu trước cùng ID. **Chưa nghe toàn âm hoặc xem liên tục**; có ghi lỗi/giới hạn từng ca. Không có dữ liệu retention. Một số clip nhiều view vẫn mở chậm hoặc hoãn đáp án: bản phân tích ghi cả điểm không nên học theo.

Repo chia sẻ metadata, đoạn hook ngắn, link gốc và phân tích riêng; không đăng lại toàn video hoặc transcript. Bộ dữ liệu nằm trong thư mục skill nên sao chép skill vẫn đủ nguồn để đọc tại chỗ.

> **English:** A pre-collected Vietnamese TikTok reference corpus: 525 channel records, 12 analyzed clips and 10 evidence-linked hook groups. The writing skill reads the bundled corpus; collection is a separate maintainer task.

[Phương pháp thu thập](MAINTENANCE.md) · [Nguồn và giấy phép](SOURCES.md) · [Đóng góp](CONTRIBUTING.md) · [Kiểm tra](evals/cases.md) · [MIT](LICENSE)
