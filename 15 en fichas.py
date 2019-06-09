import random

def revisarEleccion():
    eleccion = int(input('Elija un número de 1 a 9: '))
    while len(str(eleccion)) != 1 or str(eleccion) not in '123456789' or eleccion in eleccionesUsuario or eleccion in eleccionesPC:
        eleccion = int(input('Elija un número de 1 a 9: '))
    return eleccion

def revisarEleccionPC():
    pc = random.choice(opciones)
    while pc in eleccionesUsuario or pc in eleccionesPC:
        pc = random.choice(opciones)
    return pc

def Inicio():
    print ('Bienvenido al juego de 15 en fichas :D')
    iniciar = input('¿Quién desea iniciar?\n1.Usuario\n2.Computadora\nSu elección: ')
    if iniciar == '1':
        iniciaUsuario()
    elif iniciar == '2':
        iniciaPC()

def ganar():
    sumaUsuario = sumaU(eleccionesUsuario)
    sumaCompu = sumaPC(eleccionesPC)
    if sumaCompu == 15:
        print ('Gana compu')
        return True
    elif sumaUsuario == 15:
        print('Gana usuario')
        return True
    else:
        print('Nadie gana')
    

def sumaPC(eleccionesPC):
    sumaPC = 0
    for i in eleccionesPC:
        sumaPC += i
    return sumaPC   

def sumaU(eleccionesUsuario):
    sumaU = 0
    for i in eleccionesUsuario:
        sumaU += i
    return sumaU

def tablero(turno, fichasJugador, fichasCompu):
    print('\n'*30)
    print('Turno: ', turno)
    print('Fichas de usuario: ' ,eleccionesUsuario)
    print('Fichas de computadora: ' , eleccionesPC)

def cambioFicha():
    fichaCambia = int(input('¿Cuál ficha desea cambiar?\nFicha #: '))
    eleccionesUsuario[fichaCambia - 1] = int(input('Nueva posición de ficha: '))

def cambiandoFichas(turno):
    while not ganar():
        turno += 1
        tablero(turno,fichasJugador, fichasCompu)
        ganar()
        cambioFicha()

def iniciaUsuario():
    tablero(turno, fichasJugador, fichasCompu)
    f1 = revisarEleccion()
    eleccionesUsuario.append(f1)

    pc1 = revisarEleccionPC()
    eleccionesPC.append(pc1)
    print('\nElección de ficha 1 compu = ', pc1)

    f2 = revisarEleccion()
    eleccionesUsuario.append(f2)

    pc2 = revisarEleccionPC()
    eleccionesPC.append(pc2)
    print('\nElección de ficha 2 compu = ', pc2)

    f3 = revisarEleccion()
    eleccionesUsuario.append(f3)

    pc3 = revisarEleccionPC()
    eleccionesPC.append(pc3)
    print('\nElección de ficha 3 compu = ', pc3)

    tablero(turno, fichasJugador, fichasCompu)

def iniciaPC():
    tablero(turno, fichasJugador, fichasCompu)
    
    pc1 = revisarEleccionPC()
    eleccionesPC.append(pc1)
    print('\nElección de ficha 1 compu = ', pc1)

    f1 = revisarEleccion()
    eleccionesUsuario.append(f1)

    pc2 = revisarEleccionPC()
    eleccionesPC.append(pc2)
    print('\nElección de ficha 2 compu = ', pc2)

    f2 = revisarEleccion()
    eleccionesUsuario.append(f2)
    
    pc3 = revisarEleccionPC()
    eleccionesPC.append(pc3)
    print('\nElección de ficha 3 compu = ', pc3)

    f3 = revisarEleccion()
    eleccionesUsuario.append(f3)

    tablero(turno, fichasJugador, fichasCompu)
#----------------------------------------- PRINCIPAL -------------------------------------------------------------------------------

opciones = [1,2,3,4,5,6,7,8,9]
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

Inicio()
ganar()