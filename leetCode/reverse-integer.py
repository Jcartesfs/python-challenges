#https://leetcode.com/problems/reverse-integer/submissions/
class Solution:   
    
    def checkValue(self, num: int) -> int:
        pos_neg = 1
        
        if num >= 0:
            pos_neg = 1
        else:
            pos_neg = -1
            
        return pos_neg
        
    def reverse(self, x: int) -> int:
        
        if x == 0:
            return 0
        
        x = self.checkValue(x)*int(str(abs(x))[::-1])

        return 0 if x < -2**31 or x > 2**31 -1 else x