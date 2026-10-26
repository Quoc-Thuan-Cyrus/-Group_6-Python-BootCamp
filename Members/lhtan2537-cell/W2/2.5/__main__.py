import os  # noqa: N999
from importlib import import_module  # type: ignore

_io = import_module(".io_utils", package=__package__)
_err = import_module(".errors", package=__package__)

load_tasks = _io.load_tasks  # type: ignore
InfeasiblePlan = _err.InfeasiblePlan  # type: ignore
check_feasible = _err.check_feasible  # type: ignore

def main() -> None:
    current_dir = os.path.dirname(__file__)
    csv_file = os.path.join(current_dir, "sample_tasks.csv")

    if not os.path.exists(csv_file):
        print(f"Không tìm thấy file: {csv_file}")
        return

    tasks = load_tasks(csv_file)
    print("=" * 50)
    print(f" ĐÃ TẢI THÀNH CÔNG {len(tasks)} TASK TỪ FILE CSV MẪU")
    print("=" * 50)

    for i, t in enumerate(tasks, start=1):
        print(f"{i}. [{t.importance}/5 Sao] {t.title}")
        print(f"   - Thời gian ước tính: {t.effort_h}h")
        print(f"   - Deadline          : {t.deadline}")

    print("-" * 50)
    try:
        check_feasible(tasks, available_h=10.0)
        print("Tình trạng: Quỹ thời gian 10.0h ĐỦ cho các task trên.")
    except InfeasiblePlan as err:
        print(f"Cảnh báo: {err}")
    print("=" * 50)


if __name__ == "__main__":
    main()