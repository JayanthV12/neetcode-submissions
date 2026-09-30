class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for s in strs:
            countMap = [0] * 26
            for char in s:
                countMap[ord(char) - ord("a")] += 1
            
            keyTuple = tuple(countMap)

            if keyTuple not in hashMap:
                hashMap[keyTuple] = []
            hashMap[keyTuple].append(s)
        return list(hashMap.values())
