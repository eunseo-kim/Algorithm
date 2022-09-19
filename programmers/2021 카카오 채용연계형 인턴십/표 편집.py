class Node:
    def __init__(self, value=None):
        self.prev = None
        self.next = None
        self.value = value


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.curr = self.head

    def insert(self, prev_node, new_node, next_node):
        prev_node.next = new_node
        new_node.prev = prev_node

        new_node.next = next_node
        next_node.prev = new_node

    def delete(self, prev_node, delete_node):
        next_node = delete_node.next

        prev_node.next = next_node
        next_node.prev = prev_node


class TableEditor:
    def __init__(self):
        self.table = DoublyLinkedList()  # doubly linked list
        self.undo = []  # stack에 [prev_node, deleted_node, next_node] 저장
        self.deleted = {}  # { node number: True or False }

    def D(self, value):
        for _ in range(value):
            self.table.curr = self.table.curr.next

    def U(self, value):
        for _ in range(value):
            self.table.curr = self.table.curr.prev

    def C(self):
        delete_node = self.table.curr
        self.deleted[delete_node.value] = True

        prev_node = delete_node.prev
        next_node = delete_node.next

        # table에서 삭제합니다.
        self.table.delete(prev_node, delete_node)

        # 임시 저장소 스택에 삭제 정보를 추가합니다.
        self.undo.append([prev_node, delete_node, next_node])

        # 현재 가리키고 있는 행을 재설정 합니다.
        if next_node.value == None:
            self.table.curr = prev_node
        else:
            self.table.curr = next_node

    def Z(self):
        prev_node, delete_node, next_node = self.undo.pop()
        self.deleted[delete_node.value] = False

        self.table.insert(prev_node, delete_node, next_node)


def solution(n, k, cmd):
    te = TableEditor()

    # initialize table
    curr = te.table.curr
    tail = te.table.tail
    for i in range(n):
        te.deleted[i] = False
        node = Node(i)
        curr.next = node
        node.prev = curr
        curr = node
        if i == k:
            te.table.curr = node
    node.next = tail
    tail.prev = node

    # 표 편집 실행하기
    for command in cmd:
        cur = te.table.head
        input = command.split(" ")
        if input[0] == "D":
            te.D(int(input[1]))
        elif input[0] == "U":
            te.U(int(input[1]))
        elif input[0] == "C":
            te.C()
        elif input[0] == "Z":
            te.Z()

    # 결과 출력하기
    answer = ""
    for i in range(n):
        if te.deleted[i]:
            answer += "X"
        else:
            answer += "O"

    return answer


result = solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"])
print(result)
