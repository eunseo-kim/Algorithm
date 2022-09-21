import sys

sys.setrecursionlimit(10**6)

preorder = []


def solution(nodeinfo):
    node_numbers = {}
    for i, node in enumerate(nodeinfo, 1):
        node_numbers[" ".join(map(str, node))] = i

    def divide_and_conquer(arr):
        global preorder

        if len(arr) == 0:
            return []

        arr.sort(key=lambda x: x[1])
        root = arr.pop()

        root_node_num = node_numbers[" ".join(map(str, root))]
        preorder.append(root_node_num)

        left_arr, right_arr = [], []
        for node in arr:
            if root[0] < node[0]:
                right_arr.append(node)
            else:
                left_arr.append(node)

        left = divide_and_conquer(left_arr)
        right = divide_and_conquer(right_arr)

        return left + right + [root_node_num]

    postorder = divide_and_conquer(nodeinfo)

    return [preorder, postorder]


result = solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]])
print(result)
