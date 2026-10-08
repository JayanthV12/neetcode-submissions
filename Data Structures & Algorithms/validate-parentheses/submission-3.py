class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)%2 != 0:
            return False
        st = []

        for i in s:
            if i == "(" or i == "[" or i == "{":
                st.append(i)
            else:
                el = st.pop() if st else None
                if i == ")" and el != "(":
                    return False
                if i == "}" and el != "{":
                    return False
                if i == "]" and el != "[":
                    return False
            

        return True if len(st) == 0 else False
        