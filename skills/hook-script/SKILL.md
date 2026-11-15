---
name: hook-script
description: Viết hoặc sửa hook và kịch bản tiếng Việt từ kho TikTok Việt Nam đã thu thập, phân tích sẵn, mỗi nhóm có clip và bằng chứng. Đọc dữ liệu đi kèm tại chỗ, không cào khi viết; không lấy bài AI chưa duyệt làm mẫu.
---

# Viết từ kho clip đã lưu

Dùng brief, giọng và rule của người dùng. **Skill này đọc kho có sẵn, không chạy crawler, không tự đi tìm hoặc tải clip khi viết.** Thu thập và phân tích bổ sung là tác vụ bảo trì riêng, chỉ làm khi người dùng yêu cầu rõ.

## Chọn nguồn trong kho

1. Đọc [mục lục corpus](references/corpus/index.md) và [nhóm hook có video](references/corpus/patterns.md).
2. Chọn nhóm hợp vấn đề/khán giả/loại bài; đọc mindmap, diễn biến, nhịp cảm xúc giả thuyết và điểm mạnh/yếu trong các ca được dẫn trước khi dùng. Không cần chủ đề mới trùng danh từ với clip: chuyển cơ chế khi mục tiêu phù hợp, giải thích được sự khác biệt.
3. Mỗi hướng ghi `Học từ`: nhóm, ID clip, đoạn quan sát, điều giữ/đổi. Số view, baseline và ngày đo lấy từ [metadata](references/corpus/videos.json), không cập nhật giả hoặc suy retention.
4. Phân biệt quan sát khung hình và ASR với giả thuyết về hiệu quả. Kho hiện chưa được nghe toàn âm/xem liên tục, không nhận đã làm việc đó. Không coi mọi dữ kiện kinh tế trong clip là nguồn kiến thức đã kiểm.

## Viết và sửa

- **Hook:** đọc [cách trình nhiều lựa chọn](references/hook-options.md). Mặc định **10 option** khác góc/cơ chế, có câu hook nguyên văn, nhóm nguồn/clip và lý do hợp brief. Chọn 3 ID trong bảng để phát triển nhịp nối, hình mở và phần cần giải đáp. Số lượng người dùng yêu cầu được ưu tiên; không viết cả bài nếu chỉ được hỏi hook. Không ép nguồn không phù hợp để đủ số.
- **Kịch bản:** giữ hướng đã chọn, phát triển lời/hình và kết trả điều hook đã gợi. Giao bảng thời gian ước tính / lời đọc / hình gợi ý cùng phần truy nguồn cơ chế và dữ kiện.
- **Sửa bài:** đối chiếu đoạn yếu với đoạn có vai trò tương đương trong ca đã lưu rồi giao bản sửa. Không đổi phần người dùng yêu cầu giữ. Sửa chính tả/số đơn thuần không cần chọn ca.

Học cơ chế, không chép câu hoặc chỉ thay danh từ trong transcript. Những đoạn hẹn phần hai, mở chậm hoặc trôi chủ đề trong kho được ghi để cân nhắc, không phải chuẩn bắt chước. Bài AI chưa duyệt/bị loại không làm chuẩn giọng dù tự chấm hay test kỹ thuật đạt.

## Khi kho chưa bao phủ

Nếu không có ca đủ liên quan để chuyển cơ chế, nói rõ khoảng trống. Có thể đề xuất bảo trì kho như việc riêng, không tự chuyển tác vụ viết thành cào. Chỉ sáng tác không có đối chiếu khi người dùng yêu cầu, gắn nhãn bản nháp chưa có nguồn mẫu.

Đọc [quy trình](references/workflow.md) và [review](references/review.md) khi viết toàn bài. Số thực tế của bài mới cần nguồn riêng; giả định cần nhãn. Không bịa trải nghiệm, nguồn, mốc quan sát hoặc số hiệu quả. Kiểm kỹ thuật không thay phê duyệt chất lượng của người dùng.
