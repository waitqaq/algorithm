class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        cur = [1] * len(obstacleGrid)
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)
        for i in range(0, m):
            for j in range(0, n):
                if obstacleGrid[i][j] == 1:
                    cur[j] = 0
                    continue
                if j - 1 >= 0 and obstacleGrid[i][j-1] == 0:
                    cur[j] += cur[j - 1]
        return cur[-1]

Solution().uniquePathsWithObstacles([[0,1],[0,0]])