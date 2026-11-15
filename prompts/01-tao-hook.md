# Tạo hook từ corpus đã lưu

Với agent đã cài skill, corpus đi kèm trong `references/corpus/`. Với công cụ chat, đính kèm nhóm hook và các ca bạn chọn từ [kho](../skills/hook-script/references/corpus/index.md) trước khi gửi prompt.

```text
Chủ đề / khán giả / mục tiêu: [điền]
Giọng / thời lượng / điều cần giữ: [điền nếu có]
Corpus: [thư mục đi kèm skill hoặc các case đính kèm]

Đọc corpus có sẵn để đề xuất hook. Không tìm, cào hoặc tải video mới trong
nhiệm vụ này. Đọc mục lục, chọn nhóm và đọc ca phù hợp trước khi viết.
Mỗi hướng ghi Học từ: nhóm, ID/link clip, đoạn quan sát, điều giữ/đổi.

Mặc định cho tôi 10 option (nếu tôi yêu cầu số khác thì theo số đó), dạng
bảng ID / hook nguyên văn / góc-cơ chế / nhóm và clip nguồn / hợp khi nào.
Các option phải khác thực sự, ưu tiên ít nhất 6 cơ chế nếu brief và kho cho
phép, không ép nguồn không liên quan để đủ số. Đọc cả sơ đồ diễn biến, diễn biến
và điểm mạnh-yếu của ca. Chọn 3 ID đáng phát triển: thêm nhịp nối nguyên văn,
hình mở gợi ý và điều thân/kết phải giải đáp; dẫn rõ đoạn nguồn và điều đổi.
Khuyến nghị 1 ID, không nhận đã A/B test. Không chép lời hoặc chỉ thay danh
từ. Chưa viết cả bài nếu tôi chỉ yêu cầu hook.

Giữ đúng giới hạn evidence của ca: ASR/khung trích không đồng nghĩa nghe
âm hoặc xem liên tục; view không chứng minh retention. Các đoạn mở chậm,
hẹn phần hai hoặc trôi chủ đề cần được cân nhắc, không mặc định bắt chước.
Không dùng bài AI chưa duyệt hoặc bị tôi loại làm mẫu giọng/chất lượng.

Nếu thiếu file hoặc không có ca đủ liên quan, nói rõ thiếu gì; không bịa
nguồn và không chuyển sang cào. Bổ sung corpus là nhiệm vụ riêng. Dữ kiện
thực tế của bài mới cần nguồn riêng, ví dụ giả định cần nhãn.
```


Đa dạng nguồn: với 10 hook, ưu tiên ≥5 kênh, ≥3 cách thể hiện, ≤2 option/kênh khi có đủ ca phù hợp. Brief và yêu cầu người dùng được ưu tiên; ghi rõ khi kho chưa đủ.
