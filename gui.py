from tkinter import *
import tkinter as tk
from tkinter import ttk
import domain

def fazer_cadastro():

    def limpar_caixas_texto():
        entrada_album.delete(0, 'end')
        entrada_ano.delete(0, 'end')
        entrada_autoria.delete(0, 'end')
        entrada_lancamento.delete(0, 'end')

    cadastro = Tk() 
    cadastro.title('Cadastro de álbuns musicais')
    cadastro.geometry("400x300+10+10")

    album = Label(cadastro, text='Nome do álbum:')
    ano = Label(cadastro, text='Ano de lançamento:')
    autoria = Label(cadastro, text='Nome do artista/banda:')
    lancamento = Label(cadastro, text='Foi o álbum de lançamento da banda/artista?')

    entrada_album_var = StringVar()
    entrada_ano_var = StringVar()
    entrada_autoria_var = StringVar()
    entrada_lancamento_var = StringVar()

    entrada_album = Entry(cadastro, textvariable=entrada_album_var)
    entrada_ano = Entry(cadastro, textvariable=entrada_ano_var)
    entrada_autoria = Entry(cadastro, textvariable=entrada_autoria_var)
    entrada_lancamento = Entry(cadastro, textvariable=entrada_lancamento_var)

    botao_cadastrar = Button(cadastro, text='Cadastrar', command=lambda: domain.func_cadastro(
        entrada_album.get(),
        entrada_ano.get(),
        entrada_autoria.get(),
        entrada_lancamento.get(),
        limpar_caixas_texto
    ))

    album.place(x=50, y=30)
    ano.place(x=50, y=80)
    autoria.place(x=50, y=130)
    lancamento.place(x=50, y=180)

    entrada_album.place(x=50, y=50)
    entrada_ano.place(x=50, y=100)
    entrada_autoria.place(x=50, y=150)
    entrada_lancamento.place(x=50, y=200)

    botao_cadastrar.place(x=50, y=250)

    cadastro.mainloop()


def visualizar_registros(): #Função de interface gráfica que contém a tela de visualização de registros

    visualizacao = Tk()

    visualizacao.title('Vizualização dos álbuns existentes')
    visualizacao.geometry("400x300+10+10")

    #Acrescentar um título acima da janela

    texto = Text(visualizacao, wrap="word", width=40, height=15)
    texto.pack(padx=10, pady=10)

    domain.func_visualizacao(texto)


    visualizacao.mainloop()


def buscar_por_ano(): #Função de interface gráfica que contém a tela de busca de registro filtrando por ano

    busca_ano = tk.Tk()
    busca_ano.title("Busca de Álbuns por Ano")

    tipo_var = tk.StringVar()
    tipo_var.set("Anterior a")  

    anos = [str(ano) for ano in range(1900, 2031)] 
    entrada_ano_combobox = ttk.Combobox(busca_ano, values=anos)
    entrada_ano_combobox.set("Selecione o ano")
    entrada_ano_combobox.pack(pady=10)

    
    radiobutton_anterior = tk.Radiobutton(busca_ano, text="Anterior a", variable=tipo_var, value="Anterior a")
    radiobutton_posterior = tk.Radiobutton(busca_ano, text="Posterior a", variable=tipo_var, value="Posterior a")
    radiobutton_igual = tk.Radiobutton(busca_ano, text="Igual a", variable=tipo_var, value="Igual a")

    radiobutton_anterior.pack()
    radiobutton_posterior.pack()
    radiobutton_igual.pack()

    resultado_text = tk.Text(busca_ano, height=10, width=50)
    resultado_text.pack()


    botao_busca = tk.Button(busca_ano, text="Buscar", command=lambda: domain.buscar_ano(
    entrada_ano_combobox.get(),
    tipo_var.get(),
    resultado_text
))
    botao_busca.pack(pady=10)

 
    #botao_limparVisualizacao = tk.Button(busca_ano, text='Limpar', command=domain.limpar_visualizacao_ano)
    #botao_limparVisualizacao.pack(pady=10)

    busca_ano.mainloop()


def buscar_por_nome(): #Função de interface gráfica que contém a tela de busca de registro filtrando por nome

    busca_nome = Tk()

    busca_nome.title('Busca de álbuns por nome')
    busca_nome.geometry("400x300+10+10")

    #descricao_janela = Label(busca_nome, text='Busca de álbuns pelo respectivo NOME', fg='black', font='Helvetica, 12')
    texto_busca = Label(busca_nome, text='Faça uma busca:')

    entrada_nome_var = StringVar()

    entrada_nome = Entry(busca_nome, textvariable=entrada_nome_var)

    #descricao_janela.place(x=75, y=30)
    texto_busca.place(x=146, y=80)
    entrada_nome.place(x=130, y=110)

    botao_buscarNome = Button(busca_nome, text='Buscar', command=domain.buscar_nome(entrada_nome.get(), visualizacao_album=INSERT))
    botao_buscarNome.place(x=130, y=150)

    #botao_limparVisualizacao = Button(busca_nome, text='Limpar', command=domain.limpar_visualizacao_nome)
    #botao_limparVisualizacao.place(x=200, y=150)

    visualizacao_album = Text(busca_nome, height=10, width=50)
    visualizacao_album.place(x=0, y=200)


    busca_nome.mainloop()


def menu_inicial():

    menu = Tk()

    menu.title('Menu Principal')
    menu.geometry("300x200+10+10")

    botao_cadastro = Button(menu, text='Fazer Cadastro', command=fazer_cadastro)
    botao_cadastro.pack(pady=10)

    botao_visualizacao = Button(menu, text='Visualizar Registros', command=visualizar_registros)
    botao_visualizacao.pack(pady=10)

    botao_busca_ano = Button(menu, text='Buscar por Ano', command=buscar_por_ano)
    botao_busca_ano.pack(pady=10)

    botao_busca_nome = Button(menu, text='Buscar por Nome', command=buscar_por_nome)
    botao_busca_nome.pack(pady=10)

    menu.mainloop()

if __name__ == "__main__":
    menu_inicial()
