# Nguồn và phạm vi học

## Hai repo tham khảo

- [rediumvex/viral-hooks-skill](https://github.com/rediumvex/viral-hooks-skill): kho công thức và skill chọn hook. Dùng làm vốn từ gọi tên/so sánh cơ chế sau khi phân tích nguồn; không phải bằng chứng một công thức hiệu quả trong mọi video. [MIT nguồn](https://github.com/rediumvex/viral-hooks-skill/blob/main/LICENSE).
- [shixinzhang/tiktok-viral-hooks](https://github.com/shixinzhang/tiktok-viral-hooks): thư viện breakdown, mục lục theo chủ đề/cơ chế và công cụ xuất bản. Học luồng từ nội dung clip đến phân tích nhịp kể và ứng dụng mới. [Generator](https://github.com/shixinzhang/tiktok-viral-hooks/blob/main/_scripts/generate_breakdown.py) nhận bản phân tích từ backend TokTranscript; clone repo không tự cung cấp backend đó. Không có backend/tích hợp trả phí được cài trong bộ này.

Đã đọc README, giấy phép, kho công thức của repo thứ nhất; README, mục lục finance, template, hai bài tài chính và generator của repo thứ hai. Việc đọc repo không đồng nghĩa đã xem clip gốc, xác nhận lượt xem hoặc kiểm chứng nguyên nhân viral.

## Giấy phép và bằng chứng

Nội dung repo thứ hai theo [CC BY-NC-SA 4.0](https://github.com/shixinzhang/tiktok-viral-hooks/blob/main/LICENSE), mã trong `_scripts/` theo MIT. Repo này không chép bài breakdown, transcript hoặc ảnh nguồn vào phần MIT. Liên kết nguồn không đổi giấy phép của tài liệu bên ngoài.

[MIT](LICENSE) áp dụng cho phần hướng dẫn/prompt tự viết ở đây. Khi thêm ca phân tích, dẫn nguồn và chỉ chia sẻ phần có quyền; không coi một đoạn transcript/video là tài sản MIT vì được liên kết từ repo này.

## Thay đổi theo phản hồi chủ repo

Bản đầu đã đặt bài và hook AI tự viết làm ví dụ. Chủ repo chưa ưng ý và không chấp nhận dùng làm mẫu. Bản hiện hành gỡ năm bài đó, bảng 20 hook, năm cấu trúc định sẵn và phần tự chấm đi kèm khỏi nguồn dùng hiện tại. Lịch sử Git giữ thay đổi để truy vết, không phải thư viện mẫu.

Đợt trước đã bổ sung [corpus TikTok tiếng Việt](skills/hook-script/references/corpus/index.md): 1.949 bản ghi 14 kênh, 40 ca có media được tải lại, 40 sơ đồ diễn biến và 26 nhóm hook có bằng chứng. Skill đọc kho này khi viết, không tự cào. Xem [phương pháp](MAINTENANCE.md) về cách tuyển mẫu, reuse ASR và giới hạn review.


Đợt ngoài ngách: corpus hiện 3,149 bản ghi, 22 kênh, 56 ca và 35 nhóm; 16 ca mới có nghiên cứu lời/hình/chữ và cấu trúc hai câu. Đọc [đối chiếu nguồn tham khảo](skills/hook-script/references/reference-audit.md) và [phạm vi từng ca](skills/hook-script/references/corpus/hook-studies.md). Không coi nhãn hiệu quả/thuật toán của repo tham khảo là dữ liệu retention đã đo.
