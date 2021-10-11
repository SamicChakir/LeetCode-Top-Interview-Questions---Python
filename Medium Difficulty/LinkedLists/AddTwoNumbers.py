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
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start = ListNode(0, None)

        number_left = 0
        current = start
        isFirst = True
        while (l1 != None and l2 != None):
            current_sum = l1.val + l2.val + number_left
            if current_sum > 9:
                number_left = 1
                current_sum = current_sum - 10
            else:
                number_left = 0

            if isFirst:
                start.val = current_sum
                isFirst = False
            else:
                current.next = ListNode(current_sum,None)
                current = current.next

            l1 = l1.next
            l2 = l2.next



        while (l1 != None):
            current_sum = l1.val + number_left
            if current_sum > 9:
                number_left = 1
                current_sum = current_sum - 10
            else:
                number_left = 0
            current.next = ListNode(current_sum, None)
            current = current.next
            l1 = l1.next

        while (l2 != None):
            current_sum = l2.val + number_left
            if current_sum > 9:
                number_left = 1
                current_sum = current_sum - 10
            else:
                number_left = 0
            current.next = ListNode(current_sum, None)
            current = current.next
            l2 = l2.next
        if (number_left > 0):
            current.next = ListNode(number_left, None)
            current = current.next

        return start
node7 = ListNode(9,None)
node6 = ListNode(9,node7)
node5 = ListNode(9,node6)
node4 = ListNode(9,node5)
node3 = ListNode(9,node4)
node2 = ListNode(9,node3)
node1 = ListNode(9,node2)

sec_node4 = ListNode(9,None)
sec_node3 = ListNode(9,sec_node4)
sec_node2 = ListNode(9,sec_node3)
sec_node1 = ListNode(9,sec_node2)

sol = Solution()

res = sol.addTwoNumbers(node1,sec_node1)
print(res)
t= 0

