"""
42. 接雨水
解法:双指针
维护left和right两个指针,leftMax为left指针向右每次得到的最高柱子,那么比它小的柱子之间就会存在沟壑,用来存雨水
每次累加这个沟壑的面积,就是最终的面积
"""
class Solution:
    def trap(self, height: list) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        leftMax = 0
        rightMax = 0
        
        while left < right:
            leftMax = max(leftMax, height[left])
            right = max(rightMax, height[right])
            # 如果height[left] < height[right],必定leftMax<rightMax
            # 所以要左侧为实际接水量
            if height[left] < height[right]:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1
        return ans