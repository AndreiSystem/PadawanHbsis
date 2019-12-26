import random

class Cartas:
    cartas = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "J", "Q", "K"]
    cartas_salvas = []


    def embaralhar(self):
        return random.shuffle(self.cartas)

    def retirar_carta(self):
            return self.cartas.pop(random.randint(0,len(self.cartas)-1))

    def salvar_cartas(self, carta_retirada):
        self.cartas_salvas.append(carta_retirada)

    def retornar_cartas_salvas(self):
        print(f'Cartas já viradas: {self.cartas_salvas}')
