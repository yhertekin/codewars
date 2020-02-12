"""
The main idea is to count all the occurring characters(UTF-8) in string. If you have string like this aba then the result should be { 'a': 2, 'b': 1 }

What if the string is empty ? Then the result should be empty object literal { }
"""


def count(string):
    el = {}
    for s in string:
        el[s] = el.get(s, 0) + 1
    return el