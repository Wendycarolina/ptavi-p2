#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Vamos a programar una calculadora
#git commit -m "..." calc.py

import sys


def main():
    pass


def suma(sumando1, sumando2):
    return float(sumando1) + float(sumando2)


def resta(numero1, numero2):
    return float(numero1) - float(numero2)


if __name__ == "__main__":
    try:
        dicc = {"sumar": suma, "restar": resta}
        operando1 = sys.argv[1]
        operacion = dicc[sys.argv[2]]
        operando2 = sys.argv[3]
        print(operacion(operando1, operando2))
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    except KeyError:
        sys.exit("Operación incorrecta")
