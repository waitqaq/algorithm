"""
49. 字母异位词分组
解法:统计计数
分别将每个字母的 ascall 码为字典的key保存,value为key相同的元素组成的字典
"""
import collections
class Solution:
    def groupAnagrams(self, strs: list) -> list:
        mp = collections.defaultdict(list)
        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord('a')] += 1
            # 添加 value 内容
            mp[tuple(counts)].append(st)
    
        return list(mp.values())