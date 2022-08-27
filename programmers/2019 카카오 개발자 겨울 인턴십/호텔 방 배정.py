import sys

sys.setrecursionlimit(10 ** 6)


def solution(k, room_number):
    def find_empty_room(room):  # 약간 union-find에서 경로 단축과 비슷한 문제
        if room not in rooms:
            rooms[room] = room + 1
            return room

        empty_room = find_empty_room(rooms[room])
        rooms[room] = empty_room + 1
        return empty_room

    answer = []
    rooms = {}

    for room in room_number:
        empty_room = find_empty_room(room)
        answer.append(empty_room)

    return answer


k = 10
room_number = [1, 3, 4, 1, 3, 1]
result = solution(k, room_number)
print(result)
