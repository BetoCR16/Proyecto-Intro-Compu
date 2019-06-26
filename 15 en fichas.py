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
    #print('\nFicha #1 compu = ', pc1)
    #time.sleep(2)
    tablero(fichasJugador, fichasCompu)
    
    f2 = revisarEleccion()
    eleccionesUsuario.append(f2)
    tablero(fichasJugador, fichasCompu)
    
    pc2 = 15 - (f1 + f2)
    while pc2 in eleccionesUsuario or pc2 in eleccionesPC or str(pc2) not in '123456789':
        pc2 = random.choice(opciones)
    eleccionesPC.append(pc2)
    #print('\nFicha #2 compu = ', pc2)
    #time.sleep(2)
    tablero(fichasJugador, fichasCompu)
    
    f3 = revisarEleccion()
    eleccionesUsuario.append(f3)
    tablero(fichasJugador, fichasCompu)
    
    pc3 = 15 - sumaPC(eleccionesPC)
    while pc3 in eleccionesUsuario or pc3 in eleccionesPC or str(pc3) not in '123456789':
        pc3 = random.choice(opciones)
    #print('\nFicha #3 compu = ', pc3)
    #time.sleep(2)
    tablero(fichasJugador, fichasCompu)
    
def iniciaPC(): #Primer turno si va a iniciar primero la computadora
    tablero(fichasJugador, fichasCompu)
    
    pc1 = revisarEleccionPC()
    eleccionesPC.append(pc1)
    #print('\nFicha #1 compu = ', pc1)
    #time.sleep(2)
    tablero(fichasJugador, fichasCompu)

    f1 = revisarEleccion()
    eleccionesUsuario.append(f1)
    tablero(fichasJugador, fichasCompu)

    pc2 = revisarEleccionPC()
    eleccionesPC.append(pc2)
    #print('\nFicha #2 compu = ', pc2)
    #time.sleep(2)
    tablero(fichasJugador, fichasCompu)

    f2 = revisarEleccion()
    eleccionesUsuario.append(f2)
    tablero(fichasJugador, fichasCompu)
    
    pc3 = 15 - (f1 + f2)
    while pc3 in eleccionesUsuario or pc3 in eleccionesPC or str(pc3) not in '123456789':
        pc3 = random.choice(opciones)
    eleccionesPC.append(pc3)
    #print('\nFicha #3 compu = ', pc3)
    #time.sleep(2)
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

def cinta():
    lista = [1,2,3,4,5,6,7,8,9]
    numero = ['1 ','2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ']
    cinta = ['_','_','_','_','_','_','_','_','_']
    n = 0
    n2 = 0

    for i in eleccionesUsuario:  #Pone una U en los lugares de las fichas del usuario
        if i in lista:
            indice = lista.index(i)
            n += 1
            cinta[indice] = 'U'+ str(n)

    for i in eleccionesPC: #Pone una C en los lugares de las fichas de la compu
        if i in lista:
            indice = lista.index(i)
            n2 += 1
            cinta[indice] = 'C'+ str(n2)

    print(numero)
    print(cinta)

def tablero(fichasJugador, fichasCompu): #Tablero que se va a mostrar en el juego
    print('\n'*30)
    cinta()
    print('Suma PC: ', sumaPC(eleccionesPC))
    print('Suma Usuario: ', sumaU(eleccionesUsuario))

def cambioFicha(): #Pide la ficha a cambiar y la cambia por otra
    fichaCambia = int(input('\n¿Cuál ficha desea cambiar?\nFicha #: '))
    eleccionesUsuario[fichaCambia - 1] = int(input('Nueva posición de ficha: '))

def cambioFichaPC(eleccionesPC, eleccionesUsuario, opciones):
    fichaCambia = random.randint(0,2)
    print('Cambia: ', fichaCambia+1)
    eleccionesPC[fichaCambia] = 0
    eleccionesPC[fichaCambia] = 15 - sumaPC(eleccionesPC)
    print('....',eleccionesPC)
    while eleccionesPC[fichaCambia] in eleccionesUsuario or eleccionesPC[fichaCambia] not in opciones:
        eleccionesPC[fichaCambia] = random.choice(opciones)
        print('....',eleccionesPC)
    tablero(fichasJugador, fichasCompu)

def cambiandoFichas(eleccionesPC, eleccionesUsuario, opciones): #Va pidiendo cambio de ficha hasta que alguien gane
    turno = 0
    gana = False
    while not gana:
        if turno%2 != 0:
            cambioFichaPC(eleccionesPC, eleccionesUsuario,opciones)
            turno += 1
            tablero(fichasJugador, fichasCompu)
            gana = ganar()
        else:
            cambioFicha()
            turno += 1
            tablero(fichasJugador, fichasCompu)
            gana = ganar()
    return gana

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
        return False

def volverJuego():
    volverAJugar = int(input("¿Desea volver al juego? (1 = Sí / 2 = No) : "))
    if volverAJugar == 1:
        jugar = True
    elif volverAJugar == 2: 
        jugar = False
    return jugar
#----------------------------------------- PRINCIPAL -------------------------------------------------------------------------------

opciones = [1,2,3,4,5,6,7,8,9]

print ('Bienvenido al juego de 15 en fichas :D')
pantallaDeInicio = input('\n1. JUGAR\n2. COMO JUGAR\n3. SALIR\n\nOPCIÓN: ')
while pantallaDeInicio != '3':
    if pantallaDeInicio == '1':
        jugar = True
        while jugar:
            eleccionesUsuario = []
            eleccionesPC = []
            pc1 = 0
            pc2 = 0
            pc3 = 0
            f1 = 0
            f2 = 0
            f3 = 0
            fichasCompu = ''
            fichasJugador = ''
            iniciar = input('\n¿Quién desea iniciar?\n1.Usuario\n2.Computadora\nSu elección: ')
            if iniciar == '1':
                iniciaUsuario()
                gana = ganar()
            elif iniciar == '2':
                iniciaPC()
                gana = ganar()
            gana = cambiandoFichas(eleccionesPC, eleccionesUsuario,opciones)
            if gana == True:
                jugar = volverJuego()

    elif pantallaDeInicio == '2': 
        print("\nEl juego es simple, primero seleccionas 3 fichas, para ganar, esas fichas \nsumadas deben dar 15. Jugaras contra el computador. \nEl primero que consiga llegar a 15 gana.")
        pantallaDeInicio = input('\n1. JUGAR\n2. COMO JUGAR\n3. SALIR\n\nOPCIÓN: ')

    pantallaDeInicio = input('\n1. JUGAR\n2. COMO JUGAR\n3. SALIR\n\nOPCIÓN: ')
print('Muchas gracias, vuelva pronto')

    