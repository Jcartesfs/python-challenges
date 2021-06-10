

#https://leetcode.com/problems/longest-palindromic-substring/submissions/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s) + 1
        for i in reversed(range(0, n)):
            for j in range(n-i):
                target = s[j:i+j]
                if target[::-1] in s:
                    return target
        return s
        