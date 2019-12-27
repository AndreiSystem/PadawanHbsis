import random
cartas = ["2","3", "4", "5", "6", "7", "8", "9", "10", "A", "J", "Q", "K"]
cartas_selecionadas = []
print('JOGO DAS CARTAS!')

pt = 0
while pt < 21:
    random.shuffle(cartas)
    carta = cartas.pop(random.randint(0, len(cartas)-1))

    cartas_selecionadas.append((carta))
    
    print(cartas_selecionadas)
    print(f'Carta: {carta}')
    try:
        pt+=int(carta)
        print(f'Pontuação: {pt}')
    except:

        if carta == 'A':

            if pt > 0:
                pt+=1
                print(f'Pontuação: {pt}')
            else:
                pt+=1
                print(f'Pontuação: {pt}')
        elif carta == 'J':
            pt+=10
            print(f'Pontuação: {pt}')
        elif carta == 'Q':
            pt+=10
            print(f'Pontuação: {pt}')
        else:
            pt+=10
            print(f'Pontuação: {pt}')
    if pt > 21:
        break
    resp = input('Deseja virar outra carta? [S/N] ').upper()

    if resp == 'S':
        continue
    else:
        break
print('Fim de Jogo!')

