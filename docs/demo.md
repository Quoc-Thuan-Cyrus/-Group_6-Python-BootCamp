# Study Planner CLI — Short Demo

Tài liệu này minh họa cách chạy công cụ lập kế hoạch học tập `study_planner` từ dòng lệnh và cách chương trình xử lý các tình huống lỗi đầu vào.

## 1. Dữ liệu mẫu (`samples/tasks.csv`)

Giả sử chúng ta có file `samples/tasks.csv` với 2 công việc cần hoàn thành:

```csv
title,importance,effort_h,deadline
DS exam,5,6,2026-10-30
Assignment,4,1.5,2026-10-27
```

## 2. Chạy chương trình với dữ liệu hợp lệ

Khi sinh viên có **2 giờ** học trong tối nay (`--hours 2`), chạy lệnh sau trên terminal:

```console
$ python -m shared.study_planner samples/tasks.csv --hours 2
Tonight (2.0 h):
  1. Assignment .... 1.5 h
  2. DS exam ....... 0.5 h
```

**Diễn giải kết quả:**
1. **`parse_csv`** đọc 2 công việc từ file `samples/tasks.csv`.
2. **`prioritise`** tính độ ưu tiên (`importance / days_left`), xếp `Assignment` lên đầu vì hạn chót gần hơn, sau đó đến `DS exam`.
3. **`allocate`** phân bổ 1.5 giờ cho `Assignment` (hoàn thành trọn vẹn) và dành 0.5 giờ còn lại cho `DS exam`.
4. **`render`** định dạng danh sách các khối giờ học (`Block`) và in ra màn hình.

## 3. Demo các trường hợp xử lý lỗi (Error Handling)

### 3.1. File không tồn tại (Missing file)
Khi truyền vào đường dẫn file không có thật:
```console
$ python -m shared.study_planner samples/missing.csv --hours 2
Error: File not found: samples/missing.csv
```

### 3.2. File rỗng (Empty file)
Khi file CSV không có dữ liệu công việc nào:
```console
$ python -m shared.study_planner samples/empty.csv --hours 2
Error: The task file is empty.
```

### 3.3. Kế hoạch không khả thi (`InfeasiblePlan`)
Khi quỹ thời gian nhập vào không hợp lệ hoặc không đủ để lập kế hoạch khả thi:
```console
$ python -m shared.study_planner samples/tasks.csv --hours 0
InfeasiblePlan: Need 7.5 hours, but only 0.0 hours available.
```