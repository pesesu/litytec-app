import numpy as np


def reverse(text):
    res = ''
    for char in text:
        res = char + res
    return res


arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])


def rev_while(text):
    res = ''
    size = len(text) - 1

    while size >= 0:
        res += text[size]
        size -= 1
    return res


print(rev_while('Human'))
