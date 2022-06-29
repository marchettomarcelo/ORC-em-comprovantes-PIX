def descobre_nome_enviador(txt, banco):
    palavras_chave = {
        "NUBANK": "T} Origem",
        "INTER": "Quem pagou",
        "ITAU": "de"
    }

    quem_mandou = ""
    txt = txt.split("\n")
    txt_limpo = [frase for frase in txt if frase != ""]
    
    index_palavra_chave = txt_limpo.index(palavras_chave[banco])
    linha_contem_nome = txt_limpo[index_palavra_chave+1]

    if banco == "NUBANK":
        return linha_contem_nome.replace("Nome", "").strip()
    
    if banco == "INTER":
        lista_palavras = linha_contem_nome.split()
        quem_mandou = [nome.capitalize() for nome in lista_palavras if nome != "Nome"]
        return " ".join(quem_mandou)

    if banco == "ITAU":
        return linha_contem_nome