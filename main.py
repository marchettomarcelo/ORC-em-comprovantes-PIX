from descobrir_origem import *
from descobrir_valor import *
from os import listdir
from os.path import isfile, join
from PIL import Image


def main():
    nomes_arquivos_comprovantes = [f for f in listdir("comprovantes") if isfile(join("comprovantes", f))]

    origem_valor = []

    for nome_arquivo in nomes_arquivos_comprovantes:
        # Abre o arquivo
        imagem = Image.open(f'./comprovantes/{nome_arquivo}')
        valor = descobrir_valor_do_pix(imagem)
        origem = descobrir_origem_pix(imagem)
        origem_valor.append({'origem': origem, 'valor': valor})
    
    return origem_valor

x = main()
print(x)