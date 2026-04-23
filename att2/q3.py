import math

class EquacaoII:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # Métodos simples para mudar os valores
    def set_a(self, valor): self.a = valor
    def set_b(self, valor): self.b = valor
    def set_c(self, valor): self.c = valor

    # Cálculo do Delta: b² - 4ac
    def delta(self):
        return (self.b ** 2) - (4 * self.a * self.c)

    # Verifica se o delta é positivo
    def tem_raizes_reais(self):
        return self.delta() >= 0

    # Primeira raiz (-b + raiz de delta) / 2a
    def raiz1(self):
        d = self.delta()
        return (-self.b + math.sqrt(d)) / (2 * self.a)

    # Segunda raiz (-b - raiz de delta) / 2a
    def raiz2(self):
        d = self.delta()
        return (-self.b - math.sqrt(d)) / (2 * self.a)

    def __str__(self):
        return f"Eu sou uma equação: {self.a}x² + {self.b}x + {self.c} = 0"

va = float(input("Digite o valor de a: "))
vb = float(input("Digite o valor de b: "))
vc = float(input("Digite o valor de c: "))

minha_conta = EquacaoII(va, vb, vc)

print(minha_conta)
print("O valor de delta é:", minha_conta.delta())

if minha_conta.tem_raizes_reais():
    print("Raiz 1:", minha_conta.raiz1())
    print("Raiz 2:", minha_conta.raiz2())
else:
    print("Essa conta não tem raízes reais (delta negativo).")