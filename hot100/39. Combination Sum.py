"""
39. 组合总和
解法:搜索回溯+剪枝
第一次,使用target减去candidates第一个元素,得到residue,再减去candidates的其他元素,一直向下分叉
直到找到目标,将当前路径添加到res.
如果相减之后已经小于0,说明已经递归到头,结束
"""
class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:

        def dfs(candidates, begin, size, path, res, target):
            # 找到目标,添加到res
            if target == 0:
                res.append(path)
                return
            for index in range(begin, size):
                residue = target - candidates[index]
                # residue小于0,即当前枝杈到头退出循环
                if residue < 0:
                    break
                # index: candidates下一个元素 
                # path + [candidates[index]]: 递归拼接当前路径的数组
                dfs(candidates, index, size, path + [candidates[index]], res, residue)

        size = len(candidates)
        if size == 0:
            return []
        # 因为如果减去一个数得到负数，那么减去一个更大的数还是负数
        # 利用排序达到剪枝的效果
        candidates.sort()
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res