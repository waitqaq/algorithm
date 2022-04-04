"""
19、删除链表的倒数第N个结点
解法:双指针
添加一个头结点0,然后定义fast、slow指针,开始时fast先走到要删除的n的位置
然后,fast和slow一起向后移动,直到fast指向none,意味着slow走到了要删除结点的位置
通过next指向next.next,完成删除节点的位置
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        fast = head
        slow = dummy
        for i in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy.next