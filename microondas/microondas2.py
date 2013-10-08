#!/usr/bin/env python
# coding: utf-8

'''microondas2.py: demonstração de clousure (este exemplo não funciona)

Este exemplo mostra o problema: a variável `tempo` definida no corpo de
`montar_painel` não pode ser alterada dentro de `ajustar`. O erro é:

UnboundLocalError: local variable 'tempo' referenced before assignment

As variações deste arquivo demonstram formas diferentes de resolver o
problema. 

Os exemplos também mostram formas diferentes de passagem do valor do 
incremento `incr` para função `ajustar`.
'''

from Tkinter import *

def montar_painel(janela):
    tempo = 0
    visor = Label(janela)
    visor['text'] = tempo
    visor.pack()
    for segundos in [60, 30, 10]:
        def ajustar(incr=segundos):
            print incr
            tempo = tempo + incr # UnboundLocalError!!!
            visor['text'] = tempo
        botao = Button(janela, text=segundos, command=ajustar)
        botao.pack()

janela = Tk()
montar_painel(janela)
sair = Button(janela, text="Sair", fg="red", command=janela.quit)
sair.pack()
janela.mainloop()

