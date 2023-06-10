# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        result = ListNode()
        result.val = -1
        toplam = 0
        elde = 0
        
        while True:
            toplam = l1.val + l2.val + elde
            if toplam >= 10:
                elde = 1
                
                self.veriekle(result,toplam % 10)
                toplam = 0

            else :
                elde = 0

                self.veriekle(result,toplam % 10)
                toplam = 0

                if l1.next == None and l2.next == None:
                    break




            if l1.next != None:
                l1 = l1.next
            else :
                l1.val = 0          
                        
            if l2.next != None:
                l2 = l2.next
            else:
                l2.val = 0

            

        return result


    def veriekle(self,root,value):


        if root.val == -1:
            root.val = value
        else:
            temp = ListNode()
            temp.val = value
            while True:
                if root.next == None:
                    break
                else:
                    root = root.next
            root.next = temp
        
        return root




