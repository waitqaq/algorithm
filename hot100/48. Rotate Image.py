"""
48. 旋转图像
解法:原地旋转
先将数组水平翻转,再对角线翻转
"""
class Solution:
    def rotate(self, matrix: list) -> None:
        n = len(matrix)
        # 水平翻转,i值大小在一半以内,上面的与下面对应翻转
        # j值大小不变
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]
        # 对角线翻转,j下标取对角即可
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]