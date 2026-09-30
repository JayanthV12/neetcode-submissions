class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for i in nums:
            if i not in hashMap:
                hashMap[i] = 0
            hashMap[i] += 1
        
        groupMap = [[] for i in range(len(nums) + 1)]

        for key, value in hashMap.items():
            groupMap[value].append(key)
        res = []
        for each in range(len(nums), 0, -1):
            for i in groupMap[each]:
                res.append(i)
                if len(res) == k:
                    return res
        return res

        
        
        