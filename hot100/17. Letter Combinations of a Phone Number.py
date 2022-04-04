"""
17、电话号码的字母组合
解法: 回溯
比如目标为23, 2 对应 abc,那么(先让a和3中的d组合,再回溯a和e组合,再回溯a和f组合)
再大回溯到b、c同样按照该方法处理
"""
class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return list()
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index):
            """
            获取当前index的最终结果
            """
            # 本次回溯结束，拼接当前最终结果
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                # 按index获取digits的单个字符串
                digit = digits[index]
                # 按字符串从map中取出对应字符串遍历
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    # 走下一步，即获取digits的下一个字符串进行操作
                    backtrack(index+1)
                    # 回溯到上一步 
                    combination.pop()
        combination = list()
        combinations = list()
        backtrack(0)
        return combinations
Solution().letterCombinations("23")