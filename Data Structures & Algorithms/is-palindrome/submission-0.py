class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        reverse_string = ""

        for i in range(len(s)):
            if s[i].isalnum():
                string += s[i].lower()
                reverse_string = s[i].lower() + reverse_string
        print(string, reverse_string)
        return string == reverse_string



        