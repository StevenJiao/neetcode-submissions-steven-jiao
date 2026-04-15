class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = 0
            else:
                s_dict[s[i]] += 1
            
            if t[i] not in t_dict:
                t_dict[t[i]] = 0
            else:
                t_dict[t[i]] += 1
        
        if len(s_dict) != len(t_dict):
            return False

        for key in s_dict:
            if key not in t_dict or s_dict[key] != t_dict[key]:
                return False

        return True