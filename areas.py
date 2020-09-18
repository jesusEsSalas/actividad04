import os
import time
clear = lambda: os.system('cls')
def areaCuad(lado):
    return lado**2

def areaTri(base, altura):
    return (base * altura) / 2

def areaCir(radio):
    pi = 3.1416
    return pi * radio**2
  
while True:
    print("AREAS")
    print("1.Cuadrado")
    print("2.Triángulo")
    print("3.Círculo")
    print("0.Salir")
    opc = int(input("Selecciona una opción: "))
    time.sleep(0.2)
    clear()
    if opc == 1:
        lado = float(input("Ingresa uno de los lados del cuadrado: "))
        print("Área: {:.2f}".format(areaCuad(lado)))
    elif opc == 2:
        base = float(input("Base del triángulo: "))
        altura = float(input("Altura del triángulo: "))
        print("Área: {:.2f}".format(areaTri(base, altura)))
    elif opc == 3:
        radio = float(input("Radio del círculo: "))
        print("Área: {:.2f}".format(areaCir(radio)))
    elif opc == 0:
        break
    else:
        print("Opción inválida):")
        time.sleep(1)
        clear()