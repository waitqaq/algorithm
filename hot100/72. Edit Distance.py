"""
72. 编辑距离
解法:动态规划
二维数组,纵轴为word1,横轴为 word2,那么可以认为
第一行是 word1 向 word2 新增操作变化;第一列是word1向 word2 删除操作变化
也就是 dp[i-1][j-1] 表示替换操作; dp[i][j-1] 表示插入操作;dp[i-1][j] 表示删除操作
特征方程为:
当 word1[i] == word2[j],dp[i][j] = dp[i-1][j-1];
当 word1[i] != word2[j],dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        if m * n == 0:
            return 0
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[-1][-1]
                
print(Solution().minDistance("", "ros"))