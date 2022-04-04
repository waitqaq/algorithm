"""
21、合并两个有序链表
解法:双指针
首先,构建一个前驱节点和指针,list1和list2当前节点的值比较,取最小的值拼接到前驱指针,然后向后移动
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        prehead = ListNode(-1)
        prev = prehead
        while list1 and list2:
            if list1 <= list2:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        # 最后剩余一个节点，直接拼接到末尾
        prev.next = list1 if list1 is not None else list2
        return prehead.next