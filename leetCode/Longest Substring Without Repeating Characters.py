
#https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/3008/
import string

class Solution:
  
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #Condition max characters
        n = len(s)
        sp = len(string.printable)
        if n > sp:
            n = sp
    
        #Find longest substring without repeating characters
        for ln in reversed(range(0,n+1)):
            for x in range(0, (n - ln)+1):
                subs = s[x:ln+x]
                unique_letters = ''.join(set(subs))
                if ln == len(unique_letters):
                    return ln
        return 0