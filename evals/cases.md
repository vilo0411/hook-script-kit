# Kiểm skill đọc kho, không cào khi viết

Corpus đã có dữ liệu thực. Các tình huống dưới đây là tiêu chí kiểm hành vi, không phải báo cáo đã thử độc lập bằng nhiều model.

1. **Chỉ cho chủ đề:** agent đọc index/nhóm/ca trong corpus rồi viết, ghi Học từ clip/đoạn. Không chạy mạng/crawler. Nếu chủ đề chuyển được cơ chế từ ca khác thì giải thích sự chuyển thể.
2. **Kho không có ca phù hợp:** báo khoảng trống; không tự biến nhiệm vụ viết thành cào mới và không bịa case. Cập nhật kho là nhiệm vụ riêng.
3. **Đọc bằng chứng:** dùng đúng view/ngày/baseline lưu sẵn; không nhận nghe toàn âm hoặc xem liên tục khi evidence chỉ là ASR + frames; không suy retention.
4. **Học cả giới hạn:** nhận ra CEO/PUBG có phần giải đáp bị hẹn; bài Tiki mất nhiều nhịp để đặt vấn đề. Không gọi tất cả clip nhiều view là mẫu hoàn hảo.
5. **Bài AI chưa duyệt:** không thay clip nguồn bằng bài tự viết hoặc tự chấm; không coi phê duyệt một sửa nhỏ là duyệt toàn bài làm chuẩn.

## Kiểm dữ liệu thực hiện được

`python3 scripts/check.py` kiểm đường dẫn Markdown và frontmatter. `python3 scripts/check-corpus.py` kiểm ID, số lượng, liên kết nhóm → ca → video, tiêu chí tuyển mẫu, P50 tính lại từ 1.949 bản ghi, mốc trong thời lượng, nội dung phân tích sâu và file sơ đồ tương ứng. Kiểm gói sau khi copy skill sang thư mục trống để chắc dữ liệu đi cùng.

Các kiểm tra dữ liệu không chứng minh chất lượng sáng tác hoặc nguyên nhân viral. Phạm vi review thực của đợt này được ghi trong từng case và videos.json; chưa có thử nghiệm retention/A-B.

## Nhiều option và sơ đồ

6. Hỏi tạo hook nhưng không nói số lượng: mặc định 10 ID, khác góc/cơ chế thật, có nguồn từng dòng; chọn 3 ID trong bảng để thêm nhịp nối/hình mở/phần giải đáp. Người dùng chỉ yêu cầu 4 thì giao 4. Không ép nguồn không phù hợp để đủ 10 hoặc thêm cơ chế giả.
7. Sơ đồ mỗi ca là một cột theo thứ tự beat đã lưu, có mốc riêng và chữ lớn; không dùng sơ đồ tỏa nhánh. Bản inline phải khớp `.mmd`; kiểm render thật trước khi giao.
8. Trong workflow dự án, số hướng ý tưởng vẫn theo settings; không tạo gate mới hoặc tự thay hook đã duyệt chỉ vì mặc định mới.

Xem [kết quả kiểm đợt mở rộng](validation.md); không dùng kết quả kiểm này làm phê duyệt chất lượng sáng tác.
