import random
'''
"2" => 2
"3" => 3
"4" => 4
"5" => 5
"6" => 6
"7" => 7
"8" => 8
"9" => 9
"10" => 10
"A" => 1 or 11
"J" => 10
"Q" => 10
"K" => 10
'''
def continuar():
    while True:
        resposta = input('Deseja continuar? [S/N] ').upper().strip()
        if resposta == 'S':
            return True
        elif resposta == 'N':
            return False
        else:
            print('\033[1;31mResposta inválida, apenas [S/N]!\033[m')


cartas = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "J", "Q", "K"]
cartas_salvas = []

pt = 0

continuar_resp = True
while continuar_resp:
    random.shuffle(cartas)

    carta_retirada = cartas.pop(random.randint(0,len(cartas)-1))
    cartas_salvas.append(carta_retirada)

    print(f'Cartas já Viradas: {cartas_salvas}')
    try:
        pt+=int(carta_retirada)
        print(f'Pontuação: \033[1;32m{pt}\033[m')
    except:
        if carta_retirada == 'A':
            if pt > 0:
                pt+=1
            else:
                pt+=11
        elif carta_retirada == 'J':
            pt+=10
        elif carta_retirada == 'Q':
            pt+=10
        else:
            pt+=10
        print(f'Pontuação: \033[1;32m{pt}\033[m')

    continuar_resp = continuar()
    if len(cartas) == 0:
        print('\033[1;33mOpa as cartas acabaram! Fim de jogo.\033[m')
        break
    elif pt >= 21:
        print('\033[1;33mOpa você passou dos 21 pontos! Fim de jogo.\033[m')
        break
    else:
        continue

print('Finalizado!')

