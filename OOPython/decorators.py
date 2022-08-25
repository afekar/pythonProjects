def func_show(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'Площадь прямоугольника: {result}')
        return result

    return wrapper


@func_show
def get_sq(width, height):
    return width * height


# task 2

def show_menu(func):
    def wrapper(*args, **kwargs):
        result = func(args[0])
        for i in range(len(result)):
            print(f'{i+1}. {result[i]}')

    return wrapper


@show_menu
def get_menu(s):
    lst = s.strip().split()
    return lst


s = input()
get_menu(s)

#task 3

def sort_list(func):
    def wrapper(*args, **kwargs):
        result = func(args[0])
        result = sorted(result)
        return result

    return wrapper


@sort_list
def get_list(s):
    temp = list(map(int, s.strip().split()))
    return temp


lst = get_list(input())
print(*lst)


#task 4

import sys


def lists2dict(func):
    def wrapper(*args, **kwargs):
        result = func(*args)
        d = {key: value for key, value in zip(*result)}
        return d

    return wrapper


@lists2dict
def conv2lists(x, y):
    return x.split(), y.split()


s1, s2 = input().strip(), input().strip() #map(str.strip, sys.stdin.readlines())
d = conv2lists(s1, s2)
print(*sorted(d.items()))

#task 5

def delete_repeats(func):
    def wrapper(*args, **kwargs):
        result = func(*args)
        while '--' in result:
            result = result.replace('--', '-')
        return result

    return wrapper


@delete_repeats
def convert_str(s):
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
         'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
         'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
         'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
         ' ': '-', '"': '-', ':': '-', ';': '-', '.': '-', ',': '-', '_': '-', '-': '-'}
    temp = ''
    s = s.strip().lower()
    for x in s:
        if x in t.keys():
            temp += t[x]
        else:
            temp += x

    return temp


s = input()
print(convert_str(s))


# TASK 6

def decorator(func, start=5):
    def wrapper(*args, **kwargs):
        result = func(*args)
        result += start
        return result

    return wrapper


@decorator
def get_sum(x):
    *x, = map(int, x.strip().split())
    return sum(x)


s = input()
print(get_sum(s))

#task 7

def make_tag(tag='h1'):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            return f'<{tag}>{result}</{tag}>'
        return wrapper

    return decorator


@make_tag(tag='div')
def get_lower(s):
    s = s.strip().lower()
    return s


x = input()
print(get_lower(x))

#task 8


def change_symbs(chars='!?'):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            temp = ''
            for x in result:
                if x in chars:
                    temp += '-'
                else:
                    temp += x
            result = temp
            while '--' in result:
                result = result.replace('--', '-')
            return result
        return wrapper
    return decorator


@change_symbs(chars='?!:;,. ')
def replace_string(s):
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
         'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
         'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
         'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    s = s.strip().lower()
    temp = ''
    for x in s:
        if x in t.keys():
            temp += t[x]
        else:
            temp += x

    return temp


s = input()
print(replace_string(s))

# task 9

from functools import wraps


def get_sum(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return sum(result)

    return wrapper


@get_sum
def get_list(x):
    """Функция для формирования списка целых значений"""
    *x, = map(int, x.strip().split())
    return x


print(get_list(input()))
print(get_list.__name__, get_list.__doc__)

# task 10