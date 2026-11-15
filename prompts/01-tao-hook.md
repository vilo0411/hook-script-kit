# Tạo hook từ corpus đã lưu

Với agent đã cài skill, corpus đi kèm trong `references/corpus/`. Với công cụ chat, đính kèm nhóm hook và các ca bạn chọn từ [kho](../skills/hook-script/references/corpus/index.md) trước khi gửi prompt.

```text
Chủ đề / khán giả / mục tiêu: [điền]
Giọng / thời lượng / điều cần giữ: [điền nếu có]
Corpus: [thư mục đi kèm skill hoặc các case đính kèm]

Đọc corpus có sẵn để đề xuất hook. Không tìm, cào hoặc tải video mới trong
nhiệm vụ này. Đọc mục lục, chọn nhóm và đọc ca phù hợp trước khi viết.
Mỗi hướng ghi Học từ: nhóm, ID/link clip, đoạn quan sát, điều giữ/đổi.

Viết ba hướng mới nếu chưa có yêu cầu khác: câu mở, nhịp nối, điều thân bài
cần giải đáp và lý do phù hợp. Khuyến nghị một hướng. Không sao chép lời hay
chỉ thay danh từ của clip. Chưa viết cả bài nếu tôi chỉ yêu cầu hook.

Giữ đúng giới hạn evidence của ca: ASR/khung trích không đồng nghĩa nghe
âm hoặc xem liên tục; view không chứng minh retention. Các đoạn mở chậm,
hẹn phần hai hoặc trôi chủ đề cần được cân nhắc, không mặc định bắt chước.
Không dùng bài AI chưa duyệt hoặc bị tôi loại làm mẫu giọng/chất lượng.

Nếu thiếu file hoặc không có ca đủ liên quan, nói rõ thiếu gì; không bịa
nguồn và không chuyển sang cào. Bổ sung corpus là nhiệm vụ riêng. Dữ kiện
thực tế của bài mới cần nguồn riêng, ví dụ giả định cần nhãn.
```
