from tkinter import*

def buscar_nome():
    
    nome_inserido = entrada_nome.get()
    nome_formatado = nome_inserido.upper()

    with open('TXT/musicas.txt', 'r', encoding='utf-8') as txt:
        for registro in txt:
            if 'NOME DO ÁLBUM: ' in registro:
                nome_album = registro.split(':')
                nome_albumSeparado = nome_album[1]

                if nome_formatado in nome_albumSeparado and nome_inserido != '':
                    visualizacao_album.insert(END, nome_albumSeparado)

def limpar_visualizacao():
    visualizacao_album.delete(1.0, END)
    entrada_nome.delete (0, 'end')


busca_nome = Tk()

busca_nome.title('Busca de álbuns musicais')
busca_nome.geometry("400x300+10+10")

descricao_janela = Label(busca_nome, text='Busca de álbuns pelo respectivo NOME', fg='black', font='Helvetica, 12')
texto_busca = Label(busca_nome, text='Faça uma busca:')

entrada_nome = Entry()

descricao_janela.place(x=75, y=30)
texto_busca.place(x=146, y=80)
entrada_nome.place(x=130, y=110)

botao_buscarNome = Button(busca_nome, text='Buscar', command=buscar_nome)
botao_buscarNome.place(x=130, y=150)

botao_limparVisualizacao = Button(busca_nome, text='Limpar', command=limpar_visualizacao)
botao_limparVisualizacao.place(x=200, y=150)

visualizacao_album = Text(busca_nome, height=10, width=50)
visualizacao_album.place(x=0, y=200)


busca_nome.mainloop()