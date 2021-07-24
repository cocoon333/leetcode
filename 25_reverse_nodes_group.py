"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
"""

class ListNode:
     def __init__(self, val=0, next_node=None):
         self.val = val
         self.next = next_node

class Solution:
    def reverseKGroup(self, head, k):
        node = head
        length = 0
        while node:
            length += 1
            node = node.next

        if length < k or k <= 1:
            return head

        prev_tail = ListNode()
        tail = head
        res = prev_tail
        node = head
        for i in range(length // k):
            next_node = node.next
            for j in range(k-2):
                if j == 0:
                    tail = node
                temp = next_node.next
                next_node.next = node
                node = next_node
                next_node = temp
            temp = next_node.next
            print("temp", temp.val)
            print("next", next_node.val)
            print("node", node.val)
            next_node.next = node
            node.next = temp
            node = temp
            prev_tail.next = next_node
            prev_tail = tail
        return res.next

if (__name__ == "__main__"):
    S = Solution()
    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)

    res = S.reverseKGroup(n1, 3)
    print(res.val)
    print(res.next.val)
    print(res.next.next.val)
    print(res.next.next.next.val)
    print(res.next.next.next.next.val)
