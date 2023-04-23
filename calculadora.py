#!/usr/bin/env python3
#author: Hans saldias
'''calculadora'''
from colorama import init, Fore

def suma():
    print(Fore.GREEN+'''
.dP"Y8 88   88 8b    d8    db
`Ybo." 88   88 88b  d88   dPYb
o.`Y8b Y8   8P 88YbdP88  dP__Yb
8bodP' `YbodP' 88 YY 88 dP""""Yb
''')
    print(Fore.YELLOW+"*** suma ***".upper())
    n1 = int(input("Ingrese digito: "))
    n2 = int(input("Ingrese digito: "))
    total = n1 + n2
    print(Fore.RED+f"\n{n1} + {n2}  =  {total}")

def resta():
    print(Fore.GREEN+'''
88""Yb 888888 .dP"Y8 888888    db
88__dP 88__   `Ybo."   88     dPYb
88"Yb  88""   o.`Y8b   88    dP__Yb
88  Yb 888888 8bodP'   88   dP""""Yb
''')
    print(Fore.YELLOW+"*** resta ***".upper())
    n1 = int(input("Ingresa Digito: "))
    n2 = int(input("Ingrese Dijito:"))
    total = n1 - n2
    print(Fore.RED+f"\n{n1} - {n2} = {total}")

def multi():
    print(Fore.GREEN+'''
8b    d8 88   88 88     888888 88
88b  d88 88   88 88       88   88
88YbdP88 Y8   8P 88  .o   88   88
88 YY 88 `YbodP' 88ood8   88   88
''')
    print(Fore.YELLOW+"*** Multiplicacion ***".upper())
    n1 = int(input("Ingresa Digito: "))
    n2 = int(input("Ingresa Digito: "))
    total = n1 * n2
    print(Fore.RED+f"\n{n1} x {n2} = {total}")

def div():
    print(Fore.GREEN+'''
8888b.  88 Yb    dP 88 .dP"Y8 88  dP"Yb  88b 88
 8I  Yb 88  Yb  dP  88 `Ybo." 88 dP   Yb 88Yb88
 8I  dY 88   YbdP   88 o.`Y8b 88 Yb   dP 88 Y88
8888Y"  88    YP    88 8bodP' 88  YbodP  88  Y8
''')
    print(Fore.YELLOW+"*** division ***".upper())
    n1 = int(input("Ingrese Digito: "))
    n2 = int(input("Ingrese Digito: "))
    total = n1 / n2
    print(Fore.RED+f"\n{n1} : {n2} = {total}")

def potencia():
    print(Fore.GREEN+'''
88""Yb  dP"Yb  888888 888888 88b 88  dP""b8 88    db
88__dP dP   Yb   88   88__   88Yb88 dP   `" 88   dPYb
88"""  Yb   dP   88   88""   88 Y88 Yb      88  dP__Yb
88      YbodP    88   888888 88  Y8  YboodP 88 dP'''''''Yb
''')
    print(Fore.YELLOW+"*** POTENCIA ***")
    n1 = int(input("Ingrese Base: "))
    n2 = int(input("Ingrese Exponente: "))
    total = n1 ** n2
    print(Fore.RED+f"\n{n1} √ {n2} = {total}")

def menu():
    print(Fore.GREEN+'''
 dP""b8    db    88      dP""b8 88   88 88        db
dP   `"   dPYb   88     dP   `" 88   88 88       dPYb
Yb       dP__Yb  88  .o Yb      Y8   8P 88  .o  dP__Yb
 YboodP dP""""Yb 88ood8  YboodP `YbodP' 88ood8 dP""""Yb
''')
    while True:
        print(Fore.YELLOW+'''
        *** CALCULADORA ***
        [1] suma
        [2] resta
        [3] multiplicar
        [4] dividir
        [5] potencia
        [0] salir''')
        op = input("Ingrese opcion: ")
        if op == "1":
            suma()
        elif op == "2":
            resta()
        elif op == "3":
            multi()
        elif op == "4":
            div()
        elif op == "5":
            potencia()
        elif op == "0":
            break
        
menu()


