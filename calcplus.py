#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():
	def __init__(self,numeros):
		self.numeros = numeros

	def suma(self,sumandos):
		for i in sumandos:
			sumas += int(sumando[i+1]) 
		print(sumas) 
		
	def resta(self,numeros):
		for i in numeros:
			resta -= int(numeros[i+1])
		print(resta)

class CalculadoraHija(Calculadora):

	def multiplica(self,numeros):
		for i in numeros:
			multiplica *= int(palabras[i+1])
		print(multiplica)

	def divide(self,numeros):
		for i in numeros:
			if numeros != 0:
				divide /= int(numeros[i+1])
			else:
				print('Division by zero is not allowed')
		print(divide)


if __name__ == "__main__":
	try:	
		fichero = sys.argv[1] 
		fich = open(fichero,'r')
			
		fich.close
		lines = fich.readlines()

		for line in lines:
		
			palabras = line.split(',')
			x = CalculadoraHija(palabras)
			
			for palabra in palabras:
				if palabras == 'suma':
					x.suma(palabras)
				elif palabras == 'resta':
					x.resta(palabras)
				elif palabras == 'multiplica':	
					x.multiplica(palabras)
				elif palabras == 'divide':
					x.divide(palabras)
				else:
					print("--")
		
	except:
		sys.exit("Error")
