"""
31. 下一个排列
解法:从后往前先找到最近的两个元素的上升序列起点i,再找到比i第二大的所在位置j,两者交换
将 i 之后的序列降序排序
"""
class Solution:
    def nextPermutation(self, nums: list) -> None:
        i = len(nums) - 2
        # 从后往前搜索最近的一个上升序列，即前一个大于后一个
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            # 从后往前搜索最近的比 i 所在大的元素，两者交换
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # 将从 i 到结尾的序列进行降序排序
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1