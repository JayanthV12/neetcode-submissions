class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        numSet = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                longest = max(longest, length)
        return longest


            









        # n = len(nums)
        # if n == 0:
        #     return 0
        # nums.sort()
        # result = 1
        # count = 1
        # prev = nums[0]
        # for i in range(1, n):
        #     curr = nums[i]
        #     diff = curr - prev
        #     if diff == 0:
        #         continue
        #     if diff == 1:
        #         count += 1
        #     prev = curr
        #     result = max(count, result)
        #     if diff > 1:
        #         count = 1
            

        # return result
        