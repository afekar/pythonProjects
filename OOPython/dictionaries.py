#task1
s = input().split()
s = [x.split('=') for x in s]
values = [int(s[x][1]) for x in range(len(s))]
keys = [s[x][0] for x in range(len(s))]
d = {}
for k, v in zip(keys, values):
    d[k] = v
print(*sorted(d.items()))

#task2
import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
d = {}
lst = [x.split('=') for x in lst_in]
keys = [int(lst[x][0]) for x in range(len(lst))]
values = [lst[x][1] for x in range(len(lst))]
for k, v in zip(keys, values):
    d[k] = v
print(*sorted(d.items()))


#task 3
keys_possible = ['house', 'True', '5']
s = input().split()
s = [x.split('=') for x in s]
keys = [s[x][0] for x in range(len(s))]
values = [s[x][1] for x in range(len(s))]
d = {}
for k, v in zip(keys, values):
    d[k] = v
flag = 0
for x in keys_possible:
    if x not in d.keys():
        flag = 1
        break
print(['ДА', 'НЕТ'][flag])

#task4

s = input().split()
s = [x.split('=') for x in s]
d = dict(s)
keys_del = ['False', '3']
for x in keys_del:
    if x in d.keys():
        d.pop(x)
print(*sorted(d.items()))

#task 5

s = input().split()
keys, values = [x[:2] for x in s], s
d = {}
for k, v in zip(keys, values):
    if k in d.keys():
        d[k].append(v)
    else:
        d[k] = [v]

print(*sorted(d.items()))

#task 6

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = [x.split() for x in lst_in]
for i in range(len(lst_in)):
    lst_in[i][0], lst_in[i][1] = lst_in[i][1], lst_in[i][0]

d = {}
for i in range(len(lst_in)):
    k, v = lst_in[i][0], lst_in[i][1]
    if k in d.keys():
        d[k].append(v)
    else:
        d[k] = [v]

print(*sorted(d.items()))

#task 7

from math import sqrt
d = {}
while True:
    key = int(input())
    if key == 0:
        break
    if key in d.keys():
        print(f'значение из кэша: {d[key]}')
    else:
        d[key] = round(sqrt(key), 2)
        print(d[key])


#task 8

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
d = {}
for x in lst_in:
    if x in d.keys():
        print(f'Взято из кэша: HTML-страница для адреса {d[x]}')
    else:
        d[x] = x
        print(f'HTML-страница для адреса {d[x]}')

#task 9

morze = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.', 'ж': '...-', 'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.', 'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----', 'щ': '--.-', 'ъ': '--.--', 'ы': '-.--', 'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-', ' ': '-...-'}
d = dict(morze)
s = input().split()
temp = ''
reversed_morze = dict(zip(morze.values(), morze.keys()))
for x in s:
    temp += reversed_morze[x]
temp = temp.strip()
print(temp)


#task 10

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
d = {}
for x in lst_in:
    k, v = x.split()
    if k in d.keys():
        d[k].append(v)
    else:
        d[k] = [v]
for k in d.keys():
    temp = ', '.join(d[k])
    print(f'{k}: {temp}')

#task 11

from collections import OrderedDict

things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}

equip = {}
n = float(input()) * 1000
sorted_dict = {}
sorted_keys = sorted(things, key=things.get)
for w in sorted_keys:
    sorted_dict[w] = things[w]

sorted_dict = OrderedDict(reversed(list(sorted_dict.items())))
while True:
    temp = [k for k, v in sorted_dict.items() if v < n]
    i = 0
    while i < len(temp):
        if temp[i] in equip.keys():
            temp.remove(temp[i])
            i -= 1
        i += 1
    if not temp:
        break
    else:
        for x in temp:
            if x not in equip.keys() and sorted_dict[x] <= n:
                equip[x] = x
                n -= sorted_dict[x]
print(*equip.values())

# task 12

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
tp = tuple(tuple(map(lambda x: x.split('='), [x for x in lst_in])))
tp = {key: value for key, value in (filter(lambda x: x if int(x[1]) >= 500 else None, [x for x in tp]))}
print(*tp.keys())

#task 13

import sys


def sort_army(lst):
    res = {}
    lst = {key: value for key, value in [x for x in lst]}
    tmp = 'рядовой,сержант,старшина,прапорщик,лейтенант,капитан,майор,подполковник,полковник'.split(',')
    for i in lst.keys():
        lst[i] = tmp.index(lst[i])

    sorted_keys = sorted(lst, key=lst.get)
    for k in sorted_keys:
        res[k] = tmp[lst[k]]
    res = [list(x) for x in res.items()]
    return res


lst_in = list(map(str.strip, sys.stdin.readlines()))
temp = [x.split('=') for x in lst_in]
lst = sort_army(temp)