# Definition for a Node.
class Node:
    def __init__(self, val=None, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        dummy = Node(0, None, head, None)
        stack = [head]
        prev = dummy
        
        while stack:
            current = stack.pop()
            
            if current.next:
                stack.append(current.next)
            
            if current.child:
                stack.append(current.child)
                current.child = None
            
            prev.next = current
            current.prev = prev
            prev = current
        
        dummy.next.prev = None
        return dummy.next
