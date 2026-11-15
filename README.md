# Hook & Script Kit — kho TikTok tiếng Việt

**Dữ liệu được cào và phân tích trước. Skill đọc kho có sẵn để viết.**

Kho hiện có **1.949 bản ghi từ 14 kênh**, tải media và phân tích **40 clip**, rút ra **26 nhóm hook**. Mỗi nhóm có video gốc, chỉ số lúc thu thập và bản phân tích mở/nối/diễn biến/kết để đối chiếu. Không dùng kịch bản AI chưa duyệt làm mẫu.

## Mở kho

- [26 nhóm hook, từng nhóm kèm ca thực](skills/hook-script/references/corpus/patterns.md).
- [Mục lục 40 video, phân tích và sơ đồ diễn biến](skills/hook-script/references/corpus/index.md).
- [Dữ liệu 40 clip](skills/hook-script/references/corpus/videos.json), [1.949 bản ghi kênh](skills/hook-script/references/corpus/channel-videos.json), [baseline 14 kênh](skills/hook-script/references/corpus/channels.json).

Thêm **8 kênh mới**, mỗi kênh hai clip: Trang Ngân Hàng, Sitcom Tài Chính, Thầy Quéo, VTV24, D Trending, Kiến Thức Kinh Tế, Vietcetera và Quốc Thích Kinh Tế. Giữ sáu nguồn trước để đối chiếu. Xem [phân bố kênh/cách thể hiện](skills/hook-script/references/corpus/channels.md). Clip có lời tiếng Việt và hướng tới ngữ cảnh người Việt; một số chủ đề nói về nước ngoài. Không có analytics vị trí người xem để khẳng định toàn bộ view ở Việt Nam.

Ví dụ có thể mở ngay: [CEO và chủ tịch](skills/hook-script/references/corpus/cases/7697361245959114000.md), [lương và mua trước trả sau](skills/hook-script/references/corpus/cases/7644506205179612423.md), [giả định tăng lương và lạm phát](skills/hook-script/references/corpus/cases/7359542441285930247.md).

## Phân tích và sơ đồ diễn biến

Mỗi ca có lời hứa/câu hỏi trung tâm, bảng diễn biến theo mốc, nhịp cảm xúc giả thuyết, cách phân phối thông tin, điểm mạnh/yếu có dẫn chứng, cách chuyển thể và **sơ đồ dọc theo thời gian**: đọc từ trên xuống, mỗi hộp có mốc và một diễn biến; mở đầu màu xanh dương, nhịp cuối màu xanh lá. Sơ đồ render trực tiếp trên GitHub; có file `.mmd` riêng trong corpus.

Xem thử [E10 và phần mềm lậu — sơ đồ diễn biến](skills/hook-script/references/corpus/cases/7651946778392153362.md#mindmap) hoặc [cảnh giả định không có thuế](skills/hook-script/references/corpus/cases/7702669503209016594.md#mindmap).

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

Khi có đủ ca hợp brief, nguồn cho 10 option ưu tiên **≥5 kênh, ≥3 cách thể hiện, ≤2 option/kênh**. Các mẫu gồm hoạt hình, người dẫn, tiểu phẩm, phóng sự, tin ngắn và phỏng vấn.

Mặc định khi hỏi tạo hook: **10 option để so sánh**, rồi **3 hướng được phát triển** với nhịp nối, hình mở gợi ý và phần cần giải đáp. Người dùng yêu cầu số khác thì theo số đó. Độ đa dạng dựa vào cơ chế/góc nhìn, không chỉ đổi vài chữ; không ép nguồn không liên quan để đủ số.

## Phạm vi bằng chứng

Metadata/media được lấy ngày **2026-11-15**, mỗi request có timestamp riêng. Cả 40 clip vượt 100.000 view và 3× P50 snapshot kênh đủ tuổi 48 giờ. View từ **157,000 đến 7,600,000**; dấu phẩy tách hàng nghìn. Đây là tiêu chí tuyển mẫu, không chứng minh một kỹ thuật gây viral hoặc đại diện toàn TikTok Việt Nam.

Đã xem khung trích và đọc ASR có mốc: 24 ca trước dùng ASR đã lưu; 16 ca mới chạy ASR từ media mới tải. **Chưa nghe toàn âm hoặc xem liên tục**, không có retention. Một ca Techcombank có hashtag hợp tác, được ghi rõ để người viết biết ngữ cảnh. Các ca mở chậm, điều kiện trả muộn, lời quảng bá hoặc nhận dạng lỗi đều được phân tích cả điểm không nên học theo.

Repo chia sẻ metadata, đoạn hook ngắn, link gốc và phân tích riêng; không đăng lại toàn video hoặc transcript. Bộ dữ liệu nằm trong thư mục skill nên sao chép skill vẫn đủ nguồn để đọc tại chỗ.

> **English:** A pre-collected Vietnamese TikTok corpus: 1,949 channel records, 14 channels, 40 detailed clip analyses with vertical story diagrams, and 26 evidence-linked hook groups. The writing skill reads bundled data; collection is a separate maintainer task.

[Phương pháp thu thập](MAINTENANCE.md) · [Nguồn và giấy phép](SOURCES.md) · [Đóng góp](CONTRIBUTING.md) · [Kiểm tra](evals/cases.md) · [MIT](LICENSE)
