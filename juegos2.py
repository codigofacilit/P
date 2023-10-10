import random
def jugar():

    print("====================================")
    print("bienvenido al juego de adivinanza ")
    print("====================================")
    numero_secreto = random.randrange(1,101)
    puntaje =1000 # puntaje
    print("seleccione el nivel de dificultad")
    print("(1) facil   (2) medio   (3) dificil")
    nivel = int(input("ingrese un nivel de dificultad"))
    if(nivel ==1):
      total_intentos = 20
    elif(nivel==2):
      total_intentos = 10
    else:
      total_intentos = 5

    for iteracion in range(1, total_intentos, +1):
       print("intentos:{} de {}".format(iteracion,total_intentos))
       entrada = input("digite un numero 1 y 100 : ")
       entrada  = int(entrada)
       print("digitaste..", entrada )
       if(entrada<1 or entrada > 100):
          print("ingresar un nuemro entre 1  y 100 ")
          continue

       acertaste= entrada == nuemro_secreto #iguales
       mayor = entrada > nuemro_secreto # mayor
       menor = entrada< nuemro_secreto # menor


       if(acertaste):
          print("felicidades !! .. adivinaste el numero y ganaste {} puntos ". format(puntaje))
        #  iteraciones=6
          break

       elif(mayor ):
          print("lo siento.. el nuewmor que ingresaste es mayor")
       else:
          print(" lo sinto... , nuemro que ingresaste es menor que el nuemro secreto ")
       puntos_perdidos =abs(nuemro_secreto- entrada)

    print("fin del juego")
if(__name__=="__main__"):
    escoger_juego()