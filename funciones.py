# part of platzi´s python basic course

# def imprimir_mensaje():
    # print("Mensaje Especial: ")
    # print("Estoy aprendiendo a usar funciones!")

# imprimir_mensaje()

def conversacion(mensaje):
    print('Hola ')
    print('Como estás? ')
    print(mensaje)
    print('Adiós')


opcion = int(input("Elige una opción (1,2,3): "))

if opcion == 1: 
    conversacion(mensaje = 'Elegiste la ópcion 1.')
elif opcion == 2:
    conversacion(mensaje = 'Elegiste la ópcion 2.')
elif opcion == 3:
    conversacion(mensaje = 'Elegiste la ópcion 3.')
else: 
    print('Elige una opción valida. ')

