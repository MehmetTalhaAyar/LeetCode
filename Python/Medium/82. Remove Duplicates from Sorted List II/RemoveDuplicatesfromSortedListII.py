# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        unique = ListNode(val = None) 

        root = unique

        if head == None:
            return None
        elif head.next == None:
            return head
        
        isItGoing = False

        while True:
            temp = ListNode()
            if head.next == None:
                if unique.val != head.val and not isItGoing:
                    if unique.val == None:
                        unique.val = head.val
                    else:
                        temp.val = head.val
                        unique.next = temp
                break  

            if head.val == head.next.val:
                head = head.next
                isItGoing = True
            else:
                if not isItGoing:
                    if unique.val != None:
                        temp.val = head.val
                        unique.next = temp
                        unique = unique.next
                    else:
                        unique.val = head.val
                else:
                    isItGoing = False

                head = head.next
        
        if unique.val == None:
            return None
        else:
            return root