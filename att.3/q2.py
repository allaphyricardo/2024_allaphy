class Pais:
    def __init__(self, nome, populacao, area):
        self.set_nome(nome)
        self.set_populacao(populacao)
        self.set_area(area)

    def get_nome(self): return self.__nome
    def set_nome(self, valor):
        if not valor: raise ValueError("Nome do país é obrigatório.")
        self.__nome = valor

    def get_populacao(self): return self.__populacao
    def set_populacao(self, valor):
        if valor < 0: raise ValueError("População não pode ser negativa.")
        self.__populacao = valor

    def get_area(self): return self.__area
    def set_area(self, valor):
        if valor <= 0: raise ValueError("Área deve ser maior que zero.")
        self.__area = valor

    def densidade(self):
        return self.__populacao / self.__area

class PaisUI:
    @staticmethod
    def menu():
        print("\n1 – Calcular\n2 – Fim")
        return input("Opção: ")

    @staticmethod
    def calculo():
        try:
            nome = input("Nome do País: ")
            pop = int(input("População (habitantes): "))
            area = float(input("Área (km²): "))
            
            p = Pais(nome, pop, area)
            
            print(f"\n--- Dados do País ---")
            print(f"País: {p.get_nome()}w")
            print(f"População: {p.get_populacao()} hab.")
            print(f"Área: {p.get_area()} km²")
            print(f"Densidade Demográfica: {p.densidade():.2f} hab/km²")
        except ValueError as e:
            print(f"Erro nos dados: {e}")

    @classmethod
    def main(cls):
        while True:
            op = cls.menu()
            if op == '1':
                cls.calculo()
            elif op == '2':
                print("Saindo...")
                break
            else:
                print("Opção inválida!")

if __name__ == "__main__":
    PaisUI.main()