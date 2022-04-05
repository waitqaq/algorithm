"""
32. 最长有效括号
解法:栈
遍历字符串,左括号索引入栈,如果是右括号,就意味着栈第一个匹配,并弹出一个左括号
记录每次栈长度和res的最大值,最后得到的res就是最长的栈长度
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                # 始终保持栈底元素为当前已经遍历过的元素中
                # 最后一个没有被匹配的右括号的下标
                # 去统计后续的有效括号序列
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res