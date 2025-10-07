from typing import List, Tuple


def program1(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """
    Solution to Program 1
    
    Parameters:
    n (int): number of vaults
    k (int): no two chosen vaults are within k positions of each other
    values (List[int]): the values of the vaults

    Returns:
    int:  maximal total value
    List[int]: the indices of the chosen vaults(1-indexed)
    """
    ############################
    #pick from the rightmost vault, then skip k to the left, repeat.
    picks = []
    i = n - 1 #starts at the rightmost index (but based 0 so minus 1)
    while i >= 0:
        picks.append(i)
        i -= (k+1)
    #then convert to increasing order and based 1 for output
    picks.reverse()
    total_value = sum(values[p] for p in picks)
    return total_value, [p+1 for p in picks]


if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    m, indices = program1(n, k, values)

    print(m)
    for i in indices:
        print(i)