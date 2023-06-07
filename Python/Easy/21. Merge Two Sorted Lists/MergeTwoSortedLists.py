# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        

        temp = ListNode()
        isItFirst = True
        while True:

            if list1.val < list2.val:
                if not isItFirst:
                    self.veriekle(temp,list1.val)
                    
                    
                else:
                    temp.val = list1.val
                    isItFirst = False
                    
                
                
                
                list1 = list1.next
                if list1 == None :
                    while True:
                        if list2 == None:
                            break
                        self.veriekle(temp,list2.val)
                        list2 = list2.next
                    break
                    
            elif list1.val == list2.val:
                if not isItFirst:
                    self.veriekle(temp,list1.val)
                    self.veriekle(temp,list2.val)
                else:
                    temp.val = list2.val
                    self.veriekle(temp,list1.val)
                    isItFirst = False
                

                
                list2 = list2.next
                list1 = list1.next

                if list1 == None:
                    while True:
                        if list2 == None:
                            break
                        self.veriekle(temp,list2.val)
                        list2 = list2.next
                    break
                    
                if list2 == None:
                    while True:
                        if list1 == None:
                            break
                        self.veriekle(temp,list1.val)
                        list1 = list1.next
                    break



            elif list1.val > list2.val :
                if not isItFirst:
                    self.veriekle(temp,list2.val)
                else:
                    temp.val = list2.val
                    isItFirst = False
                

                
                list2 = list2.next
                if list2 == None :
                    while True:
                        if list1 == None:
                            break
                        self.veriekle(temp,list1.val)
                        list1 = list1.next
                    break
                   
                
            
            


        return temp


    def veriekle(self,root,value):
        ilk = 0
        ilk = root

        while True:
            if root.next != None:
                root = root.next
            else:
                break
        
        temp = ListNode(val = value)
        root.next = temp

        return ilk


                
                        


