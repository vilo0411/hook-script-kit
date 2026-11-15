# Thu thập trước, dùng sau

Cập nhật corpus là công việc của người bảo trì, tách khỏi skill viết. Đợt ngày 2026-11-15 đã hoàn thành lấy dữ liệu thật; đây là mô tả có thể kiểm lại, không phải việc giao cho người dùng tự cào mới có dữ liệu.

## Lượt ban đầu đã thực hiện

1. Lấy danh sách mới bằng `yt-dlp --flat-playlist -J --playlist-end 150` cho bốn kênh `longvasocbc1`, `nqs.kinhte`, `tinhbao.thitruong`, `longkhongphainong`. Thu được lần lượt 75, 150, 150, 150 bản ghi; tổng 525.
2. Lọc ứng viên từ nghiên cứu đã có ASR, ưu tiên kinh tế/tài chính tiếng Việt và bỏ mẫu được đánh dấu tài trợ. Chọn có chủ đích, không phải top của toàn TikTok VN. Tải lại 12 clip bằng `yt-dlp --no-playlist --write-info-json` và lấy số tại request clip.
3. Trích 12 khung/media ở mở đầu, giữa và cuối; xem các khung đó, đọc ASR có timestamp từ cache cùng ID. Đối chiếu thời lượng và giữ hash của media/metadata/contact sheet/ASR. Không tuyên bố đã nghe toàn âm, xem liên tục hoặc byte media mới trùng bản cũ.
4. Viết diễn giải riêng theo mốc, phân tích mở/nối/diễn biến/kết và giới hạn; sau đó nhóm thành 10 cơ chế. Mỗi nhóm dẫn về ít nhất một video và bản phân tích.
5. Xuất metadata chuẩn hóa và phân tích vào [corpus](skills/hook-script/references/corpus/index.md). MP4, toàn ASR và raw info.json được giữ trong bộ nghiên cứu cục bộ của người bảo trì, không đưa vào repo chia sẻ. File public giữ SHA256 để đối chiếu bản nguồn khi có quyền truy cập.

## Đợt mở rộng phân tích và lựa chọn hook

Đã thêm 12 clip và hai kênh `huyen_chungkhoan101` (150 bản ghi), `iftactix` (74 bản ghi), nâng tổng thành **749 bản ghi, 6 kênh, 24 ca**. Bốn snapshot trước giữ nguyên timestamp. Metadata và media của 12 clip bổ sung được tải riêng và có hash/ngày đo trong videos.json.

Toàn bộ 24 ca được đọc ASR và đối chiếu khung để bổ sung phân tích sâu, sơ đồ cảm xúc giả thuyết, cách phân phối thông tin, điểm mạnh/yếu và 24 mindmap. Nhóm hóa thành 19 cửa vào; một số ca mới củng cố nhóm cũ, không cố tách thêm nhãn cho đủ số. Ba ca có tự quảng bá cộng đồng được đánh dấu; chưa đủ xác định tài trợ bên thứ ba. Một ứng viên bị loại vì ASR lặp tiếng Anh không liên quan.

Dữ liệu chuẩn là JSON. Chạy `python3 scripts/render-corpus.py` để sinh case Markdown, Mermaid inline, file `.mmd`, nhóm hook và index. Công cụ chỉ render dữ liệu tại chỗ, không cào. Sơ đồ hiện dùng Mermaid `flowchart TD`, một cột có mốc thời gian; field `mindmapBranches`, thư mục `mindmaps/` và anchor `#mindmap` được giữ để tương thích liên kết cũ. Đã dùng Mermaid CLI 12.2.0 để kiểm render; không cần CLI để skill đọc nguồn hoặc GitHub hiển thị sơ đồ.

Luồng tạo hook dùng mặc định 10 option, chọn 3 ID phát triển; không đổi số hướng/gate trong workflow dự án.

## Đợt đa dạng hóa và đổi sơ đồ

Thêm 8 kênh, mỗi kênh 150 bản ghi và 2 clip: `nguyentrangtkneu`, `sitcomtaichinh`, `thayqueo`, `vtv24news`, `d.trending`, `kienthuckinhte28`, `vietcetera_`, `quocthichkinhte`. Tổng **1.949 bản ghi, 14 kênh, 40 ca**. Kênh có nhiều ca nhất chiếm 15% thay vì 25% trước đợt này. Xem bảng phân bố trong corpus.

16 ca mới được tải media, chạy Whisper cục bộ, đọc ASR và xem khung chọn lọc. Loại ứng viên Tài Chính Cá Nhân 2026 do lượt tải chỉ trả âm thanh; không tính là video đã phân tích. Không đăng toàn transcript hoặc nguồn media. Ca Techcombank có `#hoptaccungtechcombank` được đánh dấu hợp tác, không coi là đánh giá độc lập. Clip 5 tài sản dài hơn 12 phút được ghi rõ; không áp thời gian mở dài ấy làm chuẩn Shorts.

Thay toàn bộ sơ đồ tỏa nhánh bằng sơ đồ dọc theo diễn biến thật, mốc rõ và chữ 18px. Dữ liệu chi tiết về cảm xúc, câu hỏi, điểm mạnh/yếu vẫn ở bảng bên dưới. Với yêu cầu 10 hook, ưu tiên ≥5 kênh, ≥3 cách thể hiện, ≤2 option/kênh khi có đủ mẫu phù hợp; không ép nguồn lạc đề.

## Định nghĩa tuyển mẫu

Tối thiểu 100.000 view và 3× trung vị tập kênh thu thập sau khi bỏ bài dưới 48 giờ. Tất cả 40 ca đạt tiêu chí này. P50 được tính trong tối đa 150 bài lấy được, không phải toàn bộ lịch sử; có clip cũ ngoài cửa sổ baseline. Không suy ra causal uplift hay tốc độ tăng view từ số view tích lũy.

Tiêu chí Việt Nam: lời/kênh tiếng Việt, ngữ cảnh hướng tới khán giả Việt. Chủ đề có thể là kinh tế nước ngoài. Không có vị trí địa lý người xem, retention hoặc watch-time. Corpus gồm clip đăng từ 2024–2026, không chỉ các clip mới nhất.

## Bảo trì lần sau

Chỉ thực hiện khi có yêu cầu cập nhật riêng. Giữ timestamp từng request; không dùng ngày render báo cáo làm ngày crawl. Tách metadata cũ/mới, không đè ngày cũ nếu không lấy lại. Đọc và kiểm nguồn trước khi thêm nhóm hook; thiếu evidence thì chưa đưa vào nhóm dùng cho viết.

Khi cập nhật skill đã cài, thay cả thư mục skill để các ca, metadata và chỉ dẫn cùng phiên bản. Chạy `python3 scripts/check.py` và `python3 scripts/check-corpus.py`. Hai kiểm tra chỉ xác nhận liên kết và tính nhất quán của gói dữ liệu, không chứng minh chất lượng sáng tác.

## Đợt ngoài ngách sau phản hồi loại 10 hook

Đã đọc lại SKILL/database của rediumvex, README và ba breakdown tháng11 của shixinzhang, ghi rõ giá trị lẫn giới hạn tại `references/reference-audit.md`. Không nhập nội dung breakdown CC BY-NC-SA vào corpus MIT. Ghi phản hồi bộ hook là bị loại, không dùng làm nguồn mẫu.

Thêm 8 snapshot x150 bài: `khoailangthang`, `genjadao`, `kienkhongngu_official`, `vatvostudio`, `vietphuongthoa98`, `thunglongfamily`, `halinhofficial`, `quankhonggo`. Mỗi kênh hai ca, tổng 3.149 bản ghi, 22 kênh, 56 ca. Khám phá từ nguồn công khai rồi kiểm handle bằng dữ liệu thật; tài khoản trùng tên hoặc không đạt ngưỡng không tính vào tổng. Hai ứng viên genjadao chỉ có MP3 bị loại khỏi phân tích.

16 ca mới có `hookStudy`: mốc phần mở thực tế, lớp lời/hình/chữ, giả thuyết động tác gây chú ý, thông tin còn thiếu, nhịp nối, mốc trả hoặc giới hạn chưa trả, hai câu tóm cấu trúc, điều chuyển được/không chuyển theo. Một số ca là biểu diễn không có câu hỏi tự sự; không gán open-loop giả. Bốn ca đánh dấu `sampled-visual-only`, bỏ ASR ảo/nhạc khỏi nguyên văn và phân tích lời. Các ca có hợp tác/tài trợ hoặc bán hàng ghi ngữ cảnh riêng; không suy reach organic.

Sửa workflow viết để tìm chi tiết có thể thấy, cảm giác bài có thể tạo, nhịp nối có thông tin mới và payoff trước khi gắn công thức. Đa dạng nguồn chỉ là phương tiện; không dùng số kênh hoặc test kỹ thuật để tuyên bố câu hook mới hay.
