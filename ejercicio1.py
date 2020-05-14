# -*- coding: utf-8 -*-

from io import open

print('*'*30)
print('\n**** Welcome to Kwranking ****\n')
print('*'*30)
print('\n[1]--Importar palabras clave')
print('\n[2]--Mostrar palabras clave')
print('\n[0]--Salir\n')
print('*' * 30 + '\n')


def carga_keyword():

    global keywords

    listaNombres = open('keyword.txt', 'r')

    keywords = listaNombres.readlines()

    listaNombres.close()


while True:

    opcion = input('\nTeclee la opción deseada: ')

    if opcion == '1':

        carga_keyword()

        print('Lectura de archivo finalizada')

    elif opcion == '2':

        carga_keyword()  # si el usuario del menu va primero a opcion 2 antes de opcion 1

        inicio = 0

        cantidad_iteraciones = round(len(keywords) / 20)

        for x in range(cantidad_iteraciones):

            listado_parcial = keywords[inicio:inicio + 20]

            for y in listado_parcial:

                print(y)

            inicio += 20

            input('\nTeclee una tecla para continuar...\n')

    elif opcion == '0':

        print('\nVuelva pronto. :)\n')

        break

    else:

        print('\nEsa no es una opcion válida...')
