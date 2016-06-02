#uso del modulo random
#usando la libreria random generar un numero entero entre 999 y 10000
#iniciar una variable "t" en 1
#decinir un cilco en true
#pedir un numero al usuario
#verificar si los dos numeros son iguales:
#si son iguales cortar el ciclo
#si no son iguales sumarle 1 al variable "t"
#cuando el usuario adivine el numero decir la cantidad de intentos que necesito


import random
a = random.randint(999, 10000)
t = 1
while True:
    c = input('Ingresar numero: ')
    if c == a:
        print "Adivinaste"
        break
    t = t + 1
print "Necesito "+str(t)+" intentos"
