"""
22、括号生成
解法:递归+剪枝
首先,list内存左括号和右括号的数量都等于n才满足条件,这也是递归终止条件
递归获取左括号所有情况数量然后匹配到右括号,每次到递归终止条件意味着获取到了当前组合的情况
当前结果加入list,然后return,即返回上一步再去匹配其他情况
"""
class Solution:
    def generateParenthesis(self, n: int):
        self.list = []
        self._gen(0, 0, n, "")
        return self.list

    def _gen(self, left, right, n ,result):
        if left == n and right == n:
            self.list.append(result)
            return
        if left < n:
            self._gen(left+1, right, n, result+'(')
        if left > right and right < n:
            self._gen(left, right+1, n, result+')')

Solution().generateParenthesis(3)
