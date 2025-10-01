# 10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.
hemis=input("Ingrese el hemisferio en donde se encuentra: ")
mes=input("Ingrese el mes del año: ")
dia=int(input("Ingrese el día: "))
if hemis=="sur":
    if (mes=="diciembre" and dia>=21) or mes=="enero" or (mes=="marzo" and dia<=20):
        print("Usted se encuentra en verano.")
    elif (mes=="marzo" and dia>=21) or mes=="abril" or mes=="mayo" or (mes=="junio" and dia<=20):
        print("Usted se encuentra en otoño.")
    elif (mes=="junio" and dia>=21) or mes=="julio" or mes=="agosto" or (mes=="septiembre" and dia<=20):
        print("Usted se encuentra en invierno.")
    else:
        print("Usted se encuentra en primavera.")
elif hemis=="norte":
    if (mes=="diciembre" and dia>=21) or mes=="enero" or (mes=="marzo" and dia<=20):
        print("Usted se encuentra en invierno.")
    elif (mes=="marzo" and dia>=21) or mes=="abril" or mes=="mayo" or (mes=="junio" and dia<=20):
        print("Usted se encuentra en primavera.")
    elif (mes=="junio" and dia>=21) or mes=="julio" or mes=="agosto" or (mes=="septiembre" and dia<=20):
        print("Usted se encuentra en verano.")
    else:
        print("Usted se encuentra en otoño.")
else:
    print("Verifique los datos.")