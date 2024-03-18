from typing import List


class BinarySearch:

    def search(nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1
        return -1


# Template
# def binary_search(array) -> int:
#     def condition(value) -> bool:
#         pass

#     left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
#     while left < right:
#         mid = left + (right - left) // 2
#         if condition(mid):
#             right = mid
#         else:
#             left = mid + 1
#     return left
