"""
64. 最小路径和
解法:动态规划,获取动态方程
i = 0: dp[i][j] += dp[i][j-1]
j = 0: dp[i][j] += dp[i-1][j]
非边缘位置: dp[i][j] += min(dp[i][j-1], dp[i-1][j])
最后一个就是最小路径和
"""

class Solution:
    def minPathSum(self, grid) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i][j-1], grid[i-1][j])
        return grid[-1][-1]
Solution().minPathSum([[1,2,3],[4,5,6]])