# Kết quả kiểm các đợt cập nhật

Ngày 2026-11-15. Phân biệt kiểm gói dữ liệu, kiểm tuân thủ skill và đánh giá chất lượng của người dùng.

## Đợt ngoài ngách sau bộ hook bị loại

- Dữ liệu: 3.149 bản ghi, 22 kênh, 56 ca, 35 nhóm. 16 ca ngoài ngách có `hookStudy`, mỗi ca đủ cửa sổ thực tế, lời/hình/chữ, nhịp nối, mốc trả, hai câu tóm cấu trúc và giới hạn chuyển ngách.
- Bốn ca được gắn chỉ học hình/chữ; không trích ASR ảo/nhạc. Hai segment mở khác được bỏ/thu ngắn do sai đơn vị tiền và tên người/sự kiện. Không nhận nghe toàn âm/xem liên tục.
- `check.py`, `check-corpus.py` và skill validator qua. P50/tiêu chí tuyển mẫu/timestamp/hash vẫn tính từ dữ liệu lưu, không gọi mạng.
- Render 56/56 sơ đồ thành công bằng Mermaid CLI 12.2.0; xem ảnh mẫu đám cưới mới. Renderer chạy lại không đổi dữ liệu.
- Hai gói cài riêng `.agents/skills/` và `.claude/skills/` đủ 67 Markdown cùng corpus, kiểm tại chỗ thành công.
- Bản sao tạm có payoff ngoài thời lượng, thiếu lớp hình hoặc xóa nghiên cứu phần mở bắt buộc đều bị từ chối. Kiểm sai loại sơ đồ/mốc quan sát giả từ đợt trước vẫn qua.
- Workspace `npm test`: 229/229 qua; skill sync báo 0 adapter cũ.
- Chưa có benchmark sáng tác mới hoặc phê duyệt chất lượng mới từ người dùng. Bộ 10 câu trước được ghi là bị loại; các kiểm trên không chứng minh hook đã hay hoặc cải thiện retention.

## Đợt đa dạng hóa và sơ đồ dọc

- 1.949 bản ghi, 14 kênh, 40 ca, 26 nhóm hook và 40 sơ đồ dọc. Thêm đúng 2 ca mỗi kênh mới; kênh có nhiều ca nhất chiếm 15%.
- Mermaid CLI 12.2.0 render thành công 40/40 sơ đồ. Chiều rộng tối đa khoảng 408px; đã xem ảnh sơ đồ phỏng vấn mới và mẫu cũ để kiểm khả năng đọc.
- Kiểm liên kết, baseline tính lại, điều kiện tuyển mẫu, timestamp, hash, cách thể hiện; quan sát hình của 16 ca mới phải khớp mốc khung đã trích.
- Renderer chạy lại không đổi kết quả. Hai bản cài riêng trong cây `.agents/skills/` và `.claude/skills/` đều đủ 49 file Markdown và corpus, kiểm không gọi mạng.
- Bản sao tạm bị sửa sai loại biểu đồ hoặc thêm mốc quan sát không tồn tại đều bị trình kiểm từ chối.
- Workspace chạy `npm test`: 229/229 test qua; đồng bộ skill kiểm 0 adapter cũ.
- Quy tắc chọn nguồn đã bổ sung mục tiêu ≥5 kênh, ≥3 cách thể hiện, ≤2 option/kênh cho 10 hook khi kho đủ phù hợp. Chưa chạy benchmark sáng tác mới để kết luận chất lượng câu hook.

## Kết quả đợt trước (giữ để truy vết)

## Dữ liệu và mindmap

- Corpus: 749 bản ghi sáu kênh, 24 ca phân tích sâu, 19 nhóm hook, 24 mindmap.
- Đã kiểm liên kết, P50 tính lại, điều kiện tuyển mẫu, mốc trong thời lượng, trường phân tích sâu và hash provenance.
- Render toàn bộ 24 sơ đồ bằng Mermaid CLI 12.2.0: 24 thành công. Đã xem ảnh render mẫu để kiểm khả năng đọc.
- Chạy renderer lại từ JSON cho kết quả giống nhau. Bản Mermaid inline khớp file `.mmd`.
- Sao chép skill sang hai cây thư mục trống `.agents/skills/` và `.claude/skills/`: 32 file Markdown cùng corpus đủ tham chiếu, không gọi mạng.
- Thử làm lệch nội dung `.mmd` và đặt nhịp cảm xúc ngoài thời lượng trong bản sao tạm: trình kiểm đều báo lỗi.

## Lượt thử tạo nhiều hook

Một agent kiểm riêng nhận yêu cầu: tạo hook cho video lạm phát 60 giây, người mới đi làm, gần gũi, muốn nhiều lựa chọn, không CPI thực tế. Chỉ đọc skill và corpus cục bộ.

Kết quả có đúng 10 ID, tham chiếu 9 nhóm nguồn và chọn 3 ID từ bảng để phát triển nhịp nối, hình mở, phần phải giải đáp và điều giữ/đổi. Không cào, không gọi mạng và không dùng số CPI thực tế. Hai option dùng cùng nhóm để giải quyết hai câu hỏi khác, được nói rõ không phải hai cơ chế nguồn khác nhau.

Đây là kiểm cách skill trả kết quả; chưa phải người dùng duyệt câu hook đã hay, benchmark nhiều model hay kiểm chứng retention. Nội dung sáng tác của lượt thử được giữ ngoài corpus và không dùng làm mẫu giọng.

## Phạm vi chưa kiểm

Bằng chứng phân tích clip vẫn là các khung trích đã xem và ASR có mốc, chưa nghe toàn âm hoặc xem liên tục. Nhịp cảm xúc và khả năng chia sẻ là giả thuyết biên tập, không phải số liệu người xem. Mọi claim kinh tế trong nguồn cần fact-check riêng trước khi dùng làm dữ kiện cho bài mới.
