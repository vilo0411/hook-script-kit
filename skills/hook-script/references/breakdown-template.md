# Mẫu ghi phân tích clip

Đây là biểu mẫu trống, không phải một ca đã được phân tích. Thay nội dung trong ngoặc vuông bằng dữ liệu thực; chưa biết thì ghi chưa có.

## Nguồn và trạng thái

- ID / chủ đề: [điền]
- URL clip gốc / tác giả: [điền]
- Ngày quan sát / thời lượng kiểm được: [điền]
- Lý do chọn / mức tương đồng với brief: [điền]
- Lượt xem/tương tác / nguồn / thời điểm đo: [điền hoặc chưa có]
- So sánh trong kênh để gọi là nổi bật: [bằng chứng hoặc chưa có]
- Đã kiểm: [hình, âm, khung chọn lọc, transcript, bài thứ cấp; ghi rõ phạm vi]
- Chưa kiểm được: [điền]
- Trạng thái: [ứng viên / đã phân tích / được người dùng chọn làm nguồn học / bị loại]
- Bằng chứng người dùng chọn/loại nếu có: [điền, không tự đánh dấu]

## Bằng chứng theo diễn biến

| Mốc thật hoặc vị trí đoạn | Quan sát lời/hình/âm, trích ngắn hoặc diễn giải | Vai trò | Suy luận biên tập | Giới hạn |
|---|---|---|---|---|
| [điền] | [điền] | [điền] | [điền] | [điền] |

Không đăng toàn transcript/ảnh khi chưa có quyền chia sẻ. Trích ngắn cần thiết hoặc diễn giải bằng lời riêng, giữ đường dẫn gốc.

## Cơ chế rút ra

- Mở tạo kỳ vọng gì: [quan sát liên quan]
- Nhịp giữ câu chuyện tiến lên: [quan sát liên quan]
- Vị trí và cách giải đáp: [quan sát liên quan]
- Cách kết / nhịp cảm xúc: [quan sát liên quan]
- Điều có thể học và điều không phù hợp brief: [điền]
- Điều chỉ là giả thuyết, cần kiểm thêm: [điền]

## Chuyển thể sang bài mới

- Brief mới: [điền]
- Học từ clip/đoạn: [ID + vị trí]
- Giữ cơ chế nào / đổi gì về tình huống và lời: [điền]
- Hook / nhịp nối / phần giải đáp mới: [chỉ điền khi được yêu cầu viết]
- Trạng thái bài mới: [nháp / đã được duyệt cho tác vụ / được duyệt riêng làm mẫu giọng]

Được duyệt cho một tác vụ không tự trở thành mẫu giọng. Bản phân tích và bản sáng tác phải giữ riêng về nguồn và trạng thái.

## Phân tích sâu và sơ đồ diễn biến

Khi thêm vào corpus, ghi `detail` trong analyses.json: `promise`, `centralQuestion`, `emotionalArc` (mốc, cảm xúc giả thuyết, bằng chứng, diễn giải), `informationDesign` (mốc, động tác viết, lý do), `strengths`/`weaknesses` (nhận định + bằng chứng), `shareabilityHypotheses`, `adaptationRules` và `mindmapBranches` (nhãn + các chi tiết con). Mỗi nhánh phải của chính clip và có mốc khi biết; không dùng một sơ đồ lý thuyết chung làm bằng chứng cho tất cả ca.

Sơ đồ hiện sinh từ `beats` dưới dạng `flowchart TD` một cột theo thời gian, chữ 18px và rộng khoảng 400px. `mindmapBranches` giữ ghi chú phân loại và tương thích dữ liệu cũ, không dùng làm bố cục tỏa nhánh. Mỗi ca cần `deliveryStyle` mô tả hình đã xem; ghi hợp tác thương mại và tự quảng bá riêng nếu có bằng chứng.
