#init = input("¿Qué moneda quieres convertir? ")

#monedas = ("dolares", "pesos colombianos", "Dolares", "dolares ", "Dolares ", "Pesos Colombianos", "pesos ","pesos", "Pesos Colombianos ", "pesos colombianos ")

#if init in ("pesos colombianos","Pesos Colombianos", "pesos ","pesos", "Pesos Colombianos ", "pesos colombianos "): 

    #pesos = input("¿Cuántos pesos colombianos tienes? ")
    #pesos = float(pesos)
    #valor_dolar = 3875
    #dolares = pesos / float(valor_dolar)
    #dolares = round(dolares, 2)
    #dolares = str(dolares)
    #confirmation_message = "Tienes $ {} dolares".format(dolares)
    #print(confirmation_message)

#if init in ("dolares", "Dolares", "dolares ", "Dolares "): 

    #dolares = input("¿Cuántos dolares tienes? ")
    #dolares = float(dolares)
    #valor_peso = 0.27
    #pesos = (dolares / float(valor_peso))*1000
    ### pesos = round(pesos, 2)
    #pesos = str(pesos)
    #confirmation_message = "Tienes $ {} pesos".format(pesos)
    #print(confirmation_message)


#if init not in monedas : 
    #print ("En este momento no soportamos esa moneda, vuelve a correr el programa e intenta con Dolares o Pesos Colombianos")


#def suma(a,b):
    #print('Se suman dos numeros: ')
    #resultado = a + b
    #return resultado
#sumatoria = suma(1,4)
#print(sumatoria)


def currency_converter(valor, tasa) :
   proceso = int(tasa) * int(valor) 
   return proceso


init = str(input('¿Qué moneda tienes? (para pesos colombianos pon COP, para soles peruanos pon PEN, y para pesos méxicanos MXN)'))
valor = input('¿Cúanto quieres convertir?')
tasa = int(input("¿A cuánto se está transando el dolar?"))

if  init == 'cop' : 
        currency_converter(valor, tasa)
        print(proceso)