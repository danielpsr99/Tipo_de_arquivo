import os

lista_de_arquivos = os.listdir('./Dowload') # pegando todos os arquivos da pasta dos json

for arquivo in lista_de_arquivos: # percorrendo a variavel
    with open(f"{arquivo}", "w", encoding="ANSI") as arq:
        os.rename('./Dowload','./Dowload')
