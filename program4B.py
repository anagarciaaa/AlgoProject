from typing import List, Tuple

def program4B(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """
    Program 4B: Bottom-up dynamic programming (Θ(n²) worst-case)
    """

    dp = [0] * (n + 1)
    parent = [-1] * (n + 1)

    for i in range(1, n + 1):
        # Option 1: skip vault i
        dp[i] = dp[i - 1]
        parent[i] = i - 1

        # Option 2: take vault i and try all valid previous choices
        for j in range(0, max(0, i - k - 1) + 1):  # include i-(k + 1)
            take_val = values[i - 1] + dp[j]
            if take_val > dp[i]:
                dp[i] = take_val
                parent[i] = j

    # Reconstruct indices of chosen vaults
    res = []
    i = n
    while i > 0:
        # If taking i improved dp[i] relative to dp[i-1], vault i was chosen
        if dp[i] != dp[i - 1]:
            res.append(i)
            i = parent[i]
        else:
            i -= 1

    res.reverse()
    return dp[n], res


if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    m, indices = program4B(n, k, values)

    print(m)
    for i in indices:
        print(i)
