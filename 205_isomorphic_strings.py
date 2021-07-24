"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
"""

class Solution:
    def isIsomorphic(self, s, t):
        replacement = {}
        mapped = set()
        for i in range(len(s)):
            if (s[i] not in replacement):
                if (t[i] in mapped):
                    return False
                mapped.add(t[i])
                replacement[s[i]] = t[i]
            elif (not(replacement[s[i]] == t[i])):
                return False
        return True

if (__name__ == "__main__"):
    S = Solution()
    assert(S.isIsomorphic("egg", "add"))
    assert(not S.isIsomorphic("foo", "bar"))
    assert(S.isIsomorphic("paper", "title"))
    assert(not S.isIsomorphic("mississippi", "abccbddbeeb"))
    assert(not S.isIsomorphic("bb", "ab"))
    assert(not S.isIsomorphic("ab", "bb"))
