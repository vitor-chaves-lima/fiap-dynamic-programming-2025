from typing import List

def binary_search(values: List[int], target: int) -> int:
    l = 0
    h = len(values) - 1
    i = 0

    while l <= h:
        m = (h + l) // 2

        if values[m] == target:
            return m

        if values[m] < target:
            l = m + 1
        else:
            h = m - 1

        i += 1
        print(f"Iteration {i} - l={l}, h={h}, m={m}")

    return -1

print(binary_search([1, 2, 5, 4, 5], 3))