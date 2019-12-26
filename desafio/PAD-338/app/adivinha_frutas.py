import os

from .player import Player
from .frutas import Banana, Jabuticaba, Pitanga, Mirtilo, Morango, Abacaxi, Cereja
from .frutas_lista import FrutasLista

class AdivinhaFrutas(object):

    def __init__(self, player: Player):


        _frutas = [
            Banana(),
            Jabuticaba(),
            Pitanga(),
            Mirtilo(),
            Morango(),
            Abacaxi(),
            Cereja()
        ]

        self._frutas_lista = FrutasLista(_frutas)
        self._player = player
        self._score = 0

    def start(self):
        print('===== Começando =====')

        while self._frutas_lista.existe_frutas():
            resp = input('Digite uma letra: ')
            fruta = self._frutas_lista.put_frutas()
            fruta_descoberta = self._frutas_lista.tamanho_caractere()
            print(fruta_descoberta)

            for i in range(0, len(fruta)):
                if resp == fruta[i]:
                    fruta_descoberta = fruta_descoberta[:i] + resp + fruta_descoberta[i+1:]

            print(fruta_descoberta)


