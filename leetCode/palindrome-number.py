class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < -2**31 or x > 2**31 -1:
            return False
        
        x = str(x)
        
        if x == x[::-1]:
            return True
        else:
            return False