import random
import time

def revisarEleccion(): #Evita que el usuario ponga otra cosa que no sea un número del 1 al 9 y evita que se repitan fichas
    eleccion = int(input('\nSeleccione una ficha: '))
    while len(str(eleccion)) != 1 or str(eleccion) not in '123456789' or eleccion in eleccionesUsuario or eleccion in eleccionesPC:
        eleccion = int(input('Seleccione una ficha: '))
    return eleccion

def revisarEleccionPC(): #Evita que la compu repita una ficha que ya haya usado o que el usuario haya usado
    pc = random.choice(opciones)
    while pc in eleccionesUsuario or pc in eleccionesPC:
        pc = random.choice(opciones)
    return pc

def iniciaUsuario(): #Primer turno si va a iniciar primero el usuario
    tablero(fichasJugador, fichasCompu)
    f1 = revisarEleccion()
    eleccionesUsuario.append(f1)
    tablero(fichasJugador, fichasCompu)
    
    pc1 = revisarEleccionPC()
    eleccionesPC.append(pc1)
    print('\nFicha #1 compu = ', pc1)
    time.sleep(2)
    tablero(fichasJugador, fichasCompu)
    
    f2 = revisarEleccion()
    eleccionesUsuario.append(f2)
    tablero(fichasJugador, fichasCompu)
    
    pc2 = revisarEleccionPC()
    eleccionesPC.append(pc2)
    print('\nFicha #2 compu = ', pc2)
    time.sleep(2)
    tablero(fichasJugador, fichasCompu)
    
    f3 = revisarEleccion()
    eleccionesUsuario.append(f3)
    tablero(fichasJugador, fichasCompu)
    
    pc3 = revisarEleccionPC()
    eleccionesPC.append(pc3)
    print('\nFicha #3 compu = ', pc3)
    time.sleep(2)
    tablero(fichasJugador, fichasCompu)
    
def iniciaPC(): #Primer turno si va a iniciar primero la computadora
    tablero(fichasJugador, fichasCompu)
    
    pc1 = revisarEleccionPC()
    eleccionesPC.append(pc1)
    print('\nFicha #1 compu = ', pc1)
    time.sleep(2)
    tablero(fichasJugador, fichasCompu)

    f1 = revisarEleccion()
    eleccionesUsuario.append(f1)
    tablero(fichasJugador, fichasCompu)

    pc2 = revisarEleccionPC()
    eleccionesPC.append(pc2)
    print('\nFicha #2 compu = ', pc2)
    time.sleep(2)
    tablero(fichasJugador, fichasCompu)

    f2 = revisarEleccion()
    eleccionesUsuario.append(f2)
    tablero(fichasJugador, fichasCompu)
    
    pc3 = revisarEleccionPC()
    eleccionesPC.append(pc3)
    print('\nFicha #3 compu = ', pc3)
    time.sleep(2)
    tablero(fichasJugador, fichasCompu)

    f3 = revisarEleccion()
    eleccionesUsuario.append(f3)
    tablero(fichasJugador, fichasCompu)
    
def sumaPC(eleccionesPC): #Realiza la suma de las fichas de la compu
    sumaPC = 0
    for i in eleccionesPC:
        sumaPC += i
    return sumaPC   

def sumaU(eleccionesUsuario): #Suma las fichas del usuario
    sumaU = 0
    for i in eleccionesUsuario:
        sumaU += i
    return sumaU

def tablero(fichasJugador, fichasCompu): #Tablero que se va a mostrar en el juego
    print('\n'*30)
    print ('Fichas: ', opciones)
    print('Fichas de usuario: ' ,eleccionesUsuario)
    print('Fichas de computadora: ' , eleccionesPC)

'''def cambioFicha(): #Pide la ficha a cambiar y la cambia por otra
    fichaCambia = int(input('\n¿Cuál ficha desea cambiar?\nFicha #: '))
    eleccionesUsuario[fichaCambia - 1] = int(input('Nueva posición de ficha: '))

def cambiandoFichas(): #Va pidiendo cambio de ficha hasta que alguien gane
    while ganar:
        cambioFicha()
        tablero(fichasJugador, fichasCompu)
        ganar()'''

def ganar(): #Define si alguien gana o no
    sumaUsuario = sumaU(eleccionesUsuario)
    sumaCompu = sumaPC(eleccionesPC)
    if sumaCompu == 15:
        print ('\nGana compu')
        return True
    elif sumaUsuario == 15:
        print('\nGana usuario')
        return True
    else:
        print('\nNadie gana')
        return False
    
#----------------------------------------- PRINCIPAL -------------------------------------------------------------------------------

opciones = [1,2,3,4,5,6,7,8,9]
continuar = True


eleccionesUsuario = []
eleccionesPC = []
pc1 = 0
pc2 = 0
pc3 = 0
f1 = 0
f2 = 0
f3 = 0
turno = 0
fichasCompu = ''
fichasJugador = ''

print ('Bienvenido al juego de 15 en fichas :D')
pantallaDeInicio = input('\n1. JUGAR\n2. COMO JUGAR\n3. SALIR\n\nOPCIÓN: ')
while pantallaDeInicio != '3':
    if pantallaDeInicio == '1':
        iniciar = input('¿Quién desea iniciar?\n1.Usuario\n2.Computadora\nSu elección: ')
        if iniciar == '1':
            iniciaUsuario()
            ganar()
        elif iniciar == '2':
            iniciaPC()
            ganar()
    elif pantallaDeInicio == '2': 
        print("\nEl juego es simple, primero seleccionas 3 fichas, para ganar, esas fichas \nsumadas deben dar 15. Jugaras contra el computador. \nEl primero que consiga llegar a 15 gana.")
        pantallaDeInicio = input('\n1. JUGAR\n2. COMO JUGAR\n3. SALIR\n\nOPCIÓN: ')
print('Muchas gracias, vuelva pronto')

    