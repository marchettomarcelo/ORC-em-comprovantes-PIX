import unidecode
    # unaccented_string = unidecode.unidecode(primeira_palavra_da_imagem)

def identificar_banco_do_comprovante(txt):
    txt = txt.split()
    primeira_palavra_da_imagem = txt[0]
    if primeira_palavra_da_imagem == "nu":
        return "NUBANK"

    if primeira_palavra_da_imagem == "inter":
        return "INTER"

    try:
        if txt.index('realizada') == 3:
            return "ITAU"
    except:
        pass
    
    