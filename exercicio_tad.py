class operacao():
    def __init__(self, n1, n2, n3):
        self.a = n1
        self.b = n2
        self.c = n3

        self.soma = n1 + n2 + n3
        self.sub = n1 - n2 - n3
        self.div = n1 / n2 / n3
        self.mult = n1 * n2 * n3


x = complex(4, 6)
y = complex(-6, 13)
z = complex(7, -5)

print("Números complexos utilizados:\nx =", x, "\ny =", y, "\nz =", z)
print("")
resultado = operacao(x, y, z)

print("Resultado da Soma:", resultado.soma, "\nA parte real é: ", resultado.soma.real, " e a imaginária é ", resultado.
      soma.imag, "\n")
print("Resultado da Subtração:", resultado.sub, "\nA parte real é: ", resultado.sub.real, " e a imaginária é ",
      resultado.sub.imag, "\n")
print("Resultado da Divisão:", resultado.div, "\nA parte real é: ", resultado.div.real, " e a imaginária é ",
      resultado.div.imag, "\n")
print("Resultado da Multiplicação:", resultado.mult, "\nA parte real é: ", resultado.mult.real, " e a imaginária é ",
      resultado.mult.imag, "\n")
