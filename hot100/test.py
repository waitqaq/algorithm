from tkinter import N


class Solution:
    def groupAnagrams(self, strs: list) -> list:
        mp = {list: None}
        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord('a')] += 1
            mp[tuple(counts)].append(st)
    
        return list(mp.values)

print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))