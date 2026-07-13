class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_freq = collections.Counter(s)
        t_freq = collections.Counter(t)

        for i in s:
            if s_freq[i] != t_freq[i]:
                return False

        return True
        