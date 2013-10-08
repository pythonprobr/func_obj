#!/usr/bin/env python
# coding: utf-8

'''microondas2b.py: demonstração de clousure (este exemplo não funciona)

A classe vazia `Namespace` é usada apenas para criar um objeto mutável 
`ns` com um atributo `tempo` que pode ser acessado e alterado de dentro
das clausuras criadas em torno das múltiplas instâncias da `ajustar`.

As clausuras de `ajustar` não capturam os valores de `incr` no momento das
definições das funções. Quando `ajustar` é invocado, o valor é sempre 10. 
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
    for incr in [60, 30, 10]:
        def ajustar():
            print incr
            ns.tempo = ns.tempo + incr
            visor['text'] = ns.tempo
        botao = Button(janela, text=incr, command=ajustar)
        botao.pack()

janela = Tk()
montar_painel(janela)
sair = Button(janela, text="Sair", fg="red", command=janela.quit)
sair.pack()
janela.mainloop()

