# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 12:10:54 2020

@author: andre
"""

#Imports necessários
from random import randint as dado
import ctypes

#função do número
def dado60():
    return dado(1, 60)

#processamento do programa
def main():
   
    #loop do programa, 6 = botao sim e 7 = botao nao
    resposta = 6
    while resposta != 7:
   
        #calculo dos numeros
        n1 = n2 = n3 = n4 = n5= n6 = 0
        
        n1 = dado60()
        
        n2 = dado60()
        while n2 == n1:
            n2 = dado60()
            
        n3 = dado60()
        while n3 == n2 or n3 == n1:
            n3 = dado60()
            
        n4 = dado60()
        while n4 == n3 or n4 == n2 or n4 == n1:
            n4 = dado60()
        
        n5 = dado60()
        while n5 == n4 or n5 == n3 or n5 == n2 or n5 == n1:
            n5 = dado60()
        
        n6 = dado60()
        while n6 == n5 or n6 == n4 or n6 == n3 or n6 == n2 or n6 == n1:
            n6 = dado60()
        
        #ordenacao do reseultado
        resultado = sorted([n1, n2, n3, n4, n5, n6], reverse=False)
        resultado = str(resultado)
        
        #exibição em tela do resultado
        resposta = ctypes.windll.user32.MessageBoxW(0, resultado + "\n\n Jogar novamente?", "Jogo da Mega Sena", 4)

#main
if __name__ == "__main__":
    main()
