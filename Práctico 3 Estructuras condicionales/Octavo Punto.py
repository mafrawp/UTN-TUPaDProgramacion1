# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.
name=input("Ingrese su nombre: ")
num=int(input("""Ingrese 1 si quiere su nombre en mayúsculas
Ingrese 2 si quiere su nombre en minúscula
Ingrese 3 si quiere su nombre con la primera letra en mayúscula
          """))
if num == 1:
    print(name.upper())
elif num == 2:
    print(name.lower())
else:
    print(name.title())