# Lượt tự kiểm bản đầu

**Ngày:** 2026-11-15. **Cách làm:** agent biên soạn tự áp dụng skill vào ba input trong [cases](cases.md), rồi đối chiếu tiêu chí. Đây là tự kiểm cùng người viết, chưa phải thử độc lập hay benchmark nhiều model. Không có video, bản đọc hoặc dữ liệu retention.

**Kiểm kỹ thuật đã thực hiện:** 19 file Markdown không có liên kết nội bộ thiếu/thoát repo; frontmatter skill qua trình kiểm của skill-creator; sao chép skill vào hai cây thư mục `.agents/skills/` và `.claude/skills/` trong thư mục tạm đều đủ tham chiếu. Đã thử trình kiểm với tham chiếu thiếu và tham chiếu thoát thư mục, đều bị phát hiện. Đã tính lại số học của cả năm ví dụ bằng Python, gồm Decimal cho lãi kép và tỷ lệ sức mua. Đây là kiểm tính độc lập của gói file, chưa phải kiểm việc model tự chọn skill trong hai ứng dụng.

## A — Đầu ra hook

Mục tiêu: hiểu sức mua, không đo CPI thực tế.

| Cơ chế | Câu mở | Câu nối | Thân bài cần trả lời |
|---|---|---|---|
| Hành động | “An vừa bỏ một món khỏi giỏ.” | “Trong ví dụ giả định, giá giỏ cũ đã vượt khoản tiền cậu mang.” | Cho thấy cùng tiền không còn mua đủ giỏ cũ |
| Đối chiếu | “Lương tăng, giỏ hàng lại vơi.” | “Giả sử lương tăng chậm hơn giá của cùng những món hàng.” | So thu nhập và chi phí với điều kiện rõ |
| Câu hỏi vận dụng | “Tiền trong ví còn mua đủ không?” | “Thử giữ nguyên giỏ hàng rồi đổi bảng giá.” | Đổi giá làm sức mua của ngân sách thay đổi |

Khuyến nghị hành động: có hình cụ thể ngay khi mở. Không cần hỏi thêm khán giả. Ba phương án khác nhau ở cửa vào; chưa tuyên bố đây là kết quả thị trường hay viết cả kịch bản. **Tự kiểm: đạt các tiêu chí A.**

## B — Chẩn đoán và đầu ra sửa

“An chỉ có một triệu” bỏ tiền đã rút. “Hãy luôn nhập lãi” vượt quá điều ví dụ chứng minh. “Lãi kép rất tuyệt vời” nhận xét thay cho tình huống.

Ba cách mở: **so sánh** “Cùng gửi một triệu, sao tiền khác nhau?”; **dự đoán** “Năm sau tiền lãi vẫn như năm trước?”; **lựa chọn** “Bạn lấy lãi ra hay để lại?”. Câu nối tương ứng: khác cách xử lý lãi; cơ sở tính năm hai đã đổi; cần cân nhắc dùng tiền và tích lũy. Cả ba cần trả lời bằng bảng hai kỳ; chọn so sánh để bám bài cũ.

| Thời gian ước tính | Lời đọc sửa | Hình gợi ý |
|---|---|---|
| 0–5s | Cùng gửi một triệu, sao tiền khác nhau? | Hai tài khoản bằng nhau |
| 5–17s | Giả định lãi mười phần trăm mỗi năm trong hai năm, không thêm vốn, bỏ qua thuế và phí. An rút lãi để riêng, không sinh lãi. Bình để lãi nhập gốc cuối năm. | Nhãn giả định và điều kiện chung |
| 17–30s | Hết năm đầu, mỗi người có một trăm nghìn tiền lãi. Khoản đó ở ví riêng của An, còn với Bình, nó ở lại tài khoản. | Tách ví riêng khỏi tài khoản |
| 30–44s | Năm hai, An nhận thêm một trăm nghìn; Bình nhận một trăm mười nghìn vì số tiền tính lãi đã lớn hơn. | 1 triệu ×10%; 1,1 triệu ×10% |
| 44–57s | Tính cả tiền đã rút, An có một triệu hai trăm nghìn, Bình có một triệu hai trăm mười nghìn. Chênh mười nghìn đến từ lãi sinh thêm trên lãi cũ. | Tổng 1,2 triệu / 1,21 triệu |
| 57–65s | Giữ lãi giúp tích lũy trong giả định này. Rút hay giữ còn tùy bạn có cần dùng khoản tiền ấy không. | Hai mục đích dùng tiền |

Đã giữ vốn, lãi và kỳ hạn; sửa phép so và kết luận. Đáp án hook ở đoạn so tổng. Thời gian chưa đo bằng bản đọc. **Tự kiểm: đạt các tiêu chí B.**

## C — Đầu ra thay thế số liệu thiếu nguồn

Chưa có nguồn cho tỷ lệ 90%, nên bỏ tỷ lệ ấy khỏi câu khẳng định. Có thể viết hấp dẫn bằng vấn đề sức mua:

| Cơ chế | Câu mở | Câu nối | Thân bài cần trả lời |
|---|---|---|---|
| Hai cách đo | “Số dư tăng; sức mua thì sao?” | “Số tiền lớn hơn chưa nói hết lượng hàng mua được.” | So tiền và giá của giỏ giả định |
| Tình huống | “Bình nhận lãi, rồi vẫn bỏ bớt đồ.” | “Trong ví dụ giả định, giỏ hàng tăng nhanh hơn khoản tiền cậu có.” | Chỉ ra điều kiện khiến sức mua giảm |
| Phép thử | “Lãi có theo kịp giá của giỏ hàng?” | “Đặt hai tỷ lệ cùng kỳ cạnh nhau rồi mới kết luận.” | Tính tỷ lệ sức mua, không đánh đồng với mọi người gửi tiền |

Khuyến nghị hai cách đo vì ngắn và đúng mục tiêu. Không có tỷ lệ mới hoặc nguồn giả. Ví dụ nhận lãi mà sức mua giảm chỉ đúng với điều kiện đã nêu. **Tự kiểm: đạt các tiêu chí C.**
