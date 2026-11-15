# Đóng góp bằng phân tích có nguồn

Ưu tiên một breakdown clip thật hơn thêm mẫu câu tự sinh. Mỗi đóng góp cần URL gốc, lý do chọn, ngày quan sát, phạm vi thực đã kiểm và bảng diễn biến theo [mẫu](skills/hook-script/references/breakdown-template.md).

Tách quan sát khỏi giả thuyết. Không bịa mốc thời gian, transcript, lượt xem hoặc nguyên nhân viral. Nếu chỉ có transcript, ghi đúng phạm vi; nếu dựa bài thứ cấp, dẫn bài đó thay vì nhận đã xem video.

Bài sáng tác phát triển từ phân tích cần ghi học từ clip/đoạn nào và điều đã đổi. Không đưa nó vào làm chuẩn giọng hoặc chuẩn chất lượng nếu chưa được chủ repo duyệt rõ cho mục đích đó. Bài tự chấm đạt không thay được phản hồi người dùng.

Chỉ đăng phần bạn có quyền chia sẻ; ưu tiên diễn giải ngắn và liên kết nguồn, không đăng nguyên transcript/ảnh/video. Phần tự viết theo MIT; nguồn ngoài giữ giấy phép riêng. Không đưa dữ liệu nội bộ hoặc thông tin khách hàng.

Chạy `python3 scripts/check.py` (Python 3.9+, thư viện chuẩn), kiểm skill sau khi sao chép riêng và rà nguồn/vị trí trước khi gửi. Kiểm kỹ thuật không xác nhận chất lượng sáng tác.

Cập nhật dữ liệu và phân tích trước khi phát hành skill. Thêm metadata/video/case/nhóm vào corpus đi kèm, chạy `python3 scripts/check-corpus.py`. Không thêm thao tác cào vào luồng viết; maintainer cập nhật theo yêu cầu riêng.

Mỗi ca mới cần thêm lời hứa/câu hỏi trung tâm, nhịp cảm xúc như giả thuyết có mốc, phân phối thông tin, điểm mạnh/yếu có bằng chứng và các nhịp diễn biến có mốc riêng của clip. Sửa JSON nguồn rồi chạy `python3 scripts/render-corpus.py`; không sửa tay trang sinh nếu chưa cập nhật JSON. Sơ đồ phải là `flowchart TD` một cột có mốc, khớp bản inline và file `.mmd`; không dùng lại bố cục tỏa nhánh. Ghi cách thể hiện quan sát được và ngữ cảnh hợp tác/quảng bá nếu thấy. Ưu tiên kênh chưa có thay vì thêm nhiều ca cùng nguồn.

Ca ngoài ngách cần ngách và `hookStudy` theo cấu trúc trong [hướng dẫn phân tích](skills/hook-script/references/analysis.md). Có thể chỉ học hình nếu ASR lỗi, nhưng phải gắn phạm vi và không bịa lời/câu hỏi tự sự. Hai câu tóm cấu trúc mô tả nguồn, không phải kịch bản sáng tác đưa vào mẫu học.
