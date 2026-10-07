class Solution:
    def minWindow(self, s: str, t: str) -> str:

        hashMap = {}
        for i in t:
            if i not in hashMap:
                hashMap[i] = 0
            hashMap[i] += 1

        minString = ""
        minLength = float("inf")
        have = 0
        need = len(hashMap)
        l = 0
        countMap = {}
        for r in range(len(s)):
            c = s[r]
            if c not in countMap:
                countMap[c] = 0
            countMap[c] += 1

            if c in hashMap and countMap[c] == hashMap[c]:
                have += 1
            
            while have == need:
                currentLength = r - l + 1
                if currentLength < minLength:
                    minLength = currentLength
                    minString = s[l: r+1]
                
                countMap[s[l]] -= 1
                if s[l] in hashMap and countMap[s[l]] < hashMap[s[l]]:
                    have -= 1
                l += 1
                
        return minString






        # for i in range(len(s)):
        #     countMap = {}

        #     for j in range(i, len(s)):

        #         if s[j] not in countMap:
        #             countMap[s[j]] = 0
        #         countMap[s[j]] += 1

        #         eachMapped = True

        #         for a, b in hashMap.items():
        #             if a not in countMap or countMap[a] < b:
        #                 eachMapped = False
        #                 break

        #         if eachMapped:
        #             currentLength = j - i + 1

        #             if currentLength < minLength:
        #                 minLength = currentLength
        #                 minString = s[i:j + 1]

        #             break

        # return minString
