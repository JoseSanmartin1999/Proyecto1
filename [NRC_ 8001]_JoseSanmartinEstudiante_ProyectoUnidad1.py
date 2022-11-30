"""
Break The Code, es un popular juego de mesa y bastante divertido, el objetivo de este es que un jugador debera adivinar una clave propuesta
con digitos al azar en una cantidad de Turnos determinada, entre menos turnos utilize, mejor sera su puntuacion, en este caso hemos simplifi
cado un poco el juego, pero manteniendo su esencia adaptandolo a la tarea enviada.

Autor
Jose Sanmartin
Inspirado en: Break the Code de Ryohei Kurahashi

Version
Ver 1.0
"""
import random
import os
print("Jugemos BREAK THE CODE")
nombre=input("Escribe Tu nombre Agente: ")
# el conjunto de simbolos validos en el codigo en este caso digitos
digitos = ('0','1','2','3','4','5','6','7','8','9')

# "elegimos" el codigo mediante la funcion random
cant_digitos = 5
codigo = ''
for i in range(cant_digitos):
    candidato = random.choice(digitos)
    # vamos eligiendo digitos no repetidos
    while candidato in codigo:
        candidato = random.choice(digitos)
    codigo = codigo + candidato

# iniciamos interaccion con el usuario
print ("Bienvenido/a  Agente ",nombre, " a la Agencia BTC Necesitamos Encontrar unos documentos escondidos por el enemigo ")
print ("Necesitamos Entrar a la computadora del enemigo para ello")
print ("Tienes que adivinar su clave, un numero de", cant_digitos, 
      "cifras distintas, puedes hacerlo en la menor cantidad de intentos posibles")
propuesta = input("¿Que codigo propones?: ")

# procesamos las propuestas e indicamos aciertos y coincidencias que hay en el codigo
intentos = 1
while propuesta != codigo and propuesta != "Me rindo" and intentos<25:
    intentos = intentos + 1
    aciertos = 0
    coincidencias = 0

    # recorremos la propuesta y verificamos en el codigo
    for i in range(cant_digitos):
        if propuesta[i] == codigo[i]:
            aciertos = aciertos + 1
        elif propuesta[i] in codigo:
            coincidencias = coincidencias + 1
    print ("Tu propuesta (", propuesta, ") tiene", aciertos, \
          "aciertos y ", coincidencias, "coincidencias.")
    # pedimos siguiente propuesta
    propuesta = input("Propón otro codigo, DEBEN SER Digitos Distintos o Me rindo para terminar: ")
#planteamos los posibles escenarios 
#Nos planteamos una manera de terminar el juego 
if (propuesta == "Me rindo"):
    print ("nos descubieron El codigo era", codigo)
    print ("Suerte la proxima vez!")
elif(intentos<=5):
    print ("Felicitaciones! Adivinaste el codigo en", \
    intentos, "Eres el mejor Agente del Mundo.Agente", nombre)
    print ("Te llamaremos para una siguiente Mision")
elif(intentos>=6 or intentos<=10):
    print ("Felicitaciones! Adivinaste el codigo en", \
    intentos, "Eres Bueno, agente ", nombre)
    print ("Te llamaremos para una siguiente Mision")
elif(intentos>=11 or intentos<=15):
    print ("Felicitaciones! Adivinaste el codigo en", \
    intentos, "Muy Bien, agente ", nombre)
    print ("Te tendermos en cuenta para una siguiente Mision")
elif(intentos>=16 or intentos<=20):
    print ("Felicitaciones! Adivinaste el codigo en", \
    intentos, "Bien, agente ", nombre)
    print ("Debes mejorar un poco mas")

else:
    (intentos>=21 or intentos<=24)
    print ("Felicitaciones! Adivinaste el codigo en", \
    intentos, "intentos.Casi no Descubren")
os.system("pause")