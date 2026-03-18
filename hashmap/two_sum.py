# Problem: Two Sum
# Topic: HashMap
# Approach:
# Use a hash map to store numbers we have seen.
# For each number, check whether (target - num) exists in the map.
# If it exists, return the indices.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    history = {}

    for i, num in enumerate(nums):
        need = target - num

        if need in history:
            return [history[need], i]

        history[num] = i

    return []


if __name__ == "__main__":
    # Test case 1
    print(twoSum([2, 7, 11, 15], 13))  # [0, 2]

    # Test case 2
    print(twoSum([3, 2, 1], 3))  # [1, 2]
