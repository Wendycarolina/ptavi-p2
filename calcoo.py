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

if __name__ == "__main__":
    try:
        numero1 = float(sys.argv[1])
        operacion = str(sys.argv[2])
        numero2 = float(sys.argv[3])
        x = Calculadora(numero1, numero2)

    except ValueError:
        sys.exit("Error: Non numerical parameters")
    if operacion == "suma":
        print(x.suma(numero1, numero2))
    elif operacion == "resta":
        print(x.resta(numero1, numero2))
    else:
        print("Operación incorrecta")
