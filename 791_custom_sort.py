"""
order and str are strings composed of lowercase letters. In order, no letter occurs more than once.

order was sorted in some custom order previously. We want to permute the characters of str so that they match the order that order was sorted. More specifically, if x occurs before y in order, then x should occur before y in the returned string.

Return any permutation of str (as a string) that satisfies this property.
"""

class Solution:
    def customSortString(self, order, string):
        ordering = {}
        for i in range(len(order)):
            ordering[order[i]] = i

        return "".join(sorted(string, key=lambda char: ordering.get(char, 26)))

if (__name__ == "__main__"):
    S = Solution()
    assert(S.customSortString("cba", "abcd") == "cbad")
    assert(S.customSortString("b", "aaab") == "baaa")
    assert(S.customSortString("", "aaa") == "aaa")
    assert(S.customSortString("abc", "") == "")
