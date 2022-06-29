import pytesseract


def descobrir_valor_do_pix(imagem):
    tranferido = 0

    txt = pytesseract.image_to_string(imagem).split(',')
    
    for index, palavras in enumerate(txt):
        try:
            centavos = int(palavras[0:2])
            inteiros = int(txt[index-1].split(' ')[-1].replace('.', ''))
            tranferido = float(f'{inteiros}.{palavras[0:2]}')
        except:
            pass

    return tranferido