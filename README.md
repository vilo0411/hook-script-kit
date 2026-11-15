# Hook & Script Kit — học từ TikTok tiếng Việt nhiều ngách

**Thu thập và phân tích trước. Skill đọc dữ liệu tại chỗ khi viết.**

Kho hiện có **3,149 bản ghi, 22 kênh, 56 ca phân tích, 35 nhóm hook**. Đợt mới thêm **16 mẫu ngoài tài chính từ 8 kênh**, gồm nấu ăn, du lịch, công nghệ, kiến thức, hài/biểu diễn, làm đẹp/bán hàng và gặp gỡ đường phố.

Bộ 10 hook thử về lương tăng đã bị người dùng loại. [Đọc chỗ thiếu và đối chiếu hai repo](skills/hook-script/references/reference-audit.md). Bản sửa học cả hành động/hình mở, thông tin chưa biết, nhịp nối và mốc trả; không dùng các câu bị loại làm mẫu giọng hoặc cho rằng nhiều dữ liệu tự bảo đảm câu hay.

## Mở kho

- [16 nghiên cứu phần mở ngoài ngách](skills/hook-script/references/corpus/hook-studies.md): lời/hình/chữ, điều còn muốn biết, mốc trả và hai câu tóm cấu trúc.
- [56 video cùng phân tích và sơ đồ dọc](skills/hook-script/references/corpus/index.md).
- [22 kênh và phân bố ngách/cách thể hiện](skills/hook-script/references/corpus/channels.md).
- [35 nhóm có ca đối chiếu](skills/hook-script/references/corpus/patterns.md).
- [Metadata clip](skills/hook-script/references/corpus/videos.json), [bản ghi kênh](skills/hook-script/references/corpus/channel-videos.json), [baseline](skills/hook-script/references/corpus/channels.json).

Tám kênh ngoài ngách: **Khoai Lang Thang, Ông Anh Thích Nấu Ăn (`genjadao`), Kiến Không Ngủ (`kienkhongngu_official`), Vật Vờ Studio, Việt Phương Thoa, Thủng Long Family, Hà Linh, Quan Không Gờ**. Mỗi kênh thêm hai ca; giữ 40 ca trước để đối chiếu. Không tính các tài khoản trùng tên ít bài/không đạt ngưỡng hoặc lượt tải chỉ có âm thanh là nguồn video đã phân tích.

## Xem cách một phần mở vận hành

- [Xe mui trần gặp mưa](skills/hook-script/references/corpus/cases/7691281157266132231.md): câu hỏi có hình, đổi điều kiện qua các lần thử, trả từng mức kết quả; không xác nhận kỹ thuật hay hướng dẫn tái tạo.
- [Lời quả quyết trước đám cưới](skills/hook-script/references/corpus/cases/7653107443475467527.md): lời dự đoán được montage về sau kiểm lại.
- [Một người lạ trong chuyến đi](skills/hook-script/references/corpus/cases/7429725622441659649.md): chỉ đúng nhân vật, còn giữ lại hành động khiến cuộc gặp đáng kể.

Mỗi ca có sơ đồ **một cột theo thời gian**, mốc rõ, chữ lớn; đọc phần mở màu xanh dương tới nhịp cuối màu xanh lá. Bảng bên dưới giữ phân tích cảm xúc giả thuyết, cách chia thông tin, điểm mạnh/yếu và giới hạn. Liên kết cũ `#mindmap` vẫn mở đúng sơ đồ.

## Dùng để viết

[Cài skill](INSTALL.md), rồi dùng [prompt tạo hook](prompts/01-tao-hook.md), [viết bài](prompts/02-viet-kich-ban.md) hoặc [sửa bài](prompts/03-sua-bai.md).

```text
Dùng hook-script và kho đã lưu cho [chủ đề/sự việc].
Khán giả, giọng và phần nội dung thực sự sẽ giải đáp: [...].
Cho 10 lựa chọn, mỗi hướng có câu mở, hình/hành động đầu tiên,
điều còn muốn biết và ca/đoạn học từ. Phát triển 3 ID.
Có thể học nguồn ngoài ngách khi chuyển được cách chia thông tin.
Không cào thêm khi viết; không chỉ đổi danh từ trên một công thức.
```

Mười option cần khác trải nghiệm và góc tiếp cận; nhiều kênh không tự tạo ra nhiều kiểu mở. Mục tiêu ≥5 kênh, ≥3 cách thể hiện, ≤2 option/kênh chỉ giúp chống lặp khi có đủ nguồn phù hợp. Brief và lựa chọn người dùng được ưu tiên. Không thay gate/settings hay tự duyệt kịch bản dự án.

## Phạm vi bằng chứng

Metadata/media lấy ngày **2026-11-15**, mỗi request có timestamp riêng. Tất cả ca vượt 100.000 view và 3× P50 snapshot đủ 48 giờ. Đây là tiêu chí tuyển mẫu, không chứng minh nguyên nhân viral. Kênh/lời/chữ/ngữ cảnh tiếng Việt không đồng nghĩa có analytics khán giả ở Việt Nam; địa điểm/chủ đề có thể ở nước ngoài.

Đã xem khung trích và đọc ASR: 24 ca trước dùng bản lưu, 32 ca bổ sung chạy mới. **Chưa nghe toàn âm hoặc xem liên tục; không có retention.** Bốn ca ngoài ngách chỉ đủ học hình/chữ vì ASR ảo hoặc là nhạc, được gắn `sampled-visual-only`; không dùng chúng làm bằng chứng lời thoại. Các ca quảng bá/hợp tác được ghi rõ, không giả định view tự nhiên. Mọi dữ kiện trong clip vẫn cần xác minh riêng trước khi dùng cho bài mới.

Repo chỉ chia sẻ metadata chuẩn hóa, link gốc, trích ngắn và phân tích riêng; giữ video/toàn ASR ở bộ nghiên cứu cục bộ. Skill sao chép riêng vẫn đủ nguồn để đọc, không cần crawler lúc dùng.

> **English:** A pre-collected Vietnamese TikTok corpus across niches: 3,149 channel records, 22 channels, 56 analyses, 35 source-linked groups and 16 cross-niche opening studies. Evidence scope and commercial context are explicit; the writing skill uses bundled offline data.

[Phương pháp](MAINTENANCE.md) · [Nguồn](SOURCES.md) · [Đóng góp](CONTRIBUTING.md) · [Kiểm tra](evals/cases.md) · [MIT](LICENSE)
