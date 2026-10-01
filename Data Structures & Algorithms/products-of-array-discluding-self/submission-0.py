class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixProd = [0] * n
        suffixProd = [0] * n 
        prefixProd[0] = suffixProd[n-1] = 1
        for i in range(1, n):
            prefixProd[i] = prefixProd[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suffixProd[i] = suffixProd[i+1] * nums[i+1]
        res = [0] * n
        for i in range(n):
            res[i] = prefixProd[i] * suffixProd[i]
        return res

        

        


        