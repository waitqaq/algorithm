"""
20、有效的括号
解法:辅助栈
使用栈保存左括号,然后弹出去匹配过来的左括号
"""
class Solution:
    def isValid(self, s: str) -> bool:
        # 避免下方pop弹出异常
        stack = ['?']
        brackets_map = {
            '(': ')',
            '{': '}',
            '[': ']',
            '?': '?'
        }
        for i in s:
            if i in brackets_map:
                stack.append(i)
            elif brackets_map[stack.pop()] != i:
                return False
        return len(stack) == 1