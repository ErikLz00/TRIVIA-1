import time
import random
from os import system


#colores
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"
RESET ="\033[39m"

#creando una lista con las preguntas
preguntas=['1) ¿Quién fue el creador de Linux ?',
          '2) ¿Cuál de estos no es un navegador ?',
          '3) ¿Cuál de la siguiente opciones no es un motor de búsqueda ?',
          '4) ¿Cuál de estos programas no esta en Microsoft Office?',
          '5) ¿Qué significa WI-FI?',
          ]

#creando una lista con las alternativas
contenido=['\na) Linus Torvalds \nb) Bill Gates \nc) Mark Sukerberg \nd) Dennis Ritchie ',
          '\na) Mozilla \nb) Chrome \nc) Opera \nd) Turbonet',
          '\na) Yahoo \nb) Google \nc) Oracle \nd) Bing',
          '\na) Word \nb) Excel \nc) Paint \nd) PowerPoint',
          '\na) Wiggly Fibres \nb) Wireless Fidelity \nc) Wireless Fings \nd) Width of File'
          ]

#lista con las respuestas 
respuestas=['a','d','c','c','b']

claves=['a','b','c','d']

#variable de condicion para que inicie el bucle
iniciatrivia=True

system("cls")

#iniciamos pidiendo el nombre del participante
nombre=input(LIGHT_BLUE+"\nINGRESE SU NOMBRE : "+RESET)

time.sleep(2)

system("cls")

#le damos la bienvenida y mencionamos la regla del juego
print(LIGHT_GREEN+"\n==== BIENVENIDO ", nombre.upper()," A LA TRIVIA DE INFORMATICA ===="+RESET)
print(LIGHT_WHITE+"\n-Responde las siguientes preguntas escribiendo la letra correcta ")
print("\n-Empezaras con un puntaje de 0 ")
print("\n-Respuestas correctas se agregaran puntos y las incorrectas se quitaran puntos")
print("\n-Los puntos se daran aleatoriamente "+RESET)

time.sleep(6) 

system("cls")

#creamos un bucle para comenzar y si quiere seguir jugando
while iniciatrivia==True:

  #iniciamos el puntaje en cero
  puntaje=0
  
  #variable que recorrera la lista
  inicio=0

  print(LIGHT_PURPLE+"\n=========  COMENZEMOS  =========\n"+RESET)

  time.sleep(2)
  
  while inicio<len(preguntas):

    #mostramos las preguntas y alternativas mostrando la lista
    print(preguntas[inicio])
    print(contenido[inicio])

    #pedimos que ingrese la respuesta
    respuesta_1=input(BLUE+"\nRespuesta : "+RESET)

    time.sleep(2)

    while respuesta_1 not in claves:

      #si ingresa otra clave, le pedimos que ingrese de nuevo 
      print(YELLOW+"\nIngrese de nuevo la clave ")
      respuesta_1=input(BLUE+"\nRespuesta : "+RESET)

    if respuestas[inicio] == respuesta_1.lower() :

      #mostramos la alerta si la respuesta es correcta
      print (GREEN+"\nCORRECTO"+RESET)
      puntaje=puntaje+random.randint(1,10)
    
    else:
      
      #mostramos la alerta si la respuesta es incorrecta
      print(RED+"\nINCORRECTO"+RESET)
      puntaje=puntaje-random.randint(1,10)
    
    time.sleep(2) 

    system("cls") 
    inicio+=1

  #mostramos un mensaje cuando se termina las preguntas
  print(CYAN+"----- LA TRIVIA HA FINALIZADO -----\n"+RESET)

  time.sleep(2)
  
  #mostramos el puntaje obtenido del participante
  print(nombre.upper()," haz obtenido ",puntaje," puntos")

  #consultamos si quiere realizar de nuevo la TRIVIA
  print("\nDeseas realizar la trivia otravez ?")
  opcion=input("\n1)si         2)no    : ").lower()

  system("cls")

  if opcion=='si':

    #si elije realizar otra trivia, reiniciamos el puntaje a cero y la variable que recorrera la lista
    puntaje=0

    inicio=0

  else:

    #si no quiere realizar otra trivia le mostramos un mensaje  
    #igualamos a false la condicion para que se cierre el bucle

    print(CYAN+"\nGracias por realizar la Trivia, hasta pronto! \n"+RESET)
    
    iniciatrivia=False
