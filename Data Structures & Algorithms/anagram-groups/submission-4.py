class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        # Brute force - O(m*nlogn) time
        # res = defaultdict(list)
        # for s in strs:
        #     sortedS = ''.join(sorted(s)) # [eat] -> [aet] -> "aet"
        #     res[sortedS].append(s)
        # return list(res.values())

        res = defaultdict(list)
        for s in strs: 
            count = [0] * 26 # 26-length frequency table
            for c in s: 
                count[ord(c) - ord('a')] += 1 # ('c' : 1) == ('2' : 1)
            res[tuple(count)].append(s) # table is stored as the anagram mapped to string
        return list(res.values())

        # O(m*n) time where m = number of strings and n = length of longest string