import sys

input = sys.stdin.readline


class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, value):
        self.stack.append(value)
        self.size += 1

    def pop(self):
        if self.empty():
            print(-1)
        else:
            self.size -= 1
            print(self.stack.pop())

    def empty(self):
        if self.size == 0:
            return True
        return False

    def top(self):
        if self.empty():
            print(-1)
        else:
            print(self.stack[-1])

    def get_size(self):
        print(self.size)


#
stack = Stack()
for _ in range(int(input())):
    cmd = list(input().strip().split(" "))
    if cmd[0] == "push":
        stack.push(int(cmd[1]))
    elif cmd[0] == "pop":
        stack.pop()
    elif cmd[0] == "size":
        stack.get_size()
    elif cmd[0] == "empty":
        print(int(stack.empty()))
    elif cmd[0] == "top":
        stack.top()
