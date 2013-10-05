#!/usr/bin/env python
# coding: utf-8

'''microondas2f.py: demonstração de clousure

Neste exemplo a variável `tempo` é um atributo da instância de `Microondas`.

Cada instância da função `ajustar` tem um valor default diferente
para o argumento `incr`. 
'''

from Tkinter import *

class Microondas(object):
    def __init__(self, janela):
        self.janela = janela
        self.tempo = 0
        self.montar_painel()
        sair = Button(janela, text="Sair", fg="red", command=janela.quit)
        sair.pack()

    def montar_painel(self):
        visor = Label(self.janela)
        visor['text'] = self.tempo
        visor.pack()
        for segundos in [60, 30, 10]:
            def ajustar(incr=segundos):
                print incr
                self.tempo = self.tempo + incr
                visor['text'] = self.tempo
            botao = Button(self.janela, text=segundos, command=ajustar)
            botao.pack()

microondas = Microondas(Tk())
microondas.janela.mainloop()

