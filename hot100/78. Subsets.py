"""
78. 子集
解法:递归

"""
class Solution:
    def subsets(self, nums):
        res = []
        n = len(nums)
        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1, tmp + [nums[j]])
        helper(0, [])
        return res

print(Solution().subsets([1,2,3]))