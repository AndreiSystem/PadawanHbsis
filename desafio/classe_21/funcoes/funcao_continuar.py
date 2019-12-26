def continuar():
    while True:
        resposta = input('Deseja continuar? [S/N] ').upper().strip()
        if resposta == 'S':
            return True
        elif resposta == 'N':
            print('Jogo Finalizado!')
            return False
        else:
            print('\033[1;31mResposta inválida, apenas [S/N]!\033[m')
