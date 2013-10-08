#!/usr/bin/env python
# coding: utf-8

'''microondas2d.py: demonstração de clousure (este exemplo não funciona)

A classe vazia `Namespace` é usada apenas para criar um objeto mutável 
`ns` com um atributo `tempo` que pode ser acessado e alterado de dentro
das clausuras criadas em torno das múltiplas instâncias da `ajustar`.

Tentativa frustrada usando um atributo na função `ajustar`
'''

from Tkinter import *

def montar_painel(janela):
    visor = Label(janela)
    visor.tempo = 0
    visor['text'] = visor.tempo
    visor.pack()
    for incr in [60, 30, 10]:
        def ajustar():
            print ajustar.incr
            visor.tempo = visor.tempo + ajustar.incr
            visor['text'] = visor.tempo
        ajustar.incr = incr    
        botao = Button(janela, text=incr, command=ajustar)
        botao.pack()

janela = Tk()
montar_painel(janela)
sair = Button(janela, text="Sair", fg="red", command=janela.quit)
sair.pack()
janela.mainloop()

