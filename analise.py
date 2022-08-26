# MATHEUS ALVES PINHEIRO
# Matrícula: 2112650GMEC

import math

n = int(input("Entre com um número de subdivisões: "))
a = 0
b = 10
h = (b-a)/n
i = 0

def fz(z):
    return math.exp(-2*z/10) * z/(4+z)

def gz(z):
    return z*math.exp(-2*z/10) * z/(4+z)

# Regra dos Trapézios

soma = 0
for i in range(1, n):
    soma = soma + fz(a+(i*h))

f = (h/2)*(fz(a)+2*(soma)+fz(b))

print("F: ", f)

soma = 0
for i in range(1, n):
    soma = soma + gz(a+(i*h))

g = (h/2)*(gz(a)+2*(soma)+gz(b))

print("G: ", g)

d = f/g

print("Valor de 'd' pela regra dos trapézios: ", d)


# Regra de 1/3 de Simpson


soma1 = 0
for i in range(1, int(n/2 + 1)):
    soma1 = soma1 + fz(a + (2*i - 1)*h)

soma2 = 0
for i in range(1, int(n/2)):
    soma2 += fz(a+(2*i)*h)

w = (h/3)*(fz(a)+fz(b)+4*(soma1)+2*(soma2))

print("W: ", w)

soma1 = 0
for i in range(1, int(n/2 + 1)):
    soma1 = soma1 + gz(a + (2*i - 1)*h)

soma2 = 0
for i in range(1, int(n/2)):
    soma2 += gz(a+(2*i)*h)

v = (h/3)*(gz(a)+gz(b)+4*(soma1)+2*(soma2))

print("V: ", v)

D = w/v

print("Valor de 'd' pela regra 1/3 de simpson: ", D)