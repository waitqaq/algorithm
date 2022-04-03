"""
11、盛最多水的容器
解法:两个指针分别从两侧向中间收缩，直到相遇，存在两种情况
1、向内移动 长板，面积可能会减小或相等
2、向内移动 短板，面积可能会增大
每次更新 res 即可，并且短板向内移动，不会导致丢失最大面积
"""
class Solution:
    def maxArea(self, height):
        i, j, res = 0, len(height)-1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i]*(j-i))
                i += 1
            else:
                res = max(res, height[j]*(j-i))
                j -= 1
        return res
