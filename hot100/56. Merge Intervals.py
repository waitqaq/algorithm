"""
56. 合并区间
解法:先按数组第一个元素排序,形成start升序的二维数组
遍历目标二维数组,如果merged的end小于当前目标的start,意味着是一个新的范围,那么直接将它添加进来
如果merged的end大于当前目标的start,意味着该数组在merged最后一个数组的范围内,取这个得end和当前的interval的end的最大值
就是当前合并数组的end最大范围
"""
class Solution:
    def merge(self, intervals: list) -> list:
        intervals.sort(key=lambda x:x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged