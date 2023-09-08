class DoublyLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        self.key_count = {}  # Dictionary to store key-count pairs
        self.count_key = {}  # Dictionary to store count-key pairs
        self.head = DoublyLinkedListNode(float('-inf'))
        self.tail = DoublyLinkedListNode(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head

    def _insert_after(self, prev_node, value):
        new_node = DoublyLinkedListNode(value)
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node
        return new_node

    def _insert_before(self, next_node, value):
        new_node = DoublyLinkedListNode(value)
        new_node.next = next_node
        new_node.prev = next_node.prev
        next_node.prev.next = new_node
        next_node.prev = new_node
        return new_node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key in self.key_count:
            self.key_count[key] += 1
        else:
            self.key_count[key] = 1

        count = self.key_count[key]
        prev_count = count - 1

        if prev_count > 0:
            # Remove the key from the previous count's set
            self.count_key[prev_count].remove(key)
            if not self.count_key[prev_count]:
                # If the set is empty, remove the count from count_key
                del self.count_key[prev_count]

        # Add the key to the current count's set
        if count in self.count_key:
            self.count_key[count].add(key)
        else:
            self.count_key[count] = {key}

        # Update the linked list
        if not self.head.next.value == count:
            self._insert_after(self.head, count)

    def dec(self, key: str) -> None:
        if key not in self.key_count:
            return

        count = self.key_count[key]
        del self.key_count[key]

        if count == 1:
            # Remove the key from the count_key dictionary
            self.count_key[count].remove(key)
            if not self.count_key[count]:
                del self.count_key[count]
        else:
            # Remove the key from the count_key dictionary
            self.count_key[count].remove(key)
            if not self.count_key[count]:
                del self.count_key[count]
            
            # Add the key to the previous count's set
            prev_count = count - 1
            self.count_key[prev_count].add(key)

        if not self.head.next.value == prev_count:
            self._insert_before(self.head.next, prev_count)

    def getMaxKey(self) -> str:
        if self.tail.prev.value == float('-inf'):
            return ""
        return next(iter(self.count_key[self.tail.prev.value]))

    def getMinKey(self) -> str:
        if self.head.next.value == float('inf'):
            return ""
        return next(iter(self.count_key[self.head.next.value]))
