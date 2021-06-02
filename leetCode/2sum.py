#https://leetcode.com/problems/two-sum
#Solution O(n) and not O(n2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
               
        d = {}
        for i, x in enumerate(nums):
            diff = target - x
            
            if diff not in d:
                d[x] = i
            else:
                return [i, d[diff]]
