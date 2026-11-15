# Hook & Script Kit — kho TikTok tiếng Việt

**Dữ liệu được cào và phân tích trước. Skill đọc kho có sẵn để viết.**

Đợt đầu đã cào **749 bản ghi từ 6 kênh**, tải lại và phân tích **24 clip**, rút ra **19 nhóm hook**. Mỗi nhóm có video gốc, chỉ số lúc thu thập và bản phân tích mở/nối/diễn biến/kết để đối chiếu. Không dùng kịch bản AI chưa duyệt làm mẫu.

## Mở kho

- [19 nhóm hook, từng nhóm kèm ca thực](skills/hook-script/references/corpus/patterns.md).
- [Mục lục 24 video, phân tích và mindmap](skills/hook-script/references/corpus/index.md).
- [Dữ liệu 24 clip](skills/hook-script/references/corpus/videos.json), [749 bản ghi kênh](skills/hook-script/references/corpus/channel-videos.json), [baseline 6 kênh](skills/hook-script/references/corpus/channels.json).

Các kênh: **Long và Sóc, Người Quan Sát, Tình Báo Thị Trường, Lóng, Huyền Chứng Khoán 101, iftactix**. Clip có lời tiếng Việt và hướng tới ngữ cảnh người Việt; một số chủ đề nói về nước ngoài. Không có analytics vị trí người xem để khẳng định toàn bộ view ở Việt Nam.

Ví dụ có thể mở ngay: [CEO và chủ tịch](skills/hook-script/references/corpus/cases/7697361245959114000.md), [lương và mua trước trả sau](skills/hook-script/references/corpus/cases/7644506205179612423.md), [giả định tăng lương và lạm phát](skills/hook-script/references/corpus/cases/7359542441285930247.md).

## Phân tích và mindmap

Mỗi ca có lời hứa/câu hỏi trung tâm, bảng diễn biến theo mốc, nhịp cảm xúc giả thuyết, cách phân phối thông tin, điểm mạnh/yếu có dẫn chứng, cách chuyển thể và **mindmap Mermaid**. Sơ đồ render trực tiếp trên GitHub; có file `.mmd` riêng trong corpus.

Xem thử [E10 và phần mềm lậu — mindmap](skills/hook-script/references/corpus/cases/7651946778392153362.md#mindmap) hoặc [cảnh giả định không có thuế](skills/hook-script/references/corpus/cases/7702669503209016594.md#mindmap).

## Dùng để viết

[Cài skill](INSTALL.md), hoặc dùng prompt kèm các bản phân tích được chọn:

- [Tạo hook từ kho](prompts/01-tao-hook.md).
- [Viết kịch bản từ kho](prompts/02-viet-kich-ban.md).
- [Sửa bài bằng đối chiếu](prompts/03-sua-bai.md).

```text
Dùng hook-script và kho đã lưu để đề xuất hook cho [chủ đề].
Khán giả / mục tiêu / giọng: [điền].
Cho tôi nhiều lựa chọn: mặc định 10 hook khác góc/cơ chế, dẫn nhóm và
video/đoạn nguồn. Chọn 3 ID để phát triển. Không cào thêm khi viết.
```

Mặc định khi hỏi tạo hook: **10 option để so sánh**, rồi **3 hướng được phát triển** với nhịp nối, hình mở gợi ý và phần cần giải đáp. Người dùng yêu cầu số khác thì theo số đó. Độ đa dạng dựa vào cơ chế/góc nhìn, không chỉ đổi vài chữ; không ép nguồn không liên quan để đủ số.

## Phạm vi bằng chứng

Metadata và media của 24 clip được lấy lại ngày **2026-11-15**. Lượt xem từ **232.400 đến 7.600.000**. Cả 24 vượt 100.000 view và 3× P50 của snapshot kênh đủ tuổi 48 giờ; tỷ lệ thực tế từ khoảng 5,69× đến 353,47×. Đây là tiêu chí tuyển mẫu, không chứng minh một kỹ thuật gây viral hay đại diện toàn TikTok Việt Nam.

Đã xem các khung trích mới tải và đọc ASR có mốc từ bản lưu trước cùng ID. **Chưa nghe toàn âm hoặc xem liên tục**; có ghi lỗi/giới hạn từng ca. Không có dữ liệu retention. Một số clip nhiều view vẫn mở chậm hoặc hoãn đáp án: bản phân tích ghi cả điểm không nên học theo.

Repo chia sẻ metadata, đoạn hook ngắn, link gốc và phân tích riêng; không đăng lại toàn video hoặc transcript. Bộ dữ liệu nằm trong thư mục skill nên sao chép skill vẫn đủ nguồn để đọc tại chỗ.

> **English:** A pre-collected Vietnamese TikTok reference corpus: 749 channel records, 24 detailed clip analyses with Mermaid mindmaps, and 19 evidence-linked hook groups. The writing skill reads the bundled corpus; collection is a separate maintainer task.

[Phương pháp thu thập](MAINTENANCE.md) · [Nguồn và giấy phép](SOURCES.md) · [Đóng góp](CONTRIBUTING.md) · [Kiểm tra](evals/cases.md) · [MIT](LICENSE)
