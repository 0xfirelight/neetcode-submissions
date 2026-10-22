import re

class Solution:

    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        pattern = re.compile('[A-Za-z0-9]', re.I)

        while i != j and i < len(s) and j >= 0:
            if not re.search(pattern, s[i]):
                i += 1
                continue
                
            if not re.search(pattern, s[j]):
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True
        