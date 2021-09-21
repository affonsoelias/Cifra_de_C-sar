#Implementação do cifra de César básico.
#Autor affonso elias ferreira junior.

lista = 'abcdefghijklmnopqrstuvwxyz'
ponteiro_lista = 0
ponteiro_msg = 0
contador = 1


print('Escreva um numero para chave')
chave = input('')
print('Escreva a mensagem em letras minusculas e sem espaço e caracteres especiais')
msg = input('')


tamanhomensagem = len(msg)
tamanho_lista = len(lista)
print('tamanho da mensagem',tamanhomensagem)
print('tamanho da lista',tamanho_lista)
codigo = ''



while contador <= tamanhomensagem:
    if (msg[ponteiro_msg] != lista[ponteiro_lista]) or (ponteiro_lista > tamanho_lista):
        if (ponteiro_lista > tamanho_lista):
            ponteiro_lista = ponteiro_lista - tamanho_lista
        elif msg[ponteiro_msg] != lista[ponteiro_lista]:   
            while msg[ponteiro_msg] != lista[ponteiro_lista]:
                ponteiro_lista += 1
    elif msg[ponteiro_msg] == lista[ponteiro_lista]:
        ponteiro_lista += int(chave)
        if (ponteiro_lista > tamanho_lista):
            while (ponteiro_lista > tamanho_lista):
                ponteiro_lista = ponteiro_lista - tamanho_lista
        codigo += lista[ponteiro_lista] 
        ponteiro_lista = 0
        print(codigo)
        contador += 1
        ponteiro_msg += 1
print(codigo)

