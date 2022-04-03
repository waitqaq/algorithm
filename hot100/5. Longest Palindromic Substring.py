"""
5、最长回文子串
解法: 中心扩展法
按两种方法，长度为奇数（从i位置向两边搜索），长度为偶数（从i，i+1位置向两边搜索）
每次搜索当左右长度大于 end-start 就意味着 有新的更长的回文子串，更新 end、start值
最后，返回最长的 start 到 end+1
"""
from turtle import left, right


class Solution:
    def expandAroundCenter(self, s, left, right):
        # 左边界大于0，右边界小于字符串长度，左右两侧相等
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # 向两边扩散
            left -= 1
            right += 1
        # 返回相等时的两侧边界值
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            # 从 i 的位置向两边搜索
            left1, right1 = self.expandAroundCenter(s, i, i)
            # 从 i 和 i+1 的位置向两边搜索
            left2, right2 = self.expandAroundCenter(s, i, i+1)
            # 上面两种搜索，如果有符合的就记录当前的最长回文子串，更新 start 和 end
            # 再次取值进行搜索两种情况，直到最终最长回文子串
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end+1]

s = Solution()
print(s.longestPalindrome('acdbbdaa'))