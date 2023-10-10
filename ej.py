lista = [0.9]

unidades =[" ","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve"]
dieces =[" ","once", "doce","trece","catorce", "quince", "diezciseis", "diecisiete", "dieciocho", "diecinueve"]
decenas = [" ","diez","veinte", "treinta","cuarenta","cincuenta", "sesenta","setenta", "ochenta", "noventa"]
literal= " " 

numero=input("ingrese un numero")
posicion = 2

for indice in numero:
     if posicion == 2 and indice == '1':
        literal = literal + dieces[int(numero[1])]
        break
    if posicion== 2 and indice != '1':  
        literal= literal + ' ' + decenas[int(indice)]
    if posicion==1:
        literal=literal + ' ' + unidades[int(indice)]
   
    
    posicion=posicion-1
print (literal)