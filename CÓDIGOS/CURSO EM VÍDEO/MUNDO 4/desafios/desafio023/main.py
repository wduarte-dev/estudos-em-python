from classes import Triangulo, Quadrado, Retangulo
t1 = Triangulo(3, 4, 5)
print(t1.quantidade_de_lados)
print(t1.area())
print(t1.perimetro())

q1 = Quadrado(12)
print(q1.quantidade_de_lados)
print(q1.area())
print(q1.perimetro())

r1 = Retangulo(3, 4)
print(r1.quantidade_de_lados)
print(r1.area())
print(r1.perimetro())

t2 = Triangulo(1, 2, 3)