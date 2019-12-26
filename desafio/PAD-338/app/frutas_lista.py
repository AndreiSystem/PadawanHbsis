import random

class FrutasLista:
    def __init__(self, frutas: list):
        self._frutas = frutas

    def get_frutas(self):
        return self._frutas.copy()

    def shuffle(self):
        random.shuffle(self._frutas)

    def put_frutas(self):
        if not self.existe_frutas():
            raise Exception('Não existe frutas')
        return self._frutas.pop(0)

    def existe_frutas(self):
        return len(self._frutas)

    def tamanho_caractere(self):
        return '_' * len(self.put_frutas())