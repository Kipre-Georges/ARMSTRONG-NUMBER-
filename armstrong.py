from math import  *
#Juste fonctionnel pour les nombres a 3 chiffres
nombre=input()
print("Le nombre que vous avez chosit est : ", nombre)

nombre1=nombre[0]
nombre2=nombre[1]
nombre3=nombre[2]

nombre1_int=int(nombre1)
nombre2_int=int(nombre2)
nombre3_int=int(nombre3)

test_armstrong=nombre1_int**3+nombre2_int**3+nombre3_int**3

if test_armstrong==int(nombre):
    print("Le nombre :  ",nombre,"Est bel et bien un nombre narcissique ")
else:
    print("Ce nombre n'est pas un nombre narcissique")