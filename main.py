import time

BLACK='\033[3Om'
RED='\033[31m'
GREEN ='\033[32m'
YELLOW='\033[33m'
BLUE ='\033[34m'
MAGENTA ='\033[35m'
CYAN ='\033[36m'
WHITE ='\033[37m'
RESET ='\033[39m'

rpta=['a','b','c','d']

iniciarTrivia=True

nombre=input("Ingrese su nombre: ")

print("==== Bienvenido ", nombre.upper()," a mi trivia sobre Informatica ==== ")
  
print("-Responde las siguientes preguntas escribiendo la letra correcta ")
print("-Empezaras con un puntaje de 0 ")
print("-Respuestas correctas +10 puntos e incorrectas -5 puntos")

while iniciarTrivia==True:

  puntaje=0

  print("\n=========COMENZEMOS=========\n")
  time.sleep(2)
  
  print("1) Quién fue el creador de Linux ?\n")
  
  print("a) Linus Torvalds")
  print("b) Bill Gates")
  print("c) Mark Sukerberg")
  print("d) Dennis Ritchie")
  
  respuesta_1=input("Ingrese su respuesta : ")

  while respuesta_1 not in rpta:
    respuesta_1=input("Ingrese la letra correcta : ")
  time.sleep(2)
  if respuesta_1 == 'a' :
    print (GREEN+"Correcto"+RESET)
    puntaje=puntaje+10
  else:
    print(RED+"Incorrecto"+RESET)
    puntaje=puntaje-5
  
  time.sleep(2)  
  
  print("\n2) Cuál de estos no es un navegador ?")
  
  print("a) Mozilla")
  print("b) Chrome")
  print("c) Opera")
  print("d) Turbonet")
  
  respuesta_2=input("Ingrese su respuesta : ")
  while respuesta_1 not in rpta:
    respuesta_1=input("Ingrese la letra correcta : ")
  time.sleep(2)  
  
  if respuesta_2.lower() == 'd' :
    print (GREEN+"Correcto"+RESET)
    puntaje=puntaje+10
  else:
    print(RED+"Incorrecto"+RESET)
    puntaje=puntaje-5
  
  time.sleep(2)  
  
  print("\n3) Cuál de la siguiente opciones no es un motor de búsqueda ?")
  
  print("a) Yahoo")
  print("b) Google")
  print("c) Oracle")
  print("d) Bing")
  
  respuesta_3=input("Ingrese su respuesta : ")
  while respuesta_1 not in rpta:
    respuesta_1=input("Ingrese la letra correcta : ")
  time.sleep(2)
  
  if respuesta_3.lower() == 'c' :
    print (GREEN+"Correcto"+RESET)
    puntaje=puntaje+10
  else:
    print(RED+"Incorrecto"+RESET)
    puntaje=puntaje-5
  
  time.sleep(2)  
  
  print("\n4) Cuál de estos programas no esta en Microsoft Office? ")
  
  print("a) Word")
  print("b) Excel")
  print("c) Paint")
  print("d) PowerPoint")
  
  respuesta_4=input("Ingrese su respuesta : ")
  while respuesta_1 not in rpta:
    respuesta_1=input("Ingrese la letra correcta : ")
  time.sleep(2)
  
  if respuesta_4.lower() == 'c' :
    print (GREEN+"Correcto"+RESET)
    puntaje=puntaje+10
  else:
    print(RED+"Incorrecto"+RESET)
    puntaje=puntaje-5
    
  time.sleep(2)  
  
  print("\n5) Qué significa WI-FI? ")
  
  print("a) Wiggly Fibres")
  print("b) Wireless Fidelity")
  print("c) Wireless Fings")
  print("d) Width of File")
  
  respuesta_5=input("Ingrese su respuesta : ")
  while respuesta_1 not in rpta:
    respuesta_1=input("Ingrese la letra correcta : ")
  time.sleep(2)
    
  if respuesta_5.lower() == 'b' :
    print (GREEN+"Correcto"+RESET)
    puntaje=puntaje+10
  else:
    print(RED+"Incorrecto"+RESET)
    puntaje=puntaje-5
    
  time.sleep(2)

  print("---La trivia ha finalizado---")

  time.sleep(2)
  
  print(nombre.upper()," haz obtenido ",puntaje," puntos")

  print("\n Deseas realizar la trivia otravez ?")
  opcion=input("1)si    2)no").lower()

  if opcion=='no':
    print("Espero que lo hayas pasado bien, hasta pronto! ")
    iniciarTrivia=False
    
  else:
    puntaje=0