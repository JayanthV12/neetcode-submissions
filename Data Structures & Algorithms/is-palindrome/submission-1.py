class Solution:
    def isPalindrome(self, s: str) -> bool:
        # string = ""
        # reverse_string = ""

        # for i in range(len(s)):
        #     if s[i].isalnum():
        #         string += s[i].lower()
        #         reverse_string = s[i].lower() + reverse_string
        # print(string, reverse_string)
        # return string == reverse_string
        left = 0
        right = len(s) - 1
        while left <= right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True



        