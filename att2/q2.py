import math

class Frete:
    def __init__(self, distancia, peso):
        # Usamos os métodos de set para garantir a validação desde o início
        self.set_distancia(distancia)
        self.set_peso(peso)

    def set_distancia(self, d):
        self._distancia = d if d > 0 else 0

    def set_peso(self, p):
        self._peso = p if p > 0 else 0

    def get_distancia(self): return self._distancia
    def get_peso(self): return self._peso

    def calc_frete(self):
        # R$ 0,01 por kg por km
        return 0.01 * self._peso * self._distancia

    def __str__(self):
        return f"Sou o sistema de Frete. Carga: {self._peso}kg | Percurso: {self._distancia}km."

try:
    d = float(input("Digite a distância em Km: "))
    p = float(input("Digite o peso em Kg: "))

    meu_frete = Frete(d, p)

    print("\n" + str(meu_frete))
    print(f"Valor do Frete: R$ {meu_frete.calc_frete():.2f}")

except ValueError:
    print("\nERRO: Por favor, digite apenas números. Use ponto (.) em vez de vírgula.")