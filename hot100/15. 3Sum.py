"""
15、三数之和
解法:排序+双指针
先将nums排序,一次遍历，确定 i,再取下一个和最后一次分别为 left、right 双指针
依次向中间靠近,获取和值等于0。如果相邻值相等,就跳过
"""
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            # 因为 i-1 所在数字已经搜索过一次了，i 就直接跳过，不然结果会有重复的
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    res.append((nums[i], nums[left], nums[right]))
                    # 如果指针走的下一个值和当前值相等，就直接到下下一个
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1;right -= 1
        