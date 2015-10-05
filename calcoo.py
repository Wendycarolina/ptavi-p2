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
        numero2 = float(sys.argv[3])
        x = Calculadora(numero1, numero2)
        dicc = {"sumar": x.suma, "restar": x.resta}
        operacion = dicc[sys.argv[2]]
        print(operacion(numero1, numero2))
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    except KeyError:
        sys.exit("Operación incorrecta")
