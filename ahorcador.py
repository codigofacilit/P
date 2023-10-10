def jugar():
    print ("=======================")
    print("BIENVENIDO AL JUEGO DEL AHORCADO")
    print ("=======================")
    palabra_secreta="mandarina "
    ahorcado = False
    acerto = False
    while (not ahorcado and not acerto):
        
        entrada =input("ingrese una letra :")
        for letra in palabra_secreta:
            
            if(entrada ==letra):
                print(entrada)
        print("jugando...")

 
        