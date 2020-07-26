import operator
print('Первое')
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for _ in a:
    if _ < 5:
        print(_)
print('Второе')
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = set()
for _ in a:
    for k in b:
        if _ == k:
            c.add(_)
print(c)
print('Третье')
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
resulte = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print(resulte)
print('Четвертое')
dict_a = {1: 10, 2: 20}
dict_b = {3: 30, 4: 40}
dict_c = {5: 50, 6: 60}
result = {}
for d in (dict_a, dict_b, dict_c):
    result.update(d)
print(result)
print('Пятое')