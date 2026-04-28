class Viagem:
    def __init__(self, destino, distancia, litros):
        self.set_destino(destino)
        self.set_distancia(distancia)
        self.set_litros(litros)

    def get_destino(self): return self.__destino
    def set_destino(self, v): self.__destino = v

    def get_distancia(self): return self.__distancia
    def set_distancia(self, v):
        if v <= 0: raise ValueError("A distância precisa ser maior que 0.")
        self.__distancia = v

    def get_litros(self): return self.__litros
    def set_litros(self, v):
        if v <= 0: raise ValueError("Os litros precisam ser maiores que 0.")
        self.__litros = v

    def consumo(self):
        return self.__distancia / self.__litros

class ViagemUI:
    def menu(self):
        print("\n1 - Calcular Consumo | 2 - Sair")
        return input("O que deseja fazer? ")

    def calculo(self):
        try:

            dest = input("Vai pá onde? ")
            dist = float(input(f"Quantos km dá daqui até {dest}? "))
            litros = float(input(f"E gastou quantos litros para chegar lá? "))

            v = Viagem(dest, dist, litros)

            print(f"\nBeleza! Para ir até {v.get_destino()}, seu carro fez uma média de {v.consumo():.2f} km/l.")
        except ValueError as e:
            print(f"Erro: {e}")

    def main(self):
        while True:
            op = self.menu()
            if op == '1': self.calculo()
            elif op == '2': break
            else: print("Opção errada!")

if __name__ == "__main__":
    ViagemUI().main()