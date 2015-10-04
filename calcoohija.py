#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def suma(self, sumando1, sumando2):
        return sumando1 + sumando2

    def resta(self, numero1, numero2):
        return numero1 - numero2


class CalculadoraHija(Calculadora):
    def multiplica(self, numero1, numero2):
        return numero1 * numero2

    def divide(self, numero1, numero2):
        return numero1 / numero2

if __name__ == "__main__":
    try:
        numero1 = float(sys.argv[1])
        operacion = str(sys.argv[2])
        numero2 = float(sys.argv[3])
        x = CalculadoraHija(numero1, numero2)
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    except ZeroDivisionError:
        sys.exit("Division by zero is not allowed")

    if operacion == "suma":
        print(x.suma(numero1, numero2))
    elif operacion == "resta":
        print(x.resta(numero1, numero2))
    elif operacion == "multiplica":
        print(x.multiplica(numero1, numero2))
    elif operacion == "divide":
        print(x.divide(numero1, numero2))
    else:
        print("Operación incorrecta")
