"""
75. 颜色分类
解法:双指针
初始化双指针 p0 和 p1 
遍历数组,当等于 0 的时候,将所在元素与 p0 交换，之后将；当等于 1 的时候,将所在元素与 p1 交换
"""

class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = p1 = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                # 因为 0 后面是 1，直接 i 和 p0 交换的话，会导致 1 被交换出去
                # 所以需要再把 i 和 p1 交换
                if p0 < p1:
                    nums[i], nums[p1] = nums[p1], nums[i]
                # 所以两个都要加 1
                p0 += 1
                p1 += 1
