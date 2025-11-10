from typing import List, Tuple

def program3(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """
    Program 3: Naive recursive solution (Θ(2^n))
    """
    def dfs(i: int) -> Tuple[int, Tuple[int]]:
        if i >= n:
            return 0, ()
        
        # Option 1: skip
        skip_val, skip_indices = dfs(i + 1)

        # Option 2: take
        take_val, take_indices = dfs(i + k + 1)
        take_val += values[i]
        take_indices = (i,) + take_indices

        if take_val > skip_val:
            return take_val, take_indices
        else:
            return skip_val, skip_indices

    best_val, best_indices = dfs(0)
    return best_val, [i + 1 for i in best_indices]


if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    m, indices = program3(n, k, values)

    print(m)
    for i in indices:
        print(i)

