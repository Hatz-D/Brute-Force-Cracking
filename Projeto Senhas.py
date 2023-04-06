# Diogo Lourenzon Hatz  TIA: 32247389
# Leila Akina Ino   TIA: 32261128

import hashlib, base64


def codificar_senha(senha):
    senha_encoded = senha.encode('utf-8')
    digest = hashlib.sha512(senha_encoded).digest()
    digest_b64_encoded = base64.b64encode(digest)
    digest_b64_encoded_utf8_decoded = digest_b64_encoded.decode('utf-8')
    return digest_b64_encoded_utf8_decoded


def checagem(hash, linhas):
    for i in range(len(linhas)):
        linha = linhas[i].rstrip().split(':')

        if linha[1] == hash:
            return True, linha[0]

    return False, ''


def preencher_senhas_nao_quebradas(quebradas, nao_quebradas, usuarios):
    usuarios.seek(0, 0)
    quebradas_linhas =  quebradas.readlines()
    usuarios_linhas = usuarios.readlines()
    tamanho_quebradas = len(quebradas_linhas)
    tamanho_usuarios = len(usuarios_linhas)

    for i in range(tamanho_usuarios):
        aux = False
        for j in range(tamanho_quebradas):
            if quebradas_linhas[j].rstrip().split(':')[0] == usuarios_linhas[i].rstrip().split(':')[0]:
                aux = True
        if not aux:
            linha = usuarios_linhas[i]
            nao_quebradas.write(linha)


def combinacoes(palavras, usuarios, quebradas):
    comidas = palavras.readlines()
    linhas = usuarios.readlines()
    tamanho = len(comidas)

    for i in range(tamanho):                                      # Combinação de uma comida
        comida = comidas[i].rstrip()

        senha_codificada = codificar_senha(comida)
        resposta, nome = checagem(senha_codificada, linhas)

        if resposta:
            quebradas.write(nome + ':' + comida + '\n')

    for i in range(tamanho):                                     # Combinação de duas comidas
        comida_1 = comidas[i].rstrip()
        for j in range(tamanho):
            comida_2 = comidas[j].rstrip()

            comida = comida_1 + ' ' + comida_2
            senha_codificada = codificar_senha(comida)
            resposta, nome = checagem(senha_codificada, linhas)

            if resposta:
                quebradas.write(nome + ':' + comida + '\n')

    for i in range(tamanho):                                     # Combinação de três comidas
        comida_1 = comidas[i].rstrip()
        for j in range(tamanho):
            comida_2 = comidas[j].rstrip()
            for x in range(tamanho):
                comida_3 = comidas[x].rstrip()

                comida = comida_1 + ' ' + comida_2 + ' ' + comida_3
                senha_codificada = codificar_senha(comida)
                resposta, nome = checagem(senha_codificada, linhas)

                if resposta:
                    quebradas.write(nome + ':' + comida + '\n')

    for i in range(tamanho):                                    # Combinação de quatro comidas
        comida_1 = comidas[i].rstrip()
        for j in range(tamanho):
            comida_2 = comidas[j].rstrip()
            for x in range(tamanho):
                comida_3 = comidas[x].rstrip()
                for y in range(tamanho):
                    comida_4 = comidas[y].rstrip()

                    comida = comida_1 + ' ' + comida_2 + ' ' + comida_3 + ' ' + comida_4
                    senha_codificada = codificar_senha(comida)
                    resposta, nome = checagem(senha_codificada, linhas)

                    if resposta:
                        quebradas.write(nome + ':' + comida + '\n')

    for i in range(tamanho):                                    # Combinação de cinco comidas
        comida_1 = comidas[i].rstrip()
        for j in range(tamanho):
            comida_2 = comidas[j].rstrip()
            for x in range(tamanho):
                comida_3 = comidas[x].rstrip()
                for y in range(tamanho):
                    comida_4 = comidas[y].rstrip()
                    for z in range(tamanho):
                        comida_5 = comidas[z].rstrip()

                        comida = comida_1 + ' ' + comida_2 + ' ' + comida_3 + ' ' + comida_4 + ' ' + comida_5
                        senha_codificada = codificar_senha(comida)
                        resposta, nome = checagem(senha_codificada, linhas)

                        if resposta:
                            quebradas.write(nome + ':' + comida + '\n')


def main():
    palavras = open('palavras.txt', 'r', encoding='utf-8')
    usuarios = open('usuarios_senhascodificadas.txt', 'r', encoding='utf-8')
    quebradas = open('senhas_quebradas.txt', 'w', encoding='utf-8')
    nao_quebradas = open('senhas_nao_quebradas.txt', 'w', encoding='utf-8')
    combinacoes(palavras, usuarios, quebradas)
    quebradas.close()
    quebradas = open('senhas_quebradas.txt', 'r', encoding='utf-8')
    preencher_senhas_nao_quebradas(quebradas, nao_quebradas, usuarios)
    palavras.close()
    usuarios.close()
    quebradas.close()
    nao_quebradas.close()


if __name__ == '__main__':
    main()