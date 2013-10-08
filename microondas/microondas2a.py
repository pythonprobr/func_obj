#!/usr/bin/env python
# coding: utf-8

'''microondas2a.py: demonstração de clousure

A classe vazia `Namespace` é usada apenas para criar um objeto mutável 
`ns` com um atributo `tempo` que pode ser acessado e alterado de dentro
das clausuras criadas em torno das múltiplas instâncias da `ajustar`.

Cada instância da função `ajustar` tem um valor default diferente
para o argumento `incr`. 
'''

from Tkinter import *

class Namespace(object):
    pass

def montar_painel(janela):
    ns = Namespace()
    ns.tempo = 0
    visor = Label(janela)
    visor['text'] = ns.tempo
    visor.pack()
    for segundos in range(0, 100, 10):
        def ajustar(incr=segundos):
            print incr
            ns.tempo = ns.tempo + incr
            visor['text'] = ns.tempo
        botao = Button(janela, text=segundos, command=ajustar)
        botao.pack()

janela = Tk()
montar_painel(janela)
sair = Button(janela, text="Sair", fg="red", command=janela.quit)
sair.pack()
janela.mainloop()

