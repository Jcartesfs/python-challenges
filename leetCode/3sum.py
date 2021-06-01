#https://leetcode.com/problems/3sum/submissions/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        if n <3:
            return []
    
        d = {}
        l = []
        nums = sorted(nums)
        max_value = abs(max(nums))
        
        for i, x in enumerate(nums):
            #x = nums[i]
            if x > 0:
                break
            
            for j, y in enumerate(nums[i+1:]):
                #y = nums[j]
                z = x + y 
                
                if (x + y) > max_value:
                    break
                
                if -1*z in nums[i+j+2:]:
                    l_value = list(sorted([x , y, -1*z]))
                    idx   = ''.join(str(item) for item in l_value)
                    d[idx] = [x , y, -1*z]
                        
                            
                        
        return list(d.values())
