from classes.cartas import Cartas
from funcoes.funcao_continuar import continuar


def jogo_start(pt:int):
    cartas = Cartas()
    continuar_resp = True
    print('Começou!')
    while continuar_resp:
        cartas.embaralhar()

        carta_retirada = cartas.retirar_carta()
        cartas.salvar_cartas(carta_retirada)


        cartas.retornar_cartas_salvas()

        try:
            pt += int(carta_retirada)
            print(f'Pontuação: \033[1;32m{pt}\033[m')
        except:
            if carta_retirada == 'A':
                if pt > 0:
                    pt += 1
                else:
                    pt += 11
            elif carta_retirada == 'J':
                pt += 10
            elif carta_retirada == 'Q':
                pt += 10
            else:
                pt += 10
            print(f'Pontuação: \033[1;32m{pt}\033[m')

        continuar_resp = continuar()

        if len(cartas.cartas) == 0:
            print('\033[1;33mOpa as cartas acabaram! Fim de jogo.\033[m')
            print('Jogo Finalizado!')
            break
        elif pt >= 21:
            print('\033[1;33mOpa você passou dos 21 pontos! Fim de jogo.\033[m')
            print('Jogo Finalizado!')
            break
        else:
            continue









