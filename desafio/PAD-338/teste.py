
import random
from abc import ABC
class Listas_Frutas(ABC):

    _frutas_lista = ['banana',
                    'jabuticaba',
                    'pitanga',
                    'mirtilo',
                    'morango',
                    'abacaxi',
                    'cereja'
                    ]
    def escolher_fruta(self):
        return self._frutas_lista.pop(0)

    def tamanho_fruta(self):
        return '_' * len(self._frutas_lista.pop(0))





fruta_escolhida = Listas_Frutas().tamanho_fruta()
fruta_len = Listas_Frutas().escolher_fruta()

for i in range(0, len(fruta_len)):
    if 'a' == fruta_len[i]:
        fruta_escolhida = fruta_escolhida[:i] + 'a' + fruta_escolhida[i + 1:]




#pt = len(fruta_escolhida)
#print(pt)

#for i in range(0, len(fruta_escolhida)):
#    if 'a' == fruta_escolhida[i]:
#        palavra_descoberta = palavra_descoberta[:i] + 'a' + palavra_descoberta[i + 1:]