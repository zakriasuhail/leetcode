class Node:
    def __init__(self, key, val):
        self.key = key 
        self.val = val
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.mru, self.lru = Node(-1,-1), Node(-1,-1)

        # connect linked list
        self.lru.next = self.mru
        self.mru.prev = self.lru
    
    # remove node from anywhere
    def remove(self, node):
        prv = node.prev
        nxt = node.next
        prv.next = nxt
        nxt.prev = prv
        

    # insert node at mru
    def insert(self, node):  
        prev = self.mru.prev
        prev.next = node
        node.prev = prev
        node.next = self.mru
        self.mru.prev = node
        

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        # remove current node in list
        if key in self.map:
            self.remove(self.map[key])

        # add/update value
        self.map[key] = Node(key, value)

        # update position
        self.insert(self.map[key])


        # if cap has reached
        if len(self.map) > self.cap:
            node = self.lru.next
            self.remove(self.lru.next)
            del self.map[node.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)