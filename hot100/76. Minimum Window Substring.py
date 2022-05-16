"""
76. 最小覆盖子串
解法:滑动窗口
维护一个 hash_table ,初始化为目标字符串 t 每个元素的个数为 kv,以及要匹配的次数 need_count,来避免遍历 hash_table
然后遍历字符串 s,如果 need_count 等于 0,意味着匹配到了,开始缩减 i,找到 hash_table 要匹配的第一个个数为 0 时,说明当前 i 已经到最短了
计算当前 i 和 j 的距离,如果小就更新到 res
然后把要匹配的第一个元素个数 + 1,need_count + 1, i + 1 寻找另一个窗口
"""
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_table = collections.defaultdict(int)
        # 初始化包含所有要匹配的元素及元素个数
        for i in t:
            hash_table[i] += 1
        i = 0
        # 初始化一个0 到正无穷的区间
        res = (0, float('inf'))
        # 初始化需要寻找的元素个数
        need_count = len(t)
        for j,c in enumerate(s):
            # 如果该元素是要匹配的元素，那么 need_count 就减一
            if hash_table[c] > 0:
                need_count -= 1
            # 遍历一个元素，就将它的次数就减一，直到 hash_table 中要匹配的元素个数都为 0 
            hash_table[c] -= 1
            # 当窗口包含所有目标元素
            if need_count == 0:
                # 开始增加 i，即缩小窗口，排除多余元素
                while True:
                    single = s[i]
                    # 直到碰到第一个必须包含的元素，跳出
                    if hash_table[single] == 0:
                        break
                    # 记录 i 经过的元素
                    hash_table[single] += 1
                    i += 1
                # 当前窗口小于前一个窗口，就更新
                if j - i < res[1] - res[0]:
                    res = (i, j)
                # 将第一个要匹配的元素的个数加 1，来去寻找下一个窗口
                hash_table[s[i]] += 1
                # 对应 i 加 1，need_count 加 1
                need_count += 1
                i += 1
        # 如果 res[1]>len(s)，证明是正无穷，也就是没找到
        return '' if res[1]>len(s) else s[res[0]:res[1]+1]

print(Solution().minWindow("a", "aa"))


