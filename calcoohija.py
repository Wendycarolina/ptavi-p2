#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Calculadora():
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2

	def suma(self, num1, num2):
		return num1 + num2 
		
	def resta(self, num1, num2):
		return num1 - num2

class CalculadoraHija(Calculadora):

	def multiplica(self, num1, num2):
		return num1*num2	

	def divide(self, num1, num2):
		return num1 / num2

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

