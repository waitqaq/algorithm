"""
55. 跳跃游戏
解法:贪心
第一次在下标0的位置的元素即当前最大跳跃长度,往后遍历,使用rightmost维护最大长度
"""
class Solution:
    def canJump(self, nums: list) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                # 获取 前面rightmost 和 当前下标+元素 的最大值
                rightmost = max(rightmost, i + nums[i])
                # 如果大于等于数组长度，即已经可以到达结束
                if rightmost >= n - 1:
                    return True
        return False
