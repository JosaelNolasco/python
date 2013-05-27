#Calculadora Aritmitca 
def Menu():
    """Funcion que Muestra el Menu
    """
    print """************
Calculadora Ingenieria de Software
************
Wilman Josael Martinez Nolasco #SMIS371013
************
Menu
------------
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Salir"""

def Calculadora():
    """Funcion Para Calcular Operaciones Aritmeticas"""
    Menu()
    opc = int(input("Selecione una opcion\n"))
    while (opc >0 and opc <5):
        x = int(input("Ingrese primer numero\n"))
        y = int(input("Ingrese segundo numero\n"))
        if (opc==1):
            print "La Suma es:", x+y
            opc = int(input("Selecione una opcion\n"))
        elif(opc==2):
            print "La Resta es:",x-y
            opc = int(input("Selecione una opcion\n"))
        elif(opc==3):
            print "La Multiplicacion es:",x*y
            opc = int(input("Selecione una opcion\n"))
        elif(opc==4):
            try:
              print "La Division es:", x/y
              opc = int(input("Selecione una opcion\n"))
            except ZeroDivisionError:
              print "No se Permite la Division Entre 0"
              opc = int(input("Selecione una opcion\n"))

Calculadora()








