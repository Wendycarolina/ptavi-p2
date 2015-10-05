#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv


def crealist(numeros):
    a = []
    for i in numeros:
        if i != numeros[0]:
            a.append(int(i))
    numeros = a
    return numeros


class Calculadora():
    def __init__(self, numeros):
        self.numeros = numeros

    def suma(self, sumandos):
        a = crealist(sumandos)
        sumas = 0
        for j in a:
            sumas += j
        print(sumas)

    def resta(self, numeros):
        a = crealist(numeros)           
        restas = 0
        for j in a:
            if j == a[0]:
                j = j*-1
            restas -= j
        print(restas)


class CalculadoraHija(Calculadora):
    def multiplica(self, numeros):
        a = crealist(numeros) 
        multiplicar = 1
        for j in a:
            multiplicar *= j
        print(multiplicar)

    def divide(self, numeros):
        a = crealist(numeros) 
        divides = a[0]
        for j in a[1:]:
            if j != 0:
                divides /= j
            else:
                print('Division by zero is not allowed')
        print(divides)


if __name__ == "__main__":
    try:
        fichero = sys.argv[1]
        fich = open(fichero, 'r')
        fich.close
        lines = fich.readlines()

        for line in lines:
            palabras = line.split(',')
            x = CalculadoraHija(palabras)
            operacion = palabras[0]
            if operacion == 'suma':
                x.suma(palabras)
            elif operacion == 'resta':
                x.resta(palabras)
            elif operacion == 'multiplica':
                x.multiplica(palabras)
            elif operacion == 'divide':
                x.divide(palabras)
    except:
        sys.exit("Error")
