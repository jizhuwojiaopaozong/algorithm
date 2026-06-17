from collections import defaultdict

class LinkNode:
    def __init__(self, k, v, next=None, prev=None):
        self.k = k
        self.v = v
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = defaultdict(LinkNode)
        self.r = LinkNode(-1, -1)
        self.l = LinkNode(-1, -1)
        self.l.next = self.r
        self.r.prev = self.l


    def get(self, key: int) -> int:
        if key in self.d:
            self.delete(self.d[key])
            self.insert(self.d[key])
            return self.d[key].v
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key].v = value
            self.delete(self.d[key])
            self.insert(self.d[key])
        else:
            if len(self.d) == self.capacity:
                del self.d[self.r.prev.k]
                self.delete(self.r.prev)
                self.d[key] = LinkNode(key, value)
                self.insert(self.d[key])
            else:
                self.d[key] = LinkNode(key, value)
                self.insert(self.d[key])
    
    def insert(self, n:LinkNode):
        n.prev = self.l
        n.next = self.l.next
        self.l.next.prev = n
        self.l.next = n

    def delete(self, n:LinkNode):
        n.prev.next = n.next
        n.next.prev = n.prev
        


lrucache = LRUCache(2)
lrucache.put(1, 1)
lrucache.put(2, 2)
print(lrucache.get(1))
lrucache.put(3, 3)
print(lrucache.get(2))
lrucache.put(4, 4)
print(lrucache.get(1))
print(lrucache.get(3))
print(lrucache.get(4))