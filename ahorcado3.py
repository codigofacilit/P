import random 
def jugar():

    print('================================')
    print('Bienvenido al Juego del Ahorcado')
    print('================================')
    

    archivo = open('palabras.txt','r')
    palabras = []
    
    for linea in archivo:
        
        linea = linea.strip()
        palabras.append(linea)

    archivo.close()
    
    numero =random.randrange(0,len(palabras))

    palabra_secreta = palabras[numero].lower()
    
    letras_acertadas = ['_' for elemento in palabra_secreta]
    

    ahorcado = False
    acerto =False

 
    
