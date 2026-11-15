# Đối chiếu hai repo và sửa lỗi đầu ra

## Phản hồi trực tiếp

Người dùng đã loại cả 10 hook trong lượt mẫu chủ đề lương tăng/hết tiền. Trạng thái: **rejected-by-user**. Không có câu nào trong bộ đó được duyệt làm mẫu giọng hay mẫu chất lượng. Không lặp nguyên bộ, không tự sửa nhãn rồi trình như mẫu đã thành công. Chưa đủ phản hồi để kết luận người dùng ghét một thể loại, số liệu hay mọi câu hỏi nói chung.

## Hai nguồn thực sự làm gì

- [rediumvex — SKILL.md](https://github.com/rediumvex/viral-hooks-skill/blob/main/SKILL.md): xác định cảm xúc phù hợp, phối hướng gây chú ý với hướng giữ người xem, viết gọn và dùng ngôn ngữ đúng nền tảng. Kho này là 100 cấu trúc ở 10 nhóm tâm lý; **không phải corpus 100 video được mổ xẻ**. Các nhãn “battle-tested” trong nguồn không đi kèm benchmark kiểm chứng trong các file đã đọc. Mốc 12 từ là hướng dẫn tiếng Anh của nguồn, không áp máy móc theo dấu cách tiếng Việt.
- [shixinzhang — README](https://github.com/shixinzhang/tiktok-viral-hooks): tổ chức theo ngách và kiểu mở, đặt lời mở cạnh nhịp cảm xúc, bước diễn biến và phần chuyển cơ chế sang bài mới. Giá trị cần học là chuỗi mở → điều chưa biết → nhịp nối → trả lời; không chỉ tên công thức hoặc số view.
- Đã đọc lại ba breakdown tháng 11: [Shazam](https://github.com/shixinzhang/tiktok-viral-hooks/blob/main/breakdowns/en/2026-11/tiktok-transcript-how-shazam-s-transformation-works-69ec.md), [review tóc](https://github.com/shixinzhang/tiktok-viral-hooks/blob/main/breakdowns/en/2026-11/tiktok-transcript-replying-to-mieko-hair-details-ft-oqhair-oqhairshop-oqhairre-11b4.md), [bóng đá](https://github.com/shixinzhang/tiktok-viral-hooks/blob/main/breakdowns/en/2026-11/tiktok-transcript-wow-your-so-strong-kante-football-sakinakarchaoui-mbappe-bf96.md). Có hạn chế rõ: metadata duration bằng 0 trong cả ba, mốc thời gian/khẳng định về thuật toán không có dữ liệu chứng minh trong trang; một số sơ đồ thiếu hoặc khác ngôn ngữ. Không sao chép cách khẳng định nhân quả hoặc gán cả câu dài vào ba giây.

Đợt đối chiếu 2026-11-15; file SKILL rediumvex blob `8c489d0eb48447af6ebf3e0297f386b226d5ecb8`, README shixinzhang blob `8b93459dbf89ead1c0e6e3ae18f8df2b9e63c3c4`. Chỉ ghi nhận phương pháp bằng diễn giải riêng, không nhập bài CC BY-NC-SA vào corpus MIT.

## Chẩn đoán đầu ra vừa bị loại

Đây là nhận định biên tập từ đầu ra và phản hồi, không phải kết quả đo retention:

1. **Đưa chủ đề vào câu hỏi thay vì tìm một sự việc đáng xem.** Nhiều câu chỉ đổi cách nói “vì sao hết tiền”; người xem đã đoán được lời giải chung chung là chi tiêu tăng.
2. **Tên cơ chế thay cho bước chuyển thực tế.** Dẫn link CEO/chủ tịch cho câu lương/tiền dư chỉ chứng minh cùng thao tác so sánh. Nó chưa cho thấy hai câu có sức kéo tương đương.
3. **Mở và nối thiếu thông tin mới.** Một số câu nối chỉ diễn lại câu mở, hoặc đã trả hết phép tính mà không còn câu hỏi có ý nghĩa cho phần sau.
4. **Quá nhiều giọng khuyên bảo và khái quát.** Câu nhắc nhìn ba con số hoặc hỏi mình có tiêu hoang không có thể đúng mục tiêu giáo dục nhưng chưa có chi tiết đáng chú ý của bài cụ thể.
5. **Coi hook là câu chữ rời hình.** Hình mở được bổ sung sau khi đã chọn câu; chưa thử trường hợp hình tự tạo câu hỏi còn lời làm nhiệm vụ khác.
6. **Đa dạng kênh chưa thành đa dạng trải nghiệm.** 10 nguồn/nhãn vẫn có thể tạo 10 câu cùng nhịp. Chỉ tiêu số kênh là biện pháp chống lặp, không phải thước đo hay.

## Thay đổi quy trình viết

Đọc [quy trình tạo lựa chọn](hook-options.md). Trước khi viết câu, xác định: chuyện/đồ vật/hành động cụ thể, kết quả người xem sẽ nhận và chi tiết có thể xuất hiện ở khung đầu. Từ ca đã kiểm, nêu chính xác thông tin nào được cho trước, thông tin nào còn thiếu và lúc nào được trả. Ngoài ngách cũng dùng được khi chuyển được quan hệ ấy sang bài mới; không chỉ thay danh từ.

Các ca ngoài ngách mới có `hookStudy`: lớp lời/hình/chữ, động tác gây chú ý, câu hỏi còn mở, nhịp nối, mốc trả và bản mô tả hai câu. Đây là diễn giải cấu trúc, không phải kịch bản mẫu do AI viết để học lại. Chỉ trích ASR ngắn có nhãn phạm vi, không đăng toàn transcript.

Trước khi giao, đọc thành lời, thử bỏ tên chủ đề: nếu câu còn dùng được gần như nguyên cho vô số đề tài, cần thêm chi tiết của chính bài. Kiểm nhịp nối có thông tin mới và payoff có thật. Không tự chấm “viral”, không hứa cải thiện retention và không dùng kiểm kỹ thuật thay phản hồi của người dùng.

Quan sát đợt ngoài ngách: cực quang cho phần thưởng ở khung đầu; hai ca Thủng Long chủ yếu là hình thể/biểu diễn, không có đáp án tự sự bị giấu. Skill cần chọn giữa câu hỏi còn thiếu và trải nghiệm hình đang tiếp tục; không ép mọi ca vào mô hình tò mò rồi hé lộ.
