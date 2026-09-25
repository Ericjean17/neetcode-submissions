class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueNums = set()
        for num in nums: 
            if num in uniqueNums: # seen a number in past iteration
                return True
            uniqueNums.add(num) 
        return False

        # Time complexity - O(n)
        # Space complexity - O(n) since may need to store each num in set

        # return len(nums) != len(set(nums))

         