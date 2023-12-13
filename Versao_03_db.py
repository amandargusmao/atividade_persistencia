def func_persistencia(entrada):  #função que escreve as entradas no .txt
     registro = open('TXT/musicas.txt', 'a', encoding='utf-8')
     registro.write(entrada.upper())