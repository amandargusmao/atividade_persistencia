import db
import gui


def func_cadastro(nome_album, ano, autoria, lancamento, limpar_caixas_texto):
    lista = {'Nome do álbum: ': str(nome_album), 'Ano: ': str(ano), 'Cantor/Banda: ': str(autoria), 'Foi lançamento do artista/banda? ': str(lancamento)}
    lista_valor = [nome_album, ano, autoria, lancamento]

    for chave, valor in lista.items():
        if '' in lista_valor:
            return
        else:
            db.func_persistencia(chave)
            db.func_persistencia(valor)
            db.func_persistencia('\n')

    db.func_persistencia('\n')
    limpar_caixas_texto()



def func_visualizacao(texto): #função que mostra na tela o conteúdo do .txt
    txt = open('TXT/musicas.txt', 'r', encoding='utf-8')
    conteudo = txt.read()
    texto.insert(gui.END, conteudo)  


def buscar_ano(ano_selecionado, tipo_selecionado, resultado_text):
    ano_selecionado = int(ano_selecionado)

    with open('TXT/musicas.txt', 'r', encoding='utf-8') as txt:
        registros = txt.readlines()
        for i, registro in enumerate(registros):
            if 'NOME DO ÁLBUM: ' in registro:
                nome_album = registro.split(':')
                album_formatado = nome_album[1].strip()

            if 'ANO: ' in registro:
                _, valor_ano = registro.split(':')
                ano_album = int(valor_ano)

                if tipo_selecionado == "Anterior a" and ano_album >= ano_selecionado:
                    continue

                if tipo_selecionado == "Posterior a" and ano_album <= ano_selecionado:
                    continue

                if tipo_selecionado == "Igual a" and ano_album != ano_selecionado:
                    continue

                resultado_text.insert(gui.tk.END, f"{album_formatado} ({ano_album})\n")

def limpar_visualizacao_ano():
    gui.resultado_text.delete(1.0, gui.tk.END)


def buscar_nome(entrada_nome, visualizacao_album):
    
    #nome_inserido = gui.entrada_nome.get()
    nome_formatado = entrada_nome.upper()

    with open('TXT/musicas.txt', 'r', encoding='utf-8') as txt:
        registros = txt.readlines()
        for registro in registros:
            if 'NOME DO ÁLBUM: ' in registro:
                nome_album = registro.split(':')
                nome_albumSeparado = nome_album[1]

                if nome_formatado in nome_albumSeparado and entrada_nome != '':
                    gui.visualizacao_album.insert(gui.END, registros)

def limpar_visualizacao_nome():
    gui.visualizacao_album.delete(1.0, gui.END)
    gui.entrada_nome.delete (0, 'end')