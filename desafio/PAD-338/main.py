from PAD-338.app.adivinha_frutas import AdivinhaFrutas
from PAD-338.app.player import Player

if __name__ == '__main__':
    print('====Adivinha===')
    player = Player(input('Falae: '))
    adivinha = AdivinhaFrutas(player)
    adivinha.start()