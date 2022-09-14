#task 1
def get_sum(n):
    a, b, c = 1, 1, 1
    for i in range(n):
        if i < 3:
            yield a
        else:
            a, b, c = b, c, a+b+c
            yield c


N = int(input())
[print(i, end=' ') for i in get_sum(N)]

#task 2

from string import ascii_lowercase, ascii_uppercase
import random

random.seed(1)


def rand_passwd(n):
    chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
    while True:
        temp = ''
        for i in range(n):
            indx = random.randint(0, len(chars))
            temp += chars[indx]
        yield temp


N = int(input())
gen = rand_passwd(N)
[print(next(gen)) for i in range(5)]


#task 3
from string import ascii_lowercase, ascii_uppercase
import random


random.seed(1)
def rand_email(n):
    chars = ascii_lowercase + ascii_uppercase
    while True:
        temp = ''
        for i in range(n):
            indx = random.randint(0, len(chars))
            temp += chars[indx]
        yield temp+'@mail.ru'


N = int(input())
gen = rand_email(N)
[print(next(gen)) for i in range(5)]


# task 4
def get_simples(x):
    k = 0
    current = 2
    flag = True
    while k < 20:
        flag = True
        test = 2
        while test < current:
            if current % test == 0:
                flag = False
                break
            test += 1
        if flag is True:
            yield current
        else:
            k -= 1
        k += 1
        current += 1


N = int(input())
gen = get_simples(N)
[print(next(gen), end=' ') for i in range(N)]

#zip
cities = input().split()
n = 3
for row in zip(*[iter(cities)]*n):
    print(*row)