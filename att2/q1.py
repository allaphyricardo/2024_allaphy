import math

class Retangulo:
    def __init__(self, b, h):

        self.set_base(b)
        self.set_altura(h)

    def set_base(self, b):
        self._b = b if b > 0 else 0

    def set_altura(self, h):
        self._h = h if h > 0 else 0

    def get_base(self): return self._b
    def get_altura(self): return self._h

    def calc_area(self): return self._b * self._h
    
    def calc_diagonal(self): 
        return math.sqrt(self._b**2 + self._h**2)

    def __str__(self):
        return f"Olá! Eu sou um retângulo. Minha base é {self._b} e minha altura é {self._h}."


b_user = float(input("Digite a base: "))
h_user = float(input("Digite a altura: "))

meu_retangulo = Retangulo(b_user, h_user)

print("\n" + str(meu_retangulo))
print(f"Minha área calculada é: {meu_retangulo.calc_area()}")
print(f"Minha diagonal é: {meu_retangulo.calc_diagonal():.2f}")