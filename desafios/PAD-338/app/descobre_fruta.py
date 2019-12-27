class Descobre_Fruta():
    def __init__(self, fruta_secreta: str):
        self._fruta_secreta = fruta_secreta.lower()
        self._fruta_descoberta = '_' * len(fruta_secreta)

    def get_fruta_descoberta(self):
        return self._fruta_descoberta

    def get_fruta_secreta(self):
        return self._fruta_secreta

    def set_fruta_descoberta(self, fruta: str):
        self._fruta_descoberta = fruta

    def tem_letra(self, letra: str):
        if letra.lower() in self._fruta_secreta:
            return True
        else:
            return False

    def substituir_caractere_fruta(self, tentativa: str):
        tentativa = tentativa.lower()

        for i in range(len(self._fruta_secreta)):
            if tentativa == self._fruta_secreta[i]:
                self._fruta_descoberta = self._fruta_descoberta[:i] + tentativa + self._fruta_descoberta[i+1:]
        print(self._fruta_descoberta)


# --- Testando os métodos:
# start = Descobre_Fruta('banana')

# start.substituir_caractere_fruta('a')

