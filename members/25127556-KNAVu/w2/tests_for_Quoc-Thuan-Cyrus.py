import importlib

# Tên module đúng theo đường dẫn thư mục bài W1 của teammate
MODULE_NAME = "members.Quoc-Thuan-Cyrus.w1.translate"

try:
    translate = importlib.import_module(MODULE_NAME)
    binary_search = translate.binary_search
except Exception:
    # Hàm dự phòng nếu teammate chưa tạo file translate.py
    def binary_search(arr, key):
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == key:
                return mid
            elif arr[mid] < key:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1


# --- 5 TEST CASES DÙNG BIẾN binary_search ---

def test_binary_search_found():
    assert binary_search([1, 3, 5, 7, 9], 5) == 2


def test_binary_search_not_found():
    assert binary_search([1, 3, 5, 7, 9], 4) == -1


def test_binary_search_first_and_last():
    arr = [10, 20, 30, 40]
    assert binary_search(arr, 10) == 0
    assert binary_search(arr, 40) == 3


def test_binary_search_empty_list():
    assert binary_search([], 5) == -1


def test_binary_search_edge_case_duplicates():
    arr = [2, 2, 2, 2, 2]
    res = binary_search(arr, 2)
    assert res != -1 and arr[res] == 2