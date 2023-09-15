import random
from datetime import datetime
import time
import os

a = random.randint(10, 99)
b = random.randint(10, 99)

print("Eres capaz de sumar", a,  "+", b, "?")

instanteInicial = datetime.now()

result = a + b

# time.sleep(5)
#
# os.system("cls")

your_result = int(input("Introduce tu resultado:"))

while result != your_result:
    your_result = int(input("Intentalo de nuevo:"))

instanteFinal = datetime.now()
tiempo = instanteFinal - instanteInicial # Devuelve un objeto timedelta
segundos = tiempo.seconds

print("Has realizado la suma en", segundos, "segundos")




