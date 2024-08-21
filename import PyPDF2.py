#instalar biblioteca PyPDF2 (para manipulação de pdf)
import PyPDF2
#import os - é para interagir com o SO (criar arquivos)
import os


juntar = PyPDF2.PdfMerger()

#listar os arquivos no diretorio
lista_arquivos = os.listdir('arquivoo')
#organizar os arquivos = .sort
lista_arquivos.sort()
#mostrar os arquivos
print(lista_arquivos)

#para cada arquivo da minha lista de "arquivoo" ler se é pdf
for arquivo in lista_arquivos:
    if '.pdf' in arquivo:
        juntar.append(f"arquivoo/{arquivo}")

juntar.write('pdf final1.pdf')