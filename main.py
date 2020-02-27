# Escribir los datos que se te piden asta que sea correcto 
# Importa el módulo requerido para usar Regular Expressions

import re

# Colocaremos un break para que al escribir los datos correctos ya no se pregunte 
# en caso de no cumplir las condiciones se repitira asta cumplirlo

while True:
    tel = input("Dame tu numero de telefono: ")
    coincide = re.search("[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]", tel)
    if (coincide):
      print("telefono Correcto!")
      break
    else:
      print("Telefono incorrecto. Intenta de nuevo.")