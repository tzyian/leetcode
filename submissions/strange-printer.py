// https://leetcode.com/problems/strange-printer

# note that iterating dp[i][i] wont work because that doesnt take into account the start and end char could be the same
# some pruning can be done by reducing consecutive duplicate characters to a single but same TC
# alternative way to go about it is to assume that the string is circular

class Solution:
    def strangePrinter(self, s: str) -> int:
        s = re.sub(r'(.)\1*', r'\1', s)
        n = len(s)
        dp = [[n] * n for _ in range(n)]
        for length in range(1, n + 1):
            for left in range(n - length + 1):
                # in a substring from left to right of length "length"
                # calc how many chars need to be reprinted in this range
                right = left + length - 1
                j = -1  # leftmost index of char differing from s[right]
                        # -1 means not found char yet
                for i in range(left, right):
                    if s[i] != s[right] and j == -1:
                        j = i # leftmost char differing has been found
                    if j != -1:
                        dp[left][right] = min(
                            dp[left][right], 
                            # since dp[][] is initialised to n which is guaranteed possible,
                            # check whether it can be done in fewer operations
                            # dp[left][right] is optimal when it is calculated alr
                            # else optimal will be the below
                            1 + dp[j][i] + dp[i + 1][right] 
                            # print once from j to i, and once from i+1 to right
                        )
                
                if j == -1:
                    # this solution pushes the case where l=r here to initialise the diagonal as 0
                    # in the substring of left to right, they are all the same char
                    # so no processing is needed
                    dp[left][right] = 0

        # +1 because printing char 0 to char n-1 is 1, 
        # and the dp assumes all chars are the same and alr printed
        return dp[0][n - 1] + 1

