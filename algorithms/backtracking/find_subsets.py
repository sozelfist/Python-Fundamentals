from typing import List


def subsets(nums: List[int], subset: List[int], index: int) -> List[List[int]]:
    if index == len(nums):
        return [subset]
    else:
        with_num = subset + [nums[index]]
        without_num = subset
        return subsets(nums, with_num, index + 1) + subsets(nums, without_num, index + 1)


def find_subsets(nums: List[int]) -> List[List[int]]:
    return subsets(nums, [], 0)


if __name__ == '__main__':
    print(find_subsets([1, 2, 3]))
    # Result: [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
