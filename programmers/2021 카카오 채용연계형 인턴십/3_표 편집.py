from collections import deque


class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
        self.deleted = False


def solution(n, k, cmd):
    node_list = [Node(i) for i in range(n)]
    for i in range(n - 1):
        node_list[i].next = node_list[i + 1]
        node_list[i + 1].prev = node_list[i]

    history = deque()

    curr = node_list[k]

    for s in cmd:
        if s[0] == "C":
            curr.deleted = True
            history.append(curr)

            prev = curr.prev
            next = curr.next

            if prev:
                prev.next = next

            if next:
                next.prev = prev
                curr = next
            else:
                curr = prev

        elif s[0] == "Z":
            node = history.pop()
            prev = node.prev
            next = node.next

            if prev:
                prev.next = node
            if next:
                next.prev = node
            node.deleted = False
        else:
            s1, s2 = s.split(" ")
            if s1 == "D":
                num = int(s2)
                for _ in range(num):
                    curr = curr.next
            else:
                num = int(s2)
                for _ in range(num):
                    curr = curr.prev

    answer = ""
    for node in node_list:
        if node.deleted:
            answer += "X"
        else:
            answer += "O"

    return answer


cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
print(solution(8, 2, cmd))