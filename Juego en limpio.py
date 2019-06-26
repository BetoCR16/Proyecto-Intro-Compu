import random
#------------------------------ Tablero --------------------------------------------
def tablero():
    print("\n"*50)
    cinta()

def cinta():
    numeros= ['| 1  |','| 2  |','| 3  |','| 4  |','| 5  |','| 6  |','| 7  |','| 8  |','| 9  |']
    cinta = ['| __ |','| __ |','| __ |','| __ |','| __ |','| __ |','| __ |','| __ |','| __ |']
    n = 0
    n2 = 0

    for i in eleccionesUsuario:  #Pone una U en los lugares de las fichas del usuario
        if i in opciones:
            indice = opciones.index(i)
            n += 1
            cinta[indice] = '| U'+ str(n)+' |'

    for i in eleccionesPC: #Pone una C en los lugares de las fichas de la compu
        if i in opciones:
            indice = opciones.index(i)
            n2 += 1
            cinta[indice] = '| C'+ str(n2)+ ' |'

    print(numeros)
    print(cinta)

#------------------------------Revisión de elecciones-------------------------------
def revisarEleccion(): #Evita que el usuario ponga otra cosa que no sea un número del 1 al 9 y evita que se repitan fichas
    eleccion = int(input('\nSeleccione una ficha: '))
    while len(str(eleccion)) != 1 or str(eleccion) not in '123456789' or eleccion in eleccionesUsuario or eleccion in eleccionesPC:
        eleccion = int(input('Ficha no válida. Seleccione otra ficha: '))
    return eleccion

def revisarEleccionPC(): #Evita que la compu repita una ficha que ya haya usado o que el usuario haya usado
    pc = random.choice(opciones)
    while pc in eleccionesUsuario or pc in eleccionesPC:
        pc = random.choice(opciones)
    return pc

#------------------------------ Inicio ----------------------------------------------
def iniciaUsuario(): #Primer turno si va a iniciar primero el usuario
    f1 = revisarEleccion()
    eleccionesUsuario.append(f1)
    tablero()
    
    pc1 = revisarEleccionPC()
    eleccionesPC.append(pc1)
    tablero()
    
    f2 = revisarEleccion()
    eleccionesUsuario.append(f2)
    tablero()
    
    pc2 = 15 - (f1 + f2)
    while pc2 in eleccionesUsuario or pc2 in eleccionesPC or str(pc2) not in '123456789':
        pc2 = random.choice(opciones)
    eleccionesPC.append(pc2)
    tablero()
    
    f3 = revisarEleccion()
    eleccionesUsuario.append(f3)
    tablero()
    
    pc3 = 15 - sumaPC(eleccionesPC)
    while pc3 in eleccionesUsuario or pc3 in eleccionesPC or str(pc3) not in '123456789':
        pc3 = random.choice(opciones)
    eleccionesPC.append(pc3)
    tablero()

def iniciaPC(): #Primer turno si va a iniciar primero la computadora    
    pc1 = revisarEleccionPC()
    eleccionesPC.append(pc1)
    tablero()

    f1 = revisarEleccion()
    eleccionesUsuario.append(f1)
    tablero()

    pc2 = revisarEleccionPC()
    eleccionesPC.append(pc2)
    tablero()

    f2 = revisarEleccion()
    eleccionesUsuario.append(f2)
    tablero()
    
    pc3 = 15 - (f1 + f2)
    while pc3 in eleccionesUsuario or pc3 in eleccionesPC or str(pc3) not in '123456789':
        pc3 = random.choice(opciones)
    eleccionesPC.append(pc3)
    tablero()

    f3 = revisarEleccion()
    eleccionesUsuario.append(f3)
    tablero()

#-----------------------------Cambio de fichas---------------------------------------
def cambioFichaUsuario(): #Pide la ficha a cambiar y la cambia por otra
    fichaCambia = int(input('\n¿Cuál ficha desea cambiar?\nFicha #: '))
    eleccionesUsuario[fichaCambia - 1] = int(input('Nueva posición de ficha: '))

def cambioFichaPC():
    fichaCambia = random.randint(0,2)
    print('Cambia: ', fichaCambia+1)
    eleccionesPC[fichaCambia] = 0
    eleccionesPC[fichaCambia] = 15 - sumaPC(eleccionesPC)
    print('....',eleccionesPC)
    while eleccionesPC[fichaCambia] in eleccionesUsuario or eleccionesPC[fichaCambia] not in opciones:
        eleccionesPC[fichaCambia] = random.choice(opciones)
        print('....',eleccionesPC)
    tablero()

def cambiandoFichas(): #Va pidiendo cambio de ficha hasta que alguien gane
    turno = 0
    gana = False
    while not gana:
        if turno%2 != 0:
            cambioFichaPC()
            turno += 1
            tablero()
            gana = ganar()
        else:
            cambioFichaUsuario()
            turno += 1
            tablero()
            gana = ganar()
    return gana

#----------------------------Definir gane--------------------------------------------
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

#--------------------------------Volver a jugar--------------------------------------
def volverAJugar():
    volverAlJuego = int(input("¿Desea volver al juego? (1 = Sí / 2 = No) : "))
    if volverAlJuego == 1:
        jugar = True
    elif volverAlJuego == 2: 
        jugar = False
    return jugar

#----------------------------------- Programa Principal -----------------------------
print ('Bienvenido al juego de 15 en fichas :D')
pantallaDeInicio = input('\n1. JUGAR\n2. COMO JUGAR\n3. SALIR\n\nOPCIÓN: ')
while pantallaDeInicio != '3':
    if pantallaDeInicio == '1':
        jugar = True
        while jugar:
            opciones = [1,2,3,4,5,6,7,8,9]
            eleccionesUsuario = []
            eleccionesPC = []
            pc1 = 0
            pc2 = 0
            pc3 = 0
            f1 = 0
            f2 = 0
            f3 = 0
            iniciar = input('\n¿Quién desea iniciar?\n1.Usuario\n2.Computadora\nSu elección: ')
            if iniciar == '1':
                iniciaUsuario()
                gana = ganar()
            elif iniciar == '2':
                iniciaPC()
                gana = ganar()
            if gana == True:
                jugar = volverAJugar() 
            else:
                cambiandoFichas()
                jugar = volverAJugar()  

    elif pantallaDeInicio == '2': 
        print("\nEl juego es simple, primero seleccionas 3 fichas, para ganar, esas fichas \nsumadas deben dar 15. Jugaras contra el computador. \nEl primero que consiga llegar a 15 gana.")
        pantallaDeInicio = input('\n1. JUGAR\n2. COMO JUGAR\n3. SALIR\n\nOPCIÓN: ')

    pantallaDeInicio = input('\n1. JUGAR\n2. COMO JUGAR\n3. SALIR\n\nOPCIÓN: ')
print('Muchas gracias, vuelva pronto')