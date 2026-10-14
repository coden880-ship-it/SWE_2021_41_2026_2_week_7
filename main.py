from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    # Map each value we've seen to its index
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
