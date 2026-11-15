# Bảo trì: thu thập và phân tích clip tham khảo

Tài liệu dành cho tác vụ bổ sung kho được yêu cầu riêng. Skill viết mặc định chỉ đọc corpus có sẵn, không chạy quy trình này.

## Lấy đầu vào thật

Với URL, mở trang/clip bằng công cụ trình duyệt hoặc tải bản công khai bằng công cụ sẵn có khi phục vụ yêu cầu phân tích. Kiểm hình mở, diễn biến và phần kết; lấy lời hoặc phụ đề và đối chiếu với âm nếu nghe được. Có file video thì xem hình và nghe âm bằng khả năng môi trường đang có. Không cần cài một dịch vụ hay gọi API trả phí để dùng skill.

Không có công cụ đọc video thì dùng transcript/phụ đề có sẵn, ghi đúng phạm vi. Không có transcript nhưng có bài breakdown thì đó là nguồn thứ cấp để chọn ứng viên và đặt giả thuyết. Không có nguồn đọc được thì báo thiếu đầu vào; không tạo một clip, transcript hay bảng thời gian giả.

Không vượt đăng nhập/chặn truy cập. Một nguồn lỗi thì thử nguồn công khai phù hợp khác trong khả năng hiện có. Không nhận đã nghe vì chỉ trích được WAV; không nhận đã xem cả chuyển động vì chỉ có vài ảnh tĩnh.

## Ghi phạm vi bằng chứng

| Dữ liệu có | Được nhận xét | Chưa được kết luận |
|---|---|---|
| Hình + âm đã kiểm | Lời, hình và các nhịp thực quan sát | Nguyên nhân viral nếu thiếu dữ liệu kiểm nghiệm |
| Khung hình chọn lọc | Bố cục tại các khung đó | Toàn bộ chuyển động hoặc nhịp cắt giữa các khung |
| Transcript/phụ đề | Cấu trúc lời và phần diễn biến có trong văn bản | Hình, diễn xuất, âm, thời điểm khi thiếu timestamp |
| Bài phân tích thứ cấp | Những gì bài đó nhận định, với dẫn nguồn | Clip gốc đã được mình kiểm chứng |
| Metadata | Chỉ số, ngày quan sát và nguồn đọc được | Retention từ lượt xem hoặc lượt thích |

## Mổ xẻ toàn câu chuyện

1. **Mở:** người xem thấy/nghe gì đầu tiên; vấn đề, kỳ vọng hay tình huống nào xuất hiện?
2. **Nối:** sau mở có thông tin mới gì; tại sao câu chuyện còn cần được giải quyết?
3. **Diễn biến:** hành động, trở ngại, bằng chứng, thay đổi cảm xúc hoặc lựa chọn nào đẩy chuyện đi?
4. **Giải thích:** khái niệm xuất hiện trước hay sau ví dụ; lời và hình phân chia nhiệm vụ thế nào?
5. **Kết:** điều gợi ở đầu được trả ở đâu; kết có đổi cách hiểu hoặc quay lại chi tiết đầu không?

Dùng bảng `Mốc/vị trí | Quan sát | Vai trò | Suy luận | Cách chuyển thể`. Nhận định như “đoạn này có thể tạo chờ đợi” là giả thuyết biên tập, không phải số đo retention. Không ép điểm giữ chân tại các mốc 7/14/21 giây nếu clip không có.

## So sánh để học

So các clip cùng loại: cửa vào, tốc độ cung cấp thông tin, chỗ căng/thả và cách trả lời. Ghi khác biệt, không gộp mọi clip vào một công thức. Clip không nổi bật hoặc có nhịp yếu cũng có ích làm đối chứng nếu dữ liệu cho phép; không bịa trung vị hoặc kết quả A/B.

Khi dùng vào bài mới, chỉ chuyển cơ chế phục vụ đúng khán giả/giọng. Một đoạn giật gân có nhiều view không tự trở thành lựa chọn phù hợp bài giáo dục tài chính.

## Nghiên cứu phần mở có thể kiểm lại

Với ca mới, ghi `hookStudy`: cửa sổ phần mở thực tế, ba lớp lời/hình/chữ, động tác gây chú ý, giả thuyết lý do dừng, câu hỏi còn mở, thông tin giữ lại, nhịp nối và mốc trả. Tóm lược quan hệ giữa các bước bằng **hai câu cấu trúc**, không tự tạo một hook tài chính rồi nhập làm mẫu học. Ghi riêng điều chuyển được và điều phụ thuộc ngách/người nổi tiếng/nhạc/diễn xuất/sản phẩm.

Khung 0/1/2/3/5 giây chỉ đủ nhận xét những gì quan sát tại mốc ấy. ASR gộp câu dài không xác định được từng từ ở giây thứ ba. Clip nhạc/diễn không lời vẫn có thể có hook hình; bỏ nguyên văn ASR bị ảo, ghi nhịp theo khung và giới hạn. Các mốc 7/14/21 trong repo tham khảo là gợi ý đọc diễn biến, không phải mốc bắt buộc.
