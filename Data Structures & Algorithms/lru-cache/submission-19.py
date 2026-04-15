class ListNode:
    def __init__(self, key = -1, val = -1, next: ListNode = None, prev: ListNode = None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.map.get(key) if key in self.map else None
        if node:
            self.moveNodeToHead(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].val = value
            self.moveNodeToHead(self.map[key])
        else:
            node = ListNode(key, value)
            self.map[key] = node
            self.moveNodeToHead(node)
        
        if len(self.map) > self.capacity:
            self.removeLastNode()
    
    def moveNodeToHead(self, node: ListNode) -> None:
        if (node.next and node.prev):
            node.prev.next = node.next
            node.next.prev = node.prev
            
        temp = self.head.next
        self.head.next = node
        node.next = temp
        temp.prev = node
        node.prev = self.head
        print(self.head.next.key, self.tail.prev.key)

    def removeLastNode(self) -> None:
        last = self.tail.prev
        print(f"removing last node {last.key}")

        temp = last.prev
        temp.next = self.tail
        self.tail.prev = temp

        last.next = last.prev = None
        del self.map[last.key]
        print(f"new last node key: {self.tail.prev.key}")


