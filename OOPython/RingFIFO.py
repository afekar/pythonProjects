# -*- coding: utf-8 -*-
from random import choice


class ringFifo:

    def __init__(self, length):
        self.__els = list([None]*length)
        self.__in = 0
        self.__out = 0
        self.__ring_len = length

    def add_elem(self, x):
        if self.__els[self.__in] is not None:
            print 'Буфер переполнен, элемент %s будет заменён на элемент %s' % (self.__els[self.__in], x)
            self.__out = (self.__out + 1) % self.__ring_len
        self.__els[self.__in] = x
        self.__in = (self.__in + 1) % self.__ring_len

    def pop_elem(self):
        if self.__els[self.__out] is not None:
            result = self.__els[self.__out]
            self.__els[self.__out] = None
            self.__out = (self.__out + 1) % self.__ring_len
            return result

    def show(self):
        return self.__els


new_buffer = ringFifo(5)
while True:
    print 'Добавить элемент / извлечь элемент очереди (0/1)?'
    temp = input()
    if temp == 0:
        new_buffer.add_elem(choice('ABCDEFG'))
    elif temp == 1:
        new_buffer.pop_elem()
    print new_buffer.show()
