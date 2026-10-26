def sieve_of_eratosthenes(n: int) -> list[int]:
    """
    Sàng Eratosthenes tìm các số nguyên tố nhỏ hơn hoặc bằng n.
    
    Khác biệt so với C++:
    - Tạo mảng boolean `[True] * (n + 1)` nhanh hơn khởi tạo `std::vector<bool>`.
    """
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
    return [p for p in range(2, n + 1) if is_prime[p]]