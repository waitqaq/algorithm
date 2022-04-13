"""
46. 全排列
解法:回溯
将nums划分成左右两个部分,左边表示已经填过的数,右边表示待填的数
在回溯中动态维护这个数组
"""
class Solution:
    def permute(self, nums: list) -> list:
        def bfs(first = 0):
            # 当前分叉匹配完成
            if first == n:
                res.append(nums[:])
                return
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 递归下一个数
                bfs(first + 1)
                # 撤销交换,即向上回溯
                nums[first], nums[i] = nums[i], nums[first]
        n = len(nums)
        res = []
        bfs()
        return res

print(Solution().permute([1,2,3]))