import functools

def memoizar(func):
    cache = {}

    @functools.wraps(func)
    def memoizada(*args, **kwargs):
        chave = (args, str(kwargs))
        if chave not in cache:
            cache[chave] = func(*args, **kwargs)
        return cache[chave]

    return memoizada
