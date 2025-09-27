# 6)escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
import random
num_ale = [random.randint(1,100) for i in range (50)]
from statistics import mode , median , mean
mn=mean(num_ale)
me=median(num_ale)
mo=mode(num_ale)
if mo<me and me<mn:
    print("Sesgo positivo o a la derecha.")
elif mn<me and me<mo:
    print("Sesgo negativo o a la izquierda.")
elif mo==me==mn:
    print("Sin sesgo.")
else:
    print("Sin resultado.")