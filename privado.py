"""
    >>> a = Aluno('Juca',7)
    >>> a.nome
    'Juca'
    >>> a.nota
    Traceback (most recent call last):
       ...
    AttributeError: 'Aluno' object has no attribute 'nota'
    >>> a.get_nota()
    Traceback (most recent call last):
       ...
    AttributeError: Acesso negado
    >>> a.get_nota('segredo')
    7

"""


class Aluno(object):
    def __init__(self, nome, nota):
        self.nome = nome
        self.set_nota(nota)

    def set_nota(self, nota):
        def guarda_nota(senha=None):
            if senha=='segredo':
                return nota
            else:
                raise AttributeError('Acesso negado')
        self.get_nota = guarda_nota

import doctest
doctest.testmod()

