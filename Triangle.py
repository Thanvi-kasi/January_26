class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Copy the last row as the initial DP state
        dp = triangle[-1][:]

        # Start from the second-to-last row and move upward
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]
