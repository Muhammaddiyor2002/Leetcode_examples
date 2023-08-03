import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        count = 0
        result = 0
        current = self.head

        while current:
            count += 1
            if random.randint(1, count) == count:
                result = current.val
            current = current.next

        return result
