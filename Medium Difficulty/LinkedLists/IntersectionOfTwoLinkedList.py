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
         return res_str[:-2] + "]"

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        AplusC = self.countList(headB)
        reversedA = self.reverseLinkedListAndLength(headA)
        BplusC = self.countList(reversedA)
        AplusB = self.countList(headB) - 1
        headA = self.reverseLinkedListAndLength(reversedA)


        #already calculated calculate B + C
        # go through head B to calclate A + B
        #re reverse A
        # reverse  B to calculate A + C
        A = (- BplusC + AplusC + AplusB) // 2
        B = (BplusC - AplusC + AplusB) // 2
        C = (BplusC + AplusC - AplusB) // 2
        if A + C != AplusC or B + C != BplusC:
            return None
        stopB = AplusC - C
        cur = headB
        for i in range(stopB):
            cur = cur.next
        stopA = BplusC - C
        curA = headA
        for i in range(stopA):
            curA = curA.next
        if curA.val != cur.val:
            return None
        return cur



    def reverseLinkedListAndLength(self,headA):
        if (headA is None):
            return None

        current = headA

        suiv = current.next
        while ( suiv is not None):

            tmp = suiv.next
            suiv.next = current
            current = suiv
            suiv = tmp
        headA.next = None
        headA = current
        return headA

    def countList(self,head):
        cur = head
        count = 0
        while ( cur  is not None):
            count += 1
            cur = cur.next

        return count





node5 = ListNode(5,None)
node4 = ListNode(4,node5)
node3 = ListNode(8,node4)
node2 = ListNode(1,node3)
node1 = ListNode(4,node2)

node8 = ListNode(1,node3)
node7 = ListNode(6,node8)
node6 = ListNode(5,node7)



sol = Solution()

print(sol.getIntersectionNode(node6,node1))
# print("node1 :",node1)
# print("node 6: ", node6)


