class LRUCache:
    # Space: O(n)

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_keys = []
        self.data = {}

    def get(self, key: int) -> int:
        # Time: O(1)
        if key in self.data:
            self.lru_keys.remove(key)
            self.lru_keys.append(key)
            return self.data[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # Time: O(n)
        if key in self.data:
            self.lru_keys.remove(key)
        elif len(self.data) == self.capacity:
            evict_key = self.lru_keys.pop(0)
            self.data.pop(evict_key)
        self.data[key] = value
        self.lru_keys.append(key)
