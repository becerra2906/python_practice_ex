#### Done as part of Basic Python Course in Platzi

#### This program will take an inputted ammount of 
#### Colombian pesos (COP) and transform it to an ammount of USD

pesos = input("¿Cuántos pesos colombianos tienes? ")
pesos = float(pesos)
valor_dolar = 3875
dolares = pesos / float(valor_dolar)
dolares = round(dolares, 2)
dolares = str(dolares)
confirmation_message = "Tienes $ {} dolares".format(dolares)
print(confirmation_message)


