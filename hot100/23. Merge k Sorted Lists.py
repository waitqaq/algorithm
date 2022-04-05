"""
23. 合并K个升序链表
解法:优先队列
使用heapq库,构造堆(默认小顶堆),先将每个元素都添加到小顶堆中
创建空节点,连接从小顶堆中弹出的元素,最后返回空节点的next
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: ListNode) -> ListNode:
        if not lists:
            return
        import heapq
        queue = []
        for l in lists:
            while l:
                heapq.heappush(queue, l.val)
                l = l.next
        dummy = ListNode(-1)
        cur = dummy
        while queue:
            cur.next = ListNode(heapq.heappop(queue))
            cur = cur.next
        return dummy.next