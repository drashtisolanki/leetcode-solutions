class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        n = len(nums)

        for num in nums:
            xor ^= num

        for i in range(n + 1):
            xor ^= i

        return xor