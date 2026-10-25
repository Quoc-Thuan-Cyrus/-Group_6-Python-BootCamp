import subprocess  # type: ignore
from pathlib import Path  # type: ignore

def test_study_planner_e2e_cli():
    """Kiểm thử toàn trình luồng CLI của study_planner."""
    sample_csv = "Members/Quoc_Thuan_Cyrus/W2/sample.csv"
    
   
    assert Path(sample_csv).exists(), f"Không tìm thấy file mẫu: {sample_csv}"
    
    
    result = subprocess.run(
        ["python", "-m", "Shared.study_planner", sample_csv, "--hours", "2"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Chương trình lỗi. Chi tiết stderr:\n{result.stderr}"

    assert len(result.stdout.strip()) > 0, "Chương trình không in ra kết quả nào."