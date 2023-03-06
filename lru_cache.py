class Node:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.items = {}
        self.capacity = capacity
        self.older = None
        self.newer = None

    def _to_front(self, node):
        if len(self.items) == 1:
            return

        if self.newer is node:
            return

        if node.prev:
            node.prev.next = node.next
        else:
            self.older = node.next

        node.next.prev = node.prev

        self.newer.next = node
        node.next = None
        node.prev = self.newer
        self.newer = node

    def get(self, key: int) -> int:
        node = self.items.get(key)

        if not node:
            return -1

        self._to_front(node)

        #print("getting", key)
        #self.print()
        return node.val
        

    def put(self, key: int, value: int) -> None:
        curr_node = self.items.get(key)

        if curr_node:
            curr_node.val = value

            self._to_front(curr_node)

            #print("updateing", key)
            #self.print()
            
            return

        node = Node(key, value)

        if self.newer:
            node.prev = self.newer
            self.newer.next = node

        self.newer = node

        self.items[key] = node

        if not self.older:
            self.older = node

        if len(self.items) > self.capacity:
            del self.items[self.older.key]
            

            self.older = self.older.next
            self.older.prev = None

        #print("putting", key)
        #self.print()


    

    def print(self):
        return
        head = self.older
        while head:
            print(head.key, end=",")
            head = head.next
        print()
        
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.values = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.values:
            value = self.values[key]
            self.values.move_to_end(key)
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.values:
            self.values[key] = value
            self.values.move_to_end(key)
        else:
            if self.capacity == len(self.values):
                self.values.popitem(last=False)
            
            self.values[key] = value
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
