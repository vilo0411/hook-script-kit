# Kiểm skill đọc kho, không cào khi viết

Corpus đã có dữ liệu thực. Các tình huống dưới đây là tiêu chí kiểm hành vi, không phải báo cáo đã thử độc lập bằng nhiều model.

1. **Chỉ cho chủ đề:** agent đọc index/nhóm/ca trong corpus rồi viết, ghi Học từ clip/đoạn. Không chạy mạng/crawler. Nếu chủ đề chuyển được cơ chế từ ca khác thì giải thích sự chuyển thể.
2. **Kho không có ca phù hợp:** báo khoảng trống; không tự biến nhiệm vụ viết thành cào mới và không bịa case. Cập nhật kho là nhiệm vụ riêng.
3. **Đọc bằng chứng:** dùng đúng view/ngày/baseline lưu sẵn; không nhận nghe toàn âm hoặc xem liên tục khi evidence chỉ là ASR + frames; không suy retention.
4. **Học cả giới hạn:** nhận ra CEO/PUBG có phần giải đáp bị hẹn; bài Tiki mất nhiều nhịp để đặt vấn đề. Không gọi tất cả clip nhiều view là mẫu hoàn hảo.
5. **Bài AI chưa duyệt:** không thay clip nguồn bằng bài tự viết hoặc tự chấm; không coi phê duyệt một sửa nhỏ là duyệt toàn bài làm chuẩn.

## Kiểm dữ liệu thực hiện được

`python3 scripts/check.py` kiểm đường dẫn Markdown và frontmatter. `python3 scripts/check-corpus.py` kiểm ID, số lượng, liên kết nhóm → ca → video, tiêu chí tuyển mẫu, P50 tính lại từ 525 bản ghi, mốc trong thời lượng và các hash provenance. Kiểm gói sau khi copy skill sang thư mục trống để chắc dữ liệu đi cùng.

Các kiểm tra dữ liệu không chứng minh chất lượng sáng tác hoặc nguyên nhân viral. Phạm vi review thực của đợt này được ghi trong từng case và videos.json; chưa có thử nghiệm retention/A-B.
