#!/usr/bin/env python
# coding: utf-8

'''microondas2c.py: demonstração de clousure

Nesta versão a variável tempo é definida no escopo global, e por isso
pode ser acessada e modificada no corpo de `ajustar`, por causa da 
declaração `global incr`.
 
Cada instância da função `ajustar` tem um valor default diferente
para o argumento `incr`. 
'''

from Tkinter import *

janela = Tk()

# montar painel
tempo = 0
visor = Label(janela)
visor['text'] = tempo
visor.pack()
for segundos in [60, 30, 10]:
    def ajustar(incr=segundos):
        global tempo
        print incr
        tempo = tempo + incr
        visor['text'] = tempo
    botao = Button(janela, text=segundos, command=ajustar)
    botao.pack()

sair = Button(janela, text="Sair", fg="red", command=janela.quit)
sair.pack()
janela.mainloop()

