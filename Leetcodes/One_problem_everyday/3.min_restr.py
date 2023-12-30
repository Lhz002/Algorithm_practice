class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        longest = ""

        for i in range(n):
            for j in range(i, n):
                if s[i] == s[j] and s[i: j + 1] == s[i: j + 1][::-1]:
                    if j - i + 1 > len(longest):
                        longest = s[i: j + 1]
        return longest

if __name__ == "__main__":
    s = "babad"
    S = Solution()
    print(S.longestPalindrome(s))
