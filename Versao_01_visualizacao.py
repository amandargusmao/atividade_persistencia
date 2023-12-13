from tkinter import *

def func_visualizacao(): #função que mostra na tela o conteúdo do .txt
    txt = open('TXT/musicas.txt', 'r', encoding='utf-8')
    conteudo = txt.read()
    texto.insert(END, conteudo)  


visualizacao = Tk() #tela de visualização

visualizacao.title('Vizualização dos álbuns existentes')
visualizacao.geometry("400x300+10+10")

#Acrescentar um título acima da janela

texto = Text(visualizacao, wrap="word", width=40, height=15)
texto.pack(padx=10, pady=10)

func_visualizacao()


visualizacao.mainloop()
