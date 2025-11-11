from typing import List, Tuple
from functools import lru_cache
import sys
sys.setrecursionlimit(100000)

def program4A(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """
    Program 4A: Top-down DP with memoization (Θ(n^2) worst-case)
    """

    @lru_cache(maxsize=None)
    def dp(i: int) -> Tuple[int, Tuple[int]]:
        if i < 0:
            return 0, ()

        # Option 1 – skip vault i
        best_val, best_indices = dp(i - 1)

        # Option 2 – take vault i and check all valid previous vaults
        for j in range(i - (k + 1), -1, -1):
            take_val, take_indices = dp(j)
            take_val += values[i]
            take_indices = take_indices + (i,)
            if take_val > best_val:
                best_val, best_indices = take_val, take_indices

        return best_val, best_indices

    total, chosen = dp(n - 1)
    return total, [i + 1 for i in chosen]


if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    m, indices = program4A(n, k, values)

    print(m)
    for i in indices:
        print(i)

