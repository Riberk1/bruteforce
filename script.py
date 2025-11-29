def carregar_wordlist(file)
    try
        with open(file, r) as f
            return [linha.strip() for linha in f]
    except FileNotFoundError
        print(fArquivo '{file}' não encontrado.)
        return []

def main()
    arquivo = wordlist.txt
    palavras = carregar_wordlist(arquivo)

    if not palavras
        return

    print(Processando entradas da wordlistn)

    for palavra in palavras
        print(f- Entrada encontrada {palavra})

    print(nProcesso finalizado.)

if __name__ == __main__
    main()
