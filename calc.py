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
	
		operando1 = sys.argv[1]
		operacion = str(sys.argv[2])
		operando2 = sys.argv[3]

	except ValueError:
		sys.exit("Error: Non numerical parameters")

	if operacion == "suma":
		print(suma(operando1,operando2))
	elif operacion == "resta":
		print(resta(operando1,operando2))
	else:
		print("Operación incorrecta")

