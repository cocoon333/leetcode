"""
3. Longest Substring Without Repeating Characters
Medium

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        count = 0
        max_count = 0
        current_substring = {}
        i = 0
        while i < len(s):
            if s[i] in current_substring:
                i = current_substring[s[i]]+1
                if i >= len(s):
                    break
                current_substring = {s[i]:i}
                if count > max_count:
                    max_count = count
                count = 1
            else:
                current_substring[s[i]] = i
                count += 1
            i += 1

        return max(count, max_count)

if __name__ == "__main__":
    s = Solution()
    assert(s.lengthOfLongestSubstring("dvdf") == 3)
    assert(s.lengthOfLongestSubstring(" ") == 1)
    assert(s.lengthOfLongestSubstring("abcabcbb") == 3)
    assert(s.lengthOfLongestSubstring("bbbbb") == 1)
    assert(s.lengthOfLongestSubstring("pwwkew") == 3)
