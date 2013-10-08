#!/usr/bin/env python3.0

'''microondas3b.py: demonstração de clousure

Na função `ajustar` a declaração `nonlocal tempo` permite que a variável
`tempo` definida no corpo de `montar_painel` seja acessada e alterada.
Obs: `nonlocal` é uma palavra reservada introduzida no Python 3.0.

Cada instância da função `ajustar` tem um valor default diferente
para o argumento `incr`. 
'''

from tkinter import *

def montar_painel(janela):
    tempo = 0
    visor = Label(janela)
    visor['text'] = tempo
    visor.pack()
    for segundos in [60, 30, 10]:
        def ajustar(incr=segundos):
            nonlocal tempo
            print(incr)
            tempo = tempo + incr
            visor['text'] = tempo
        botao = Button(janela, text=segundos, command=ajustar)
        botao.pack()

janela = Tk()
montar_painel(janela)
sair = Button(janela, text="Sair", fg="red", command=janela.quit)
sair.pack()
janela.mainloop()

