class Solution:
    def numDecodings(self, s: str) -> int:

        if int(s[0]) == 0:
            return 0

        dp = [0] * len(s)

        dp[0] = 1

        for i in range(1, len(s)):

            if int(s[i]) == 0:
                if int(s[i - 1]) == 1 or int(s[i - 1]) == 2:

                    if i >= 2:
                        dp[i] = dp[i - 2]
                    else:
                        dp[i] = dp[i - 1]
                else:
                    return 0


            elif int(s[i]) <= 6 and (int(s[i - 1]) == 1 or int(s[i - 1]) == 2):
                if i >= 2:
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    dp[i] = dp[i - 1] + 1

            elif int(s[i]) > 6 and int(s[i - 1]) == 1:
                if i >= 2:
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    dp[i] = dp[i - 1] + 1

            else:
                dp[i] = dp[i - 1]

        return dp[-1]