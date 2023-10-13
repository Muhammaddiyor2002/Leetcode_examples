import collections

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_value = {}  # Dictionary to store key-value pairs
        self.key_count = {}  # Dictionary to store key-use count
        self.use_keys = collections.defaultdict(collections.OrderedDict)  # Dictionary of ordered dictionaries for each use count
        self.min_count = 0

    def get(self, key: int) -> int:
        if key not in self.key_value:
            return -1

        # Update use count for the key
        self.key_count[key] += 1

        # Move the key to the next use count
        use_count = self.key_count[key]
        self.use_keys[use_count][key] = self.use_keys[use_count - 1].pop(key)

        # If the previous use count dictionary is empty and it's the min_count, update min_count
        if not self.use_keys[self.min_count]:
            self.min_count += 1

        return self.key_value[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        # If the key exists, update its value and call get to increase its use count
        if key in self.key_value:
            self.key_value[key] = value
            self.get(key)
            return

        # If we've reached the capacity, evict the least frequently used key
        if len(self.key_value) >= self.capacity:
            # Get the least frequently used key from the current min_count
            evicted_key, _ = self.use_keys[self.min_count].popitem(last=False)
            del self.key_value[evicted_key]
            del self.key_count[evicted_key]

        # Add the new key-value pair with a use count of 1
        self.key_value[key] = value
        self.key_count[key] = 1
        self.use_keys[1][key] = key
        self.min_count = 1
