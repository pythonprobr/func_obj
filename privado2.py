"""
    >>> a = Aluno('Juca',7,'abc123')
    >>> a.nome
    'Juca'
    >>> a.nota
    Traceback (most recent call last):
       ...
    AttributeError: 'Aluno' object has no attribute 'nota'
    >>> a.get_nota()
    Traceback (most recent call last):
       ...
    AttributeError: Acesso negado: senha incorreta
    >>> a.get_nota('abc123')
    7
    >>> a.set_nota(9, 'xyz789')
    >>> a.get_nota('abc123')
    Traceback (most recent call last):
       ...
    AttributeError: Acesso negado: senha incorreta
    >>> a.get_nota('xyz789')
    9

"""


class Aluno(object):
    def __init__(self, nome, nota, senha):
        self.nome = nome
        self.set_nota(nota, senha)

    def set_nota(self, nota, senha_inicial):
        def guarda_nota(senha=None):
            if senha==senha_inicial:
                return nota
            else:
                raise AttributeError('Acesso negado: senha incorreta')
        self.get_nota = guarda_nota

import doctest
doctest.testmod()

