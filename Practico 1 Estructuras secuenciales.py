#1 Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print("Hola Mundo")



#2 Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.

#Pido el nombre con la funcion input
nombre=input("Ingrese su nombre:")
#utilizo print f para simplificar
print(f"Hola {nombre}")



#3 Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

#Pido los datos con la funcion input
nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
edad=input("Ingrese su edad: ")
residiencia=input("Ingrese su pais de residencia: ")

#Escribo la frase con los datos ingresados y utilizo print f para que sea mas sencillo
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residiencia}")



#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

#pido que ingrese el radio del circulo y uso float para que la variable quede en decimal
radio=float(input("Ingrese el radio del circulo: "))
#Realizo las operaciones matematicas
area=3.1415*radio**2
perimetro=2*3.1415*radio
#Escribo la resolucion del problema utilizando print f
print(f"El area del circulo es:{area}")
print(f"Su perimetro del circulo es: {perimetro}")



#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

#Pido que ingrese la cantidad de segundo y cambio la variable a decimal con float
segundos=float(input("Ingrese los segundos: "))
#Hago los calculos matematicos para llegar a las horas usando float para que queden en decimal
minutos=float(segundos/60)
horas=float(minutos/60)
#Escribo la equivalencia de segundos en horas
print(f"Su equivalente en horas es: {horas}")



#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

#Pido el numero, lo voy a hacer de entero y la tabla va a ser de 0 a 10
num=int(input("Ingrese su numero: "))
#Realizo la tabla matematica
ce=int(num*0)
un=int(num*1)
do=int(num*2)
tr=int(num*3)
cu=int(num*4)
ci=int(num*5)
se=int(num*6)
si=int(num*7)
oc=int(num*8)
nu=int(num*9)
di=int(num*10)
#Escribo la tabla
print(f"x0={ce}")
print(f"x1={un}")
print(f"x2={do}")
print(f"x3={tr}")
print(f"x4={cu}")
print(f"x5={ci}")
print(f"x6={se}")
print(f"x7={si}")
print(f"x8={oc}")
print(f"x9={nu}")
print(f"x10={di}")



#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

#pido el numero entero y uso int
num=int(input("Ingrese su primer numer: "))
num2=int(input("Ingrese su segundo numero: "))
#realizo las operaciones matematicas
sum=int(num+num2)
res=int(num-num2)
mul=int(num*num2)
div=float(num/num2)
#escribo los resultados
print(f"La suma de ambos es: {sum}")
print(f"El resto de ambos es: {res}")
print(f"La multiplicacion de ambos es: {mul}")
print(f"La division de ambos es: {div}")



#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal.

#Pido los datos y utilizo float
al=float(input("Ingrese su altura en metros: "))
pe=float(input("Ingrese su peso en kilogramos: "))
#utilizo la formula de imc
imc=float(pe/al**2)
#escribo el imc resultante
print(f"Su índice de masa corporal es de: {imc}")



#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit.

#pido los grados en celsius y utilizo float
celsius=float(input("Ingrese su temperatura en grados celsius: "))
#Hago la conversion de celsius a fahrenheit
fahrenheit=float(((9/5)*celsius)+32)
#Escribo la temperatura en fahrenheit
print(f"Su equivalente en grados Fahrenheit es de: {fahrenheit}")



#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

#pido al usuario que ingrese sus 3 numeros usando float
num1=float(input("Ingrese su primer numero: "))
num2=float(input("Ingrese su segundo numero: "))
num3=float(input("ingrese su tercer numero: "))
#Realizo el calculo de promedio
prom=float((num1+num2+num3)/3)
#escribo el resultado
print(f"El promedio de sus 3 numeros es de: {prom}")