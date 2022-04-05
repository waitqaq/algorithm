"""
34. 在排序数组中查找元素的第一个和最后一个位置
解法:二分查找
因为数组是升序排列,所以target第一次出现的位置到比他大数字的前一个位置就是目标区间
需要进行两次二分查找,因为返回left的值,可能存在超出索引
"""
class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        def binarySearch(nums, target):
            left, right = 0, len(nums) - 1
            mid = (left + right) // 2
            while left < right:
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        
        a = binarySearch(nums, target)
        b = binarySearch(nums, target + 1)
        # left走到头也没有找到 或者 目标值不存在
        if a == len(nums) or nums[a] != target:
            return [-1, -1]
        else:
            return [a, b-1]