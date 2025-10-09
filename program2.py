from typing import List, Tuple


def program2(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """
    Solution to Program 2
    
    Parameters:
    n (int): number of vaults
    k (int): no two chosen vaults are within k positions of each other
    values (List[int]): the values of the vaults

    Returns:
    int:  maximal total value
    List[int]: the indices of the chosen vaults(1-indexed)
    """
    if n == 0:
        return 0, []

    dp = [0] * (n + 1)
    parent = [("skip", i - 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        take_prev = max(0, i - (k + 1))
        take_val = values[i - 1] + dp[take_prev]
        skip_val = dp[i - 1]

        # Prefer taking when equal (consistent with greedy approach)
        if take_val >= skip_val:
            dp[i] = take_val
            parent[i] = ("take", take_prev)
        else:
            dp[i] = skip_val
            parent[i] = ("skip", i - 1)

    # Reconstruct chosen indices (1-indexed)
    chosen = []
    i = n
    while i > 0:
        action, prev_i = parent[i]
        if action == "take":
            chosen.append(i)  # 1-indexed
        i = prev_i

    chosen.reverse()
    return dp[n], chosen


if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    m, indices = program2(n, k, values)

    print(m)
    for i in indices:
        print(i)
