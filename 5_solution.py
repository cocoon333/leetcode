"""
5. Longest Palindromic Substring
Medium

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s):
        longest = ""
        for i in range(len(s)):
            current = ""
            current += s[i]
            r = 1
            l = 1
            if i-1 >= 0 and s[i-1] == s[i] and (i+1 >= len(s) or (i+1 < len(s) and s[i+1] != s[i])):
                l += 1
                current += s[i-1]
            elif (i-1 < 0 or (i-1 >= 0 and s[i-1] != s[i])) and i+1 < len(s) and s[i+1] == s[i]:
                r += 1
                current += s[i+1]
            while i-l >= 0 and i+r < len(s) and s[i-l] == s[i+r]:
                current = s[i-l] + current + s[i+r]
                l += 1
                r += 1
            if len(current) > len(longest):
                longest = current
        return longest

if __name__ == "__main__":
    s = Solution()
    assert(s.longestPalindrome("cbbd") == "bb")
    assert(s.longestPalindrome("babad") == "bab")
