class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def popNode(self, prev, next):
        prev.next = next
        next.prev = prev

    def addNode(self, prev, next, node):
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node


class LRU:
    def __init__(self, size):
        self.size = size
        self.currSize = 0
        self.pageFault = 0
        self.hashmap = dict()
        self.memory = DoublyLinkedList()

    def get(self, value):
        # Cache Hit
        if value in self.hashmap.keys():
            print("Cache Hit!")
            node = self.hashmap[value]
            self.memory.popNode(node.prev, node.next)
            self.memory.addNode(self.memory.tail.prev, self.memory.tail, node)
            return

        # Cache Miss
        if self.currSize == self.size:
            # 가장 오래전에 참조된 페이지를 swap out 시킨다.
            self.pageFault += 1
            currNode = Node(value)
            deleteNode = self.memory.head.next
            self.memory.popNode(deleteNode.prev, deleteNode.next)
            self.memory.addNode(self.memory.tail.prev, self.memory.tail, currNode)
            self.hashmap.pop(deleteNode.value)
            self.hashmap[value] = currNode
            print("Cache Miss!")
            print(f"Change Page into {deleteNode.value} => {currNode.value}")
            return

        # add Page in Memory
        self.currSize += 1
        currNode = Node(value)
        self.memory.addNode(self.memory.tail.prev, self.memory.tail, currNode)
        self.hashmap[value] = currNode
        self.pageFault += 1
        print("Cache Miss!")
        print(f"Add New Page -> {currNode.value}")
        return

    def printNodes(self):
        curr = self.memory.head
        while curr:
            if curr.value != None:
                print(curr.value, end="=> ")
            curr = curr.next
        print()
        print()

    def printPageFault(self):
        print("Page Fault:", self.pageFault)


lru = LRU(3)
data = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
for d in data:
    lru.get(d)
    lru.printNodes()
lru.printPageFault()
