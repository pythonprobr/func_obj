#!/usr/bin/env python
# coding: utf-8

'''saldo.py - Exemplo de função com estado interno

Adaptação do exemplo na p. 241 do livro "Programação em Scheme", 
de João Pavão Martins e Maria dos Remédios Cravo.

O exemplo demonstra o uso de uma clausura para manter estado 
entre invocações sucessivas de uma função.

    >>> conta1 = criar_conta(1000)
    >>> conta2 = criar_conta(500)
    >>> conta1()
    1000
    >>> conta1(100)
    1100
    >>> conta1()
    1100
    >>> conta2(-300)
    200
    >>> conta2(-300)
    Traceback (most recent call last):
      ...
    ValueError: Saldo insuficiente
    >>> conta2()
    200

Obs. Esta versão não funciona!!! É um contra-exemplo didático
'''
# nao funciona!!!
def criar_conta(saldo_inicial):
    saldo = saldo_inicial 
    def conta(movimento=0):
        if (saldo + movimento) < 0:
            raise ValueError('Saldo insuficiente')
        saldo += movimento
        return saldo
    return conta
        
if __name__=='__main__':
    from doctest import testmod
    testmod()        
