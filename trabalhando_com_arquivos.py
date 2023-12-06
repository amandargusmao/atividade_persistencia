def leitura():
    arquivo = open('meu_nome.txt', 'r', encoding='utf-8')
    nomes = arquivo.read()
    lista = nomes.split('|')
    for nome in lista:
        print(nome)


def escrita(entrada):
    arquivo = open('meu_nome.txt', 'a', encoding='utf-8')
    separador = '|'
    arquivo.write(separador)
    arquivo.write(entrada)
   

def cadastro():
    while True:

        nome = input('Nome: ')

        if nome == '0':
            break

        idade = input('Idade: ')
        genero = input('Gênero (F, M ou O): ').upper()

        while genero != 'F' and genero != 'M' and genero != 'O':
            genero = input('\nDigite uma opção válida: \n\nF - feminino\nM - masculino\nO - outro\n\nSua resposta: ').upper()

        telefone = input('Telefone: ')

        lista_entrada = [nome, idade, genero, telefone, "\n"]

        for item in lista_entrada:
            registro = item
            escrita(registro)


def main():
    cadastro()
    leitura()


main()