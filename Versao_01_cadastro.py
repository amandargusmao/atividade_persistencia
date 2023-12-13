from tkinter import *

def func_persistencia(entrada):  #função que escreve as entradas no .txt
     registro = open('TXT/musicas.txt', 'a', encoding='utf-8')
     registro.write(entrada.upper())


def func_cadastro(evento): #função que, a partir do clique no botão "cadastrar", itera cada item das caixas de texto chamando a função que escreverá cada um deles no .txt
    lista = {'Nome do álbum: ': str(entrada_album.get()), 'Ano: ': str(entrada_ano.get()), 'Cantor/Banda: ': str(entrada_autoria.get()), 'Foi lançamento do artista/banda? ': str(entrada_lancamento.get())}
    lista_valor = [entrada_album.get(), entrada_ano.get(), entrada_autoria.get(), entrada_lancamento.get()]
    
    for chave, valor in lista.items():
        if '' in lista_valor:
            entrada_album.delete(0, 'end')
            entrada_ano.delete(0, 'end')
            entrada_autoria.delete(0, 'end')
            entrada_lancamento.delete(0, 'end')
            return 
        else:
            func_persistencia(chave)
            func_persistencia(valor)
            func_persistencia('\n')  

    func_persistencia('\n')

    entrada_album.delete(0, 'end')
    entrada_ano.delete(0, 'end')
    entrada_autoria.delete(0, 'end')
    entrada_lancamento.delete(0, 'end')

cadastro = Tk() #tela de cadastro

cadastro.title('Cadastro de álbuns musicais')
cadastro.geometry("400x300+10+10")

album = Label(cadastro, text='Nome do álbum:')
ano = Label(cadastro, text='Ano de lançamento:')
autoria = Label(cadastro, text='Nome do artista/banda:')
lancamento = Label(cadastro, text='Foi o álbum de lançamento da banda/artista?')

entrada_album = Entry()
entrada_ano = Entry()
entrada_autoria = Entry()
entrada_lancamento = Entry()

botao_cadastrar = Button(cadastro, text='Cadastrar')

album.place(x=50, y=30)
ano.place(x=50, y=80)
autoria.place(x=50, y=130)
lancamento.place(x=50, y=180)

entrada_album.place(x=50, y=50)
entrada_ano.place(x=50, y=100)
entrada_autoria.place(x=50, y=150)
entrada_lancamento.place(x=50, y=200)

botao_cadastrar.place(x=50, y=250)

botao_cadastrar.bind('<Button-1>', func_cadastro)

cadastro.mainloop()


'''Melhorias: 

01 - não deixar cadastrar informações repetidas (álbuns iguais)'''