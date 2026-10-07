class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hash1 = [0] * 26
        for i in s1:
            hash1[ord(i) - ord("a")] += 1
        l = 0
        hashMap = [0] * 26
        for r in range(len(s2)):
            hashMap[ord(s2[r]) - ord("a")] += 1
            if (r-l+1) > len(s1):
                hashMap[ord(s2[l]) - ord("a")] -= 1
                l += 1
            if tuple(hash1) == tuple(hashMap):
                return True
        return False


        # for i in range(len(s2)):
        #     hashMap = [0]*26
        #     hashMap[ord(s2[i])-ord("a")] += 1
        #     for j in range(i+1, len(s2)):
        #         hashMap[ord(s2[j]) - ord("a")] += 1

        #         if tuple(hash1) == tuple(hashMap):
        #             return True
        # return False

                


        