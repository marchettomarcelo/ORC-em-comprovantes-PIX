import pytesseract
# from PIL import Image
from nome_enviador import descobre_nome_enviador
from descobrir_banco import identificar_banco_do_comprovante
import unidecode

def descobrir_origem_pix(imagem):    
    txt = pytesseract.image_to_string(imagem)

    # Descobre de que banco foi enviado o PIX
    o_banco = identificar_banco_do_comprovante(txt)
    if not o_banco:
        return "Não foi possível descobrir o banco do PIX"
    nome_enviador = descobre_nome_enviador(txt, o_banco)
    
    return nome_enviador
    