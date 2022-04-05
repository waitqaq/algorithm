"""
33. 搜索旋转排序数组
解法:二分查找
每次将数组分为两份,如果mid的值小于nums[0],那么mid之前是上升序列
如果target在0到mid之间,那么right就直接到当前mid前即可,mid之后的可以舍弃
反之同理
"""
class Solution:
    def search(self, nums: list, target: int) -> int:
        if not list:
            return -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + target) // 2
            if nums[mid] == target:
                return mid
            # 左侧是上升序列
            if nums[0] < nums[mid]:
                # target在mid左侧,将rigth移动到mid左侧,右侧可以舍弃
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 右侧是上升序列
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1