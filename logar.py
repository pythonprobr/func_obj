from time import strftime

def logar(func):
    def logadora(*args, **kwargs):
        res = func(*args, **kwargs)
        print(strftime('%H:%M:%S.%m'), args, kwargs, '->', res)
        return res
    return logadora

@logar
def dobro(n):
    return n*2
