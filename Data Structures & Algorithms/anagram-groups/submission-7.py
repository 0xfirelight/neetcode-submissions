class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        used = {}
        groups = []

        for i in range(len(strs)):
            if used.get(strs[i]):
                continue

            group = [strs[i]]
            used[i] = True
            for j in range(i+1, len(strs)):
                if used.get(j):
                    continue
                if self.is_anagram(strs[i], strs[j]):
                    group.append(strs[j])
                    used[strs[j]] = True

            groups.append(group)

        return groups

    def is_anagram(self, s1: str, s2: str):
        if len(s1) != len(s2):
            return False

        counter_one, counter_two = self.count_s(s1), self.count_s(s2)
        for k, c in counter_one.items():
            if counter_two.get(k) != c:
                return False

        for k, c in counter_two.items():
            if counter_one.get(k) != c:
                return False

        return True

    def count_s(self, s1):
        counter = {}
        for c in range(len(s1)):
            if counter.get(s1[c]):
                counter[s1[c]] += 1
            else:
                counter[s1[c]] = 1

        return counter