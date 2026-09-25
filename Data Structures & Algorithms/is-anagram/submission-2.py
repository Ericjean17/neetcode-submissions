class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # can't be anagrams
            return False

        # store letter occurences for both strings
        dict_s = {}
        dict_t = {}

        for letter in s:
            # dict_s[letter] = dict_s.get(letter, 0) + 1
            if letter not in dict_s:
                dict_s[letter] = 1
            else:
                dict_s[letter] += 1
        
        for letter in t:
            if letter not in dict_t:
                dict_t[letter] = 1
            else:
                dict_t[letter] += 1

        return dict_s == dict_t