# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
     def __str__(self):
         res_str = "[ "
         cur = self
         while( cur != None):
             res_str = res_str +  str(cur.val) + ", "
             cur = cur.next
         return res_str + " ]"
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        if head.next is None:
            return head
        odd_head = head
        even_head = head.next

        current_odd = odd_head
        current_even = even_head

        current = head.next.next

        while current is not None:
            if current is None:
                break;
            suiv = current.next
            current_odd.next = current
            current_even.next = suiv

            current_even = current_even.next
            current_odd = current_odd.next
            if suiv is not None:
                current = suiv.next
            else:
                current = suiv
        current_odd.next = even_head


        return odd_head

