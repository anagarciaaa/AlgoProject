from typing import List, Tuple

def program5(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """
    Program 5: Optimized bottom-up DP (Θ(n) time and space)
    """

    if n == 0:
        return 0, []

    dp = [0] * (n + 1)
    parent = [("skip", i - 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        take_prev = max(0, i - (k + 1))
        take_val = values[i - 1] + dp[take_prev]
        skip_val = dp[i - 1]

        if take_val >= skip_val:
            dp[i] = take_val
            parent[i] = ("take", take_prev)
        else:
            dp[i] = skip_val
            parent[i] = ("skip", i - 1)

    chosen = []
    i = n
    while i > 0:
        action, prev_i = parent[i]
        if action == "take":
            chosen.append(i)
        i = prev_i

    chosen.reverse()
    return dp[n], chosen


if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    m, indices = program5(n, k, values)

    print(m)
    for i in indices:
        print(i)

