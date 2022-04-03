"""
4、寻找两个正序数组的中位数
解法: 首选，可以将转化为求数组的第k个元素。
     为了不区分长度为奇数和偶数，两种情况都求，最后求和除以2
"""
class Solution:
    def findMedianSortArrays(self, nums1, nums2):
        # 找第 K 个元素
        def findKthElement(arr1, arr2, k):
            len1, len2 = len(arr1), len(arr2)
            # 如果 arr1 的长度大于 arr2 的，将两者互换
            # 这里是为了省略对两个数组长度分别判断两次，在这里判断互换，可以使用下方的not判断直接返回结果
            if len1 > len2:
                return findKthElement(arr2, arr1, k)
            # 当 arr1 切片后为空，返回 arr2 k 之后的数组 
            if not arr1:
                return arr2[k-1]
            # 如果k是1，直接取两个数组的最小数字
            if k == 1:
                return min(arr1[0], arr2[0])
            # 检查是否存在 k/2 数字
            # 如果存在就取出，否则就赋值最大值，即数组长度
            # -1 为了防止下面切片超出index
            i, j = min(k//2, len1)-1, min(k//2, len2)-1
            # 比较两个数字第 k/2 小的数字的大小
            # 如果 arr1 大于 arr2，那么说明要找的数字肯定不在 arr2 的前 k/2 个数字
            # 也就是将 arr2 的起始位置向后移动 k/2，那么k也得减去 k/2
            if arr1[i] > arr2[j]:
                return findKthElement(arr1, arr2[j+1:], k-j-1)
            else:
                return findKthElement(arr1[i+1:], arr2, k-i-1)
        
        l1, l2 = len(nums1), len(nums2)
        # 这里为了不区分 奇数个 和 偶数个，两种情况都求
        # 如果 l1+l2 是奇数，那么 left和right 是相等的
        left, right = (l1+l2+1)//2, (l1+l2+2)//2
        return (findKthElement(nums1, nums2, left) + findKthElement(nums1, nums2, right)) / 2

s = Solution()
print(s.findMedianSortArrays([1,3], [2]))