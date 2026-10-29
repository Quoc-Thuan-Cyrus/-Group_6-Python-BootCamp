# Study Planner CLI

Công cụ dòng lệnh (CLI) hỗ trợ sinh viên lập kế hoạch học tập tự động từ danh sách công việc trong file CSV dựa trên mức độ quan trọng, thời lượng cần thiết và hạn chót (deadline).

## Cấu trúc Module

Gói `shared.study_planner` hoạt động dựa trên các hợp đồng dữ liệu (`Task`, `Block`) trong `shared/contract.py` và đi qua chuỗi xử lý 4 bước (`parse_csv` → `prioritise` → `allocate` → `render`):

* `parse.py`: Cung cấp hàm `parse_csv(path) -> list[Task]` để đọc và kiểm tra tính hợp lệ của dữ liệu từ file CSV.
* `prioritise.py`: Cung cấp hàm `prioritise(tasks, today) -> list[Task]` để sắp xếp công việc theo độ ưu tiên (`importance / days_left`).
* `allocate.py`: Cung cấp hàm `allocate(tasks, hours) -> list[Block]` để phân bổ số giờ học khả dụng theo thuật toán tham lam (greedy).
* `render.py`: Cung cấp hàm `render(blocks) -> str` để định dạng danh sách các phiên học thành văn bản hiển thị trên terminal.
* `__main__.py`: Điểm khởi chạy giao diện dòng lệnh (CLI), kết nối toàn bộ luồng xử lý và bắt các ngoại lệ đầu vào.

## Định dạng file CSV đầu vào

File CSV đầu vào cần có dòng tiêu đề (header) gồm 4 cột `title,importance,effort_h,deadline`:
* `title`: Tên môn học hoặc công việc (chuỗi ký tự).
* `importance`: Mức độ quan trọng từ `1` đến `5` (số nguyên).
* `effort_h`: Số giờ dự kiến cần để hoàn thành (số thực).
* `deadline`: Hạn chót theo định dạng `YYYY-MM-DD`.

Ví dụ (`samples/tasks.csv`):
```csv
title,importance,effort_h,deadline
DS exam,5,6,2026-10-30
Assignment,4,1.5,2026-10-27