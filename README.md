# Hook & Script Kit

Viết video giáo dục, tài chính dễ nghe và có lý do để xem tiếp.

Bộ tiếng Việt gồm **20 mẫu hook**, **5 cấu trúc kịch bản**, **5 ví dụ hoàn chỉnh**, **3 prompt** và **1 AI skill**. Dùng cho video ngắn khoảng 30–90 giây. Không cần API key hay phần mềm dựng video để đọc và dùng bộ này. Công cụ AI bạn chọn có thể có phí riêng.

> **English:** A Vietnamese hook and short-video writing toolkit for education and finance. Includes reusable prompts, a portable AI skill, original examples, and editorial checks. Original material is MIT licensed.

## Dùng ngay

Chọn một cách:

- **Chỉ cần viết:** mở [prompt tạo hook](prompts/01-tao-hook.md), thay phần đầu vào rồi dán vào công cụ chat của bạn.
- **Đã có ý tưởng:** dùng [prompt viết kịch bản](prompts/02-viet-kich-ban.md).
- **Bài đang chán:** dùng [prompt sửa bài](prompts/03-sua-bai.md).
- **Dùng thường xuyên với agent:** [cài skill](INSTALL.md).

Ví dụ đầu vào:

```text
Chủ đề: vì sao lương tăng mà vẫn thấy thiếu tiền?
Khán giả: người mới đi làm, chưa học kinh tế.
Mục tiêu: hiểu sức mua, không tư vấn đầu tư.
Nền tảng / thời lượng: video dọc, khoảng 60 giây.
Giọng: gần gũi, hài nhẹ, xưng bạn.
Dữ kiện: dùng ví dụ giả định, không nêu CPI thực tế.
```

Bạn sẽ nhận ba hook khác cơ chế, câu nối, điều thân bài cần giải đáp và một khuyến nghị. Khi chuyển sang kịch bản, đầu ra là bảng **thời lượng ước tính / lời đọc / hình gợi ý**, kèm phép tính hoặc nguồn cần kiểm.

## Đọc theo nhu cầu

| Cần làm gì | Đọc gì |
|---|---|
| Bắt đầu từ chủ đề | [Quy trình viết](skills/hook-script/references/workflow.md) |
| Đổi cách mở đầu | [20 mẫu hook](skills/hook-script/references/hooks.md) |
| Kể cho đến hết | [5 cấu trúc](skills/hook-script/references/structures.md) |
| Tự sửa trước khi đăng | [Kiểm bài và phân tích video](skills/hook-script/references/review.md) |
| Hiểu cách áp dụng | [Lạm phát](examples/01-lam-phat.md) · [Lãi kép](examples/02-lai-kep.md) · [Chi phí vay](examples/03-chi-phi-vay.md) · [Bán khống](examples/04-ban-khong.md) · [Lý thuyết trò chơi](examples/05-ly-thuyet-tro-choi.md) |

## Cách bộ này chọn hook

Câu mở cần cho người xem biết chuyện gì đang xảy ra. Nhịp kế tiếp cho họ một lý do để quan tâm. Thân bài giải đáp đúng điều đã gợi.

Thử ba cơ chế khác nhau trước khi chọn: chẳng hạn một hành động, một phép so sánh và một câu hỏi có đánh đổi. Giữ một ý chính; đọc thành tiếng để bỏ câu rào và câu quá dài. Khoảng ba giây đầu là điểm kiểm sự rõ ràng, không phải khuôn ép mọi hook vào đúng ba giây.

Các mẫu là gợi ý sáng tác. Chưa có dữ liệu thử nghiệm chứng minh bộ này làm tăng retention hoặc đảm bảo video viral. Số liệu thực tế cần nguồn; số giả định cần ghi nhãn. Ví dụ học cơ chế tài chính không thay thế đánh giá một sản phẩm hay quyết định đầu tư cụ thể.

## Đóng góp

Gửi issue hoặc pull request theo [hướng dẫn đóng góp](CONTRIBUTING.md). Ưu tiên ví dụ có đầu vào, bản trước/sau và lý do sửa. Không đưa dữ liệu khách hàng, tài liệu nội bộ hoặc transcript không có quyền chia sẻ.

[Nguồn học và giấy phép](SOURCES.md) · [MIT License](LICENSE) · [Các tình huống đánh giá](evals/cases.md)
