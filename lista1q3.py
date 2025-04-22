import math
base = float(input("digite a base do retangulo: "))
altura = float(input("digite a altura do retangulo:"))
area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt(base**2 + altura**2)
print(f"area: {area:.2f}")
print(f"perimetro: {perimetro:.2f}")
print(f"diagonal: {diagonal:.2f}")