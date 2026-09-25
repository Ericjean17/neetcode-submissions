class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} 
        for i, n in enumerate(nums): 
            complement = target - n # target = current num + complement
            if complement in seen:
                return [seen[complement], i]
            seen[n] = i
        return []

        # O(n) space worst case (store all nums)
        # O(n) time worst case (iterate on all nums)