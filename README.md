# Hook & Script Kit

Học từ clip thật để viết hook và kịch bản video giáo dục, tài chính.

**Luồng chính: tìm clip → phân tích bằng chứng → rút cơ chế → viết mới → xem lại kết quả.** Không lấy bài AI tự viết rồi tự chấm làm chuẩn chất lượng.

Repo hiện cung cấp skill, prompt và mẫu ghi phân tích. **Chưa có clip nào được kiểm trực tiếp và duyệt vào thư viện của bộ này.** Các bài tự viết ở bản đầu đã được gỡ khỏi bản hiện hành theo phản hồi của chủ repo; không dùng chúng làm mẫu giọng hoặc nguồn học.

> **English:** A research-first Vietnamese video-writing skill. Analyze reference clips before deriving hooks and scripts. The verified clip library is currently empty; this is a workflow toolkit, not a validated viral dataset.

## Dùng ngay

- [Phân tích clip rồi tạo hook](prompts/01-tao-hook.md): đưa URL/file clip hoặc yêu cầu agent tìm clip cùng chủ đề.
- [Viết kịch bản từ phân tích](prompts/02-viet-kich-ban.md): mỗi lựa chọn ghi rõ học từ clip và nhịp nào.
- [Sửa bài qua đối chiếu](prompts/03-sua-bai.md): chỉ ra khác biệt giữa bài hiện tại và cách triển khai trong clip tham khảo.
- [Cài skill](INSTALL.md) cho agent dùng thường xuyên.

```text
Chủ đề cần viết: [chủ đề của bạn]
Khán giả / mục tiêu / giọng: [điền]
Clip tham khảo: [URL hoặc file; nếu chưa có, hãy tìm clip phù hợp]
Việc cần làm: phân tích trước, sau đó đề xuất hook hoặc kịch bản.
Bài riêng đã được tôi duyệt làm mẫu, nếu có: [đường dẫn hoặc để trống]
```

Nếu không truy cập được clip, agent phải nói rõ tài liệu nào đã đọc: video, transcript hay bài phân tích thứ cấp. Không được nhận đã xem clip, đặt mốc hình/âm hoặc bịa dữ liệu hiệu quả. Thiếu nguồn thì tìm nguồn khác hoặc xin đầu vào còn thiếu; không lấp bằng một kho mẫu tự sinh.

## Trong bộ này

| Phần | Công dụng |
|---|---|
| [Quy trình](skills/hook-script/references/workflow.md) | Từ chọn clip đến viết mới, có truy vết |
| [Cách thu thập và phân tích](skills/hook-script/references/analysis.md) | Đầu vào thực, phạm vi đã xem và nhịp giữ chân |
| [Mẫu ghi breakdown](skills/hook-script/references/breakdown-template.md) | Nguồn, mốc quan sát, suy luận và cách chuyển thể |
| [Kiểm kết quả](skills/hook-script/references/review.md) | Đối chiếu nguồn và phần viết mới |
| [Thư viện clip](library/README.md) | Phân biệt nguồn ứng viên, bản đã phân tích và nguồn đã duyệt |

Kho công thức của [rediumvex](https://github.com/rediumvex/viral-hooks-skill) dùng để gọi tên/so sánh cơ chế sau phân tích. Hướng tổ chức phân tích clip học từ [shixinzhang](https://github.com/shixinzhang/tiktok-viral-hooks). Không có dữ liệu chứng minh bộ này tăng retention; lượt xem và đánh giá của nguồn ngoài chưa được xác nhận độc lập.

[Nguồn và giấy phép](SOURCES.md) · [Đóng góp](CONTRIBUTING.md) · [Kiểm hành vi](evals/cases.md) · [MIT License](LICENSE)
