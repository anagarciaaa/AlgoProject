from typing import List, Tuple

def program4B(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """
    Program 4B: Bottom-up dynamic programming (Θ(n²) worst-case)
    """

    # dp[i] = best total value using first i vaults
    dp = [0] * (n + 1)
    parent = [-1] * (n + 1)   # for reconstruction

    for i in range(1, n + 1):
        # Case 1 – skip vault i
        best_val = dp[i - 1]
        best_parent = i - 1

        # Case 2 – take vault i + any valid previous vault j ≤ i − (k + 1)
        for j in range(i - k - 1, -1, -1):      # iterate down to 0 inclusive
            take_val = values[i - 1] + dp[j]
            if take_val > best_val:
                best_val = take_val
                best_parent = j
        dp[i] = best_val
        parent[i] = best_parent

    res = []
    i = n
    while i > 0:
        if dp[i] != dp[i - 1]:
            res.append(i)
            i = parent[i]
        else:
            i -= 1
    res.reverse()
    return dp[n], res


if __name__ == "__main__":
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    total, indices = program4B(n, k, values)
    print(total)
    for idx in indices:
        print(idx)
