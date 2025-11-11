from typing import List, Tuple

def program4B(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """
    Program 4B: Bottom-up dynamic programming (Θ(n^2) worst-case)
    """

    dp = [0] * (n + 1)
    parent = [-1] * (n + 1)

    for i in range(1, n + 1):
        # Option 1: skip vault i
        best_val = dp[i - 1]
        best_parent = i - 1

        # Option 2: take vault i and try all valid previous choices
        for j in range(max(0, i - k - 1) + 1):
            take_val = values[i - 1] + dp[j]
            if take_val > best_val:
                best_val = take_val
                best_parent = j


        dp[i] = best_val
        parent[i] = best_parent

    # Reconstruct indices
    res = []
    i = n
    while i > 0:
        if parent[i] < i - 1:  # vault i was taken
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

