"""
62. 不同路径
解法:动态规划
由于只能向下或向右移动一步,通过画表,得出转移方程 db[i][j] = dp[i-1][j] + dp[i][j-1]
也就是到达当前位置 dp[i][j]的路径数等于上方和左侧的路径数之和
这里为了节省空间复杂度,使用一维数组,也就是 n 的长度
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j - 1]
        return cur[-1]

print(Solution().uniquePaths(3, 7))