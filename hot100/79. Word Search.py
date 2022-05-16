"""
79. 单词搜索
解法:深度优先搜索与回溯
从一个字符开始匹配 word 的元素,如果不是当前路径返回 False,从第二个字符开始
每到一个字符,分别从四个方向走一遍,直到该方向路径返回搜索结果
"""
class Solution:
    def exist(self, board, word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(i, j, k):
            """
            表示从(i, j) 触发,能否搜索到 word[k](表示word 从第 k 个字符开始的后缀子串)
            """
            # 如果当前不匹配，直接返回 False
            if board[i][j] != word[k]:
                return False
            # 如果访问到末尾，依然匹配，返回 True
            if k == len(word) - 1:
                return True
            # 记录足迹
            visited.add((i, j))
            result = False
            # 四个方向，每次向一个方向移动，直到匹配 return
            # 匹配到就是 True，不匹配就是 False，然后换个方向
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    # 确保没有重复的足迹
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            result = True
                            break
            # 删除当前路径
            visited.remove((i, j))
            return result
        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True
        return False

print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))