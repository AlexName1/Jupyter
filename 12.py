users = [
    {"id": 0, "name": "Алексей"},
    {"id": 1, "name": "Петр"},
    {"id": 2, "name": "Александр"},
    {"id": 3, "name": "Сергей"},
    {"id": 4, "name": "Катя"},
    {"id": 5, "name": "Владимир"},
    {"id": 6, "name": "Аня"},
    {"id": 7, "name": "Дмитрий"},
    {"id": 8, "name": "Ирина"},
    {"id": 9, "name": "Дарья"},
    {"id": 10, "name": "Женя"}
]

fp = [(0, 1), (0, 2), (1, 2), (1, 3), (3, 4),
      (4, 5), (4, 10), (5, 6), (5, 7), (5, 8), (6, 8), (7, 8), (8, 9), (10, 2), (10, 6)]

friendships = {user["id"]: [] for user in users}

for i, j in fp:
    friendships[i].append(j)  # Добавить j как друга для i
    friendships[j].append(i)  # Добавить i как друга ДЛЯ j


def number_of_friends(u):
    id = u['id']
    friend_ids = friendships[id]
    return len(friend_ids)


num_friends_by_name = []

for i in users:
    user = (i["name"], number_of_friends(i))
    num_friends_by_name.append(user)

pass
num_friends_by_name.sort(key=lambda x: x[1], reverse=False)

pass
