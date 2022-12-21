# 6. Друзья друзей

friends_pair = input()
dic_friends = dict()

while friends_pair != '':
    friends = friends_pair.split()
    if friends[0] not in dic_friends.keys():
        dic_friends[friends[0]] = {friends[1]}
    else:
        dic_friends[friends[0]].add(friends[1])

    if friends[1] not in dic_friends.keys():
        dic_friends[friends[1]] = {friends[0]}
    else:
        dic_friends[friends[1]].add(friends[0])

    friends_pair = input()

dic_result = {i: set() for i in dic_friends.keys()}

for i in dic_friends.keys():
    for j in dic_friends[i]:
        temp = dic_friends[j].copy()
        temp.discard(i)
        temp.difference_update(dic_friends[i])
        dic_result[i] = dic_result[i].union(temp)


for i in sorted(dic_result):
    print(f"{i}: {', '.join(sorted(dic_result[i]))}")

# Васильев: Иванов, Кириллов, Яковлев
# Иванов: Васильев, Кириллов, Яковлев
# Кириллов: Васильев, Иванов, Яковлев
# Петров: Сергеев
# Сергеев: Петров
# Яковлев: Васильев, Иванов, Кириллов
