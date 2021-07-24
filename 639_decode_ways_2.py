"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

In addition to the mapping above, an encoded message may contain the '*' character, which can represent any digit from '1' to '9' ('0' is excluded). For example, the encoded message "1*" may represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", or "19". Decoding "1*" is equivalent to decoding any of the encoded messages it can represent.

Given a string s containing digits and the '*' character, return the number of ways to decode it.

Since the answer may be very large, return it modulo 109 + 7.
"""

class Solution:
    def numDecodings(self, s):
        if not s:
            return 0
        dp = []
        dp.append(1)
        dp.append(self.oneDecoding(s[0]))
        for i in range(2, len(s)+1):
            single = self.oneDecoding(s[i-1]) * dp[i-1]
            double = self.twoDecoding(s[i-1], s[i-2]) * dp[i-2]
            dp.append((single + double) % (10 ** 9 + 7))
        print(dp)
        return dp[-1]

    def oneDecoding(self, curr):
        if (curr == "*"):
            return 9
        if (curr == "0"):
            return 0
        return 1

    def twoDecoding(self, curr, prev):
        if (prev == "*"):
            if (curr == "*"):
                return 15
            elif (int(curr) > 6):
                return 1
            return 2
        elif (prev == "1"):
            if (curr == "*"):
                return 9
            return 1
        elif (prev == "2"):
            if (curr == "*"):
                return 6
            return int(int(curr) <= 6)
        else:
            return 0

if (__name__ == "__main__"):
    S = Solution()
    assert(S.numDecodings('11106') == 2)
    assert(S.numDecodings('2839') == 1)
    assert(S.numDecodings('1*') == 18)
    assert(S.numDecodings('*') == 9)
    assert(S.numDecodings('2*') == 15)
    assert(S.numDecodings('11111') == 8)
    assert(S.numDecodings('1*09') == 2)
    assert(S.numDecodings('*9') == 10)
    print(S.numDecodings('1*9'))
