"""
LeetCode 33 - Search in Rotated Sorted Array
Difficulty: Medium
Topic: Arrays, Binary Search
"""

class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[right] >= target and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

"""
Brute Force Version
"""
class Solution(object):
    def search(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
