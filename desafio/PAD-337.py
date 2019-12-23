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


cartas = ["2","3", "4", "5", "6", "7", "8", "9", "10", "A", "J", "Q", "K"]
pt = 0
while pt <= 21:
    random.shuffle(cartas)

    resp = int(input(f'Digite um valor de 0 à {len(cartas)-1}: '))

    print(f'Carta: {cartas[resp]}')
    try:
        pt+= int(cartas[resp])
    except:
        if cartas[resp] == "A":
            if pt > 0:
                pt+= 1
            pt+=11
        elif cartas[resp] == 'Q':
            pt+= 10
        elif cartas[resp] == "K":
            pt+=10

    print(f'Pontuação: {pt}')
    cartas.pop(resp)

print('Fim de Jogo')










