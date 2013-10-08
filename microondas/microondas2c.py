#!/usr/bin/env python
# coding: utf-8

'''microondas2c.py: demonstração de clousure

A classe vazia `Namespace` é usada apenas para criar um objeto mutável 
`ns` com um atributo `tempo` que pode ser acessado e alterado de dentro
das clausuras criadas em torno das múltiplas instâncias da `ajustar`.

As clausuras criadas para as diferente instâncias da função `ajustar` têm
valores diferentes de `incr` em seus ambientes. 
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
    for segundos in [60, 30, 10]:
        def ajustador(incr):
            def ajustar():
                print incr
                ns.tempo = ns.tempo + incr
                visor['text'] = ns.tempo
            return ajustar
        botao = Button(janela, text=segundos, command=ajustador(segundos))
        botao.pack()

janela = Tk()
montar_painel(janela)
sair = Button(janela, text="Sair", fg="red", command=janela.quit)
sair.pack()
janela.mainloop()

