class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 0:
            return 0
        nums.sort()
        result = 1
        count = 1
        prev = nums[0]
        for i in range(1, n):
            curr = nums[i]
            diff = curr - prev
            if diff == 0:
                continue
            if diff == 1:
                count += 1
            prev = curr
            result = max(count, result)
            if diff > 1:
                count = 1
            

        return result
        