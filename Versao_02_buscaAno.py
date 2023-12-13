import tkinter as tk
from tkinter import ttk

def limpar_visualizacao():
    resultado_text.delete(1.0, tk.END)

def buscar_ano():
    ano_selecionado = int(entrada_ano_combobox.get())
    tipo_selecionado = tipo_var.get()

    with open('TXT/musicas.txt', 'r', encoding='utf-8') as txt:
        
        for registro in txt:

            if 'NOME DO ÁLBUM: ' in registro:
                nome_album = registro.split(':')
                album_formatado = nome_album[1]

            if 'ANO: ' in registro:
                _, valor_ano = registro.split(':')
                ano_album = int(valor_ano)

                if (tipo_selecionado == "Anterior a" and ano_album <= ano_selecionado) or \
                   (tipo_selecionado == "Posterior a" and ano_album >= ano_selecionado) or \
                   (tipo_selecionado == "Igual a" and ano_album == ano_selecionado):
                    resultado_text.insert(tk.END, album_formatado)


busca_ano = tk.Tk()
busca_ano.title("Busca de Álbuns por Ano")

anos = [str(ano) for ano in range(1900, 2031)] 
entrada_ano_combobox = ttk.Combobox(busca_ano, values=anos)
entrada_ano_combobox.set("Selecione o ano")
entrada_ano_combobox.pack(pady=10)


tipo_var = tk.StringVar()
tipo_var.set("Anterior a")  
radiobutton_anterior = tk.Radiobutton(busca_ano, text="Anterior a", variable=tipo_var, value="Anterior a")
radiobutton_posterior = tk.Radiobutton(busca_ano, text="Posterior a", variable=tipo_var, value="Posterior a")
radiobutton_igual = tk.Radiobutton(busca_ano, text="Igual a", variable=tipo_var, value="Igual a")

radiobutton_anterior.pack()
radiobutton_posterior.pack()
radiobutton_igual.pack()

botao_busca = tk.Button(busca_ano, text="Buscar", command=buscar_ano)
botao_busca.pack(pady=10)

resultado_text = tk.Text(busca_ano, height=10, width=50)
resultado_text.pack()

botao_limparVisualizacao = tk.Button(busca_ano, text='Limpar', command=limpar_visualizacao)
botao_limparVisualizacao.pack(pady=10)

busca_ano.mainloop()
