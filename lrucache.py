"""
Use doubly linked list to maintain access order and use dictionary to get node in O(1) time
TC: O(1)
SP: O(1)

"""

class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.lrucache = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.count = 0

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev


    def addToHead(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        
    def get(self, key: int) -> int:
        if key not in self.lrucache:
            return -1
        node = self.lrucache[key]
        self.remove(node)
        self.addToHead(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key not in self.lrucache:
            newNode = Node(key, value)
            self.addToHead(newNode)
            self.lrucache[key] = newNode
            self.count+=1
            if self.count>self.capacity:
                del self.lrucache[self.tail.prev.key]
                self.remove(self.tail.prev)
                self.capacity-=1
        else:
            self.lrucache[key].val = value
            self.remove(self.lrucache[key])
            self.addToHead(self.lrucache[key])




        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)