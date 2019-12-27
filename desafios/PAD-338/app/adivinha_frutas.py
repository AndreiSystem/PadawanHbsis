from app.descobre_fruta import Descobre_Fruta
import random

class AdivinhaFrutas:
    _lista_frutas = ['banana', 'jabuticaba', 'pitanga', 'mirtilo', 'morango', 'abacaxi', 'cereja']
    _letra_fruta = ' '
    _score = 10

    def __init__(self):
        self._palavra = Descobre_Fruta(random.choice(self._lista_frutas))

    def set_fruta(self):
        return self._palavra

    def start(self):
        print('COMEÇANDO O RODEIO')

        while '_' in self._palavra._fruta_descoberta and self._score > 0:
            #status jogo:
            self.status()
            self.resposta_jogador()

            if self._palavra.tem_letra(self._letra_fruta):
                self._palavra.substituir_caractere_fruta(self._letra_fruta)
            else:
                self._score -= 1

        print(f'Pontuação final: {self._score}')
        print('Fim de jogo!')


    def status(self):
        print(f'A Fruta Secreta é: {self._palavra.get_fruta_descoberta()}')
        print(f'Score de Vida: {self._score}...')

    def resposta_jogador(self):
        while True:
            resposta = input('Digite uma letra: ')
            if len(resposta) == 1 and resposta.isalpha():
                self._letra_fruta = resposta
                break
            else:
                print('Digite somente uma letra!')



