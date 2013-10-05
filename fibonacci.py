import timeit

# source: http://oeis.org/A000045
fibo_seq = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,
            987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025,
            121393, 196418, 317811, 514229, 832040, 1346269, 2178309,
            3524578, 5702887, 9227465, 14930352, 24157817, 39088169]

from memoizadores import memoizar
from functools import lru_cache

def fibo_rec(n):
    if n < 2:
        return n
    return fibo_rec(n-2) + fibo_rec(n-1)

@memoizar
def fibo_rec_memo(n):
    if n < 2:
        return n
    return fibo_rec(n-2) + fibo_rec(n-1)

@lru_cache
def fibo_rec_lruc(n):
    if n < 2:
        return n
    return fibo_rec(n-2) + fibo_rec(n-1)

def fibo_gen():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b

def fibo_iter(n):
    for i in fibo_gen():
        if n == 0:
            return i
        n -= 1

def fibo_loop(n):
    if n < 2:
        return n
    a, b = 0, 1
    i = 1
    while i < n:
        a, b = b, a + b
        i += 1
    return b

sqrt5 = 5 ** .5

def fibo_calc(n):
    return int(((1+sqrt5)**n - (1-sqrt5)**n) / (2**n * sqrt5))

def test_function(fn):
    for i, n in enumerate(fibo_seq[:30]):
        res = fn(i)
        assert n == res, '%s != %s' % (n, res)
    print('pass', fn.__name__)

def test():
    test_function(fibo_loop)
    test_function(fibo_iter)
    test_function(fibo_calc)
    test_function(fibo_rec)

#test()

def time_function(fn, name=None, start=5, stop=26, step=5):
    if name is None:
        name = fn.__name__
    prep = '\nfrom __main__ import ' + name
    print('%-14s' % name, end='  ')
    for n in range(start, stop, step):
        cmd = '%s(%d)' % (name, n)
        res = timeit.timeit(cmd, prep, number=1000)
        print('%8.4f' % res, end='  ')
    print()

def benchmark():
    time_function(fibo_loop)
    time_function(fibo_iter)
    time_function(fibo_calc)
    time_function(fibo_rec)
    time_function(fibo_rec_memo)
    time_function(fibo_rec_lruc, 'fibo_rec_lruc')

benchmark()
