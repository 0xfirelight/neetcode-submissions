class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c_s, c_t  = self.count(s), self.count(t)

        for char in c_t.keys():
            if c_s.get(char) != c_t.get(char):
                return False

        for char in c_s.keys():
            if c_s.get(char) != c_t.get(char):
                return False

        return True

    def count(self, s):
        counter = {}
        for i in range(len(s)):
            if not counter.get(s[i]):
                counter[s[i]] = 1
            else:
                counter[s[i]] += 1
        return counter


        