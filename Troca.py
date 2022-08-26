import os
import encodings
lista_de_arquivos = os.listdir('./Dowload') # pegando todos os arquivos da pasta dos json
print(lista_de_arquivos)
for arquivo in lista_de_arquivos: # percorrendo a variavel
    print(arquivo)
    with open(f"./Dowload/{arquivo}", encoding="ANSI") as arq:
        n = arq.read()
        n1 = n.encode('ANSI')
        with open(f'./Dowload/{arquivo}', 'wb') as n3:
            n3.write(n1)
        print(encodings.detect(n3))