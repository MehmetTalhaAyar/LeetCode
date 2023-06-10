"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        

        if head == None:
            return None
        
        headRoot = head
        temp = None
        lastIndex = None

        while True:
            print(head.val)
            if head.next == None and head.child == None:
                break

            if head.child != None:
                if head.next != None:
                    temp = head.next
                head.next = head.child
                head.next.prev = head
                head.child = None
                if head.next != None:
                    lastIndex = head.next
                while temp != None:
                    if lastIndex.next == None:
                        lastIndex.next = temp
                        temp.prev = lastIndex
                        break
                    else:
                        lastIndex = lastIndex.next
            else:
                head = head.next

        return headRoot
