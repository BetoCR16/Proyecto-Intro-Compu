import random


# ------------------------------ Tablero --------------------------------------------
def tablero():
    print("\n" * 50)
    cinta()


def cinta():
    numeros = ['| 1  |', '| 2  |', '| 3  |', '| 4  |', '| 5  |', '| 6  |', '| 7  |', '| 8  |', '| 9  |']
    cinta = ['| __ |', '| __ |', '| __ |', '| __ |', '| __ |', '| __ |', '| __ |', '| __ |', '| __ |']
    n = 0
    n2 = 0

    for i in eleccionesUsuario:  # Pone una U en los lugares de las fichas del usuario
        if i in opciones:
            indice = opciones.index(i)
            n += 1
            cinta[indice] = '| U' + str(n) + ' |'

    for i in eleccionesPC:  # Pone una C en los lugares de las fichas de la compu
        if i in opciones:
            indice = opciones.index(i)
            n2 += 1
            cinta[indice] = '| C' + str(n2) + ' |'

    print(numeros)
    print(cinta)


# ------------------------------Revisi�n de elecciones-------------------------------
def revisarEleccion():  # Evita que el usuario ponga otra cosa que no sea un n�mero del 1 al 9 y evita que se repitan fichas
    eleccion = int(input('\nSeleccione una ficha: '))
    while len(str(eleccion)) != 1 or str(
            eleccion) not in '123456789' or eleccion in eleccionesUsuario or eleccion in eleccionesPC:
        eleccion = int(input('Ficha no válida. Seleccione otra ficha: '))
    return eleccion


def revisarEleccionPC():  # Evita que la compu repita una ficha que ya haya usado o que el usuario haya usado
    pc = random.choice(opciones)
    while pc in eleccionesUsuario or pc in eleccionesPC:
        pc = random.choice(opciones)
    return pc


# ------------------------------ Inicio ----------------------------------------------
def iniciaUsuario(turno):  # Primer turno si va a iniciar primero el usuario
    turno = 1
    f1 = revisarEleccion()
    eleccionesUsuario.append(f1)
    turno += 1
    tablero()

    pc1 = revisarEleccionPC()
    eleccionesPC.append(pc1)
    turno += 1
    tablero()

    f2 = revisarEleccion()
    eleccionesUsuario.append(f2)
    turno += 1
    tablero()

    pc2 = 15 - (f1 + f2)
    while pc2 in eleccionesUsuario or pc2 in eleccionesPC or pc2 not in opciones:
        pc2 = random.choice(opciones)
    eleccionesPC.append(pc2)
    turno += 1
    tablero()

    f3 = revisarEleccion()
    eleccionesUsuario.append(f3)
    turno += 1
    tablero()

    pc3 = 15 - sumaPC(eleccionesPC)
    while pc3 in eleccionesUsuario or pc3 in eleccionesPC or str(pc3) not in '123456789':
        pc3 = random.choice(opciones)
    eleccionesPC.append(pc3)
    turno += 1
    tablero()

    return turno

def iniciaPC(turno):  # Primer turno si va a iniciar primero la computadora
    pc1 = revisarEleccionPC()
    eleccionesPC.append(pc1)
    turno += 1
    tablero()

    f1 = revisarEleccion()
    eleccionesUsuario.append(f1)
    turno += 1
    tablero()

    pc2 = revisarEleccionPC()
    eleccionesPC.append(pc2)
    while sumaPC(eleccionesPC) >= 15:
        pc2 = revisarEleccionPC()
        eleccionesPC[1] = pc2
    if 15 - sumaPC(eleccionesPC) in eleccionesUsuario and 15 - sumaPC(eleccionesPC) in eleccionesPC:
        pc2 = revisarEleccionPC()
        eleccionesPC[1] = pc2
    turno += 1
    tablero()

    f2 = revisarEleccion()
    eleccionesUsuario.append(f2)
    turno += 1
    tablero()

    pc3 = 15 - sumaPC(eleccionesPC)
    if 14 >= sumaU(eleccionesUsuario) >= 6 :
        pc3 = 15 - sumaU(eleccionesUsuario)
        while pc3 in eleccionesUsuario or pc3 in eleccionesPC or pc3 not in opciones:
            pc3 = revisarEleccionPC()
    eleccionesPC.append(pc3)
    turno += 1
    tablero()

    f3 = revisarEleccion()
    eleccionesUsuario.append(f3)
    turno += 1
    tablero()

    return turno


# -----------------------------Cambio de fichas---------------------------------------
def cambioFichaUsuario():  # Pide la ficha a cambiar y la cambia por otra
    fichaCambia = input('\n¿Cuál ficha desea cambiar?\nFicha (1,2 o 3): ')
    while fichaCambia not in '123' or fichaCambia == '':
        fichaCambia = input('\nNúmero de ficha no es válido\n¿Cuál ficha desea cambiar?\nFicha (1,2 o 3): ')
    fichaVieja = eleccionesUsuario[int(fichaCambia) - 1]
    fichaNueva = int(input('Nueva posición de ficha: '))
    while fichaNueva in eleccionesPC or fichaNueva in eleccionesUsuario\
    or fichaNueva == fichaVieja:
        fichaNueva = int(input('\nFicha inválida\nDigite otra posición de ficha: ' ))
        print (eleccionesUsuario)
    eleccionesUsuario[int(fichaCambia) - 1] = fichaNueva

def cambioFichaPC(eleccionesPC):
    fichaCambia = random.randint(0, 2)
    fichaVieja = eleccionesPC[fichaCambia]
    eleccionesPC[fichaCambia] = 0
    eleccionesPC[fichaCambia] = 15 - sumaPC(eleccionesPC)
    fichaNueva = eleccionesPC[fichaCambia]
    while fichaNueva in eleccionesUsuario or fichaNueva in eleccionesPC or fichaNueva not in opciones or fichaNueva == fichaVieja:
        fichaNueva = revisarEleccionPC()
    eleccionesPC[fichaCambia] = fichaNueva
    tablero()
    return fichaCambia

def cambiandoFichas(turno):  # Va pidiendo cambio de ficha hasta que alguien gane
    gana = False
    while not gana:
        if turno % 2 == 0:
            fichaCambia = cambioFichaPC(eleccionesPC)
            turno += 1
            tablero()
            print('Computadora cambió de posición la ficha: ' + str(fichaCambia+1))
            gana = ganar(eleccionesPC, eleccionesUsuario)
        else:
            cambioFichaUsuario()
            turno += 1
            tablero()
            gana = ganar(eleccionesPC, eleccionesUsuario)
    return gana


# ----------------------------Definir gane--------------------------------------------
def sumaPC(eleccionesPC):  # Realiza la suma de las fichas de la compu
    sumaPC = 0
    for i in eleccionesPC:
        sumaPC += i
    return sumaPC


def sumaU(eleccionesUsuario):  # Suma las fichas del usuario
    sumaU = 0
    for i in eleccionesUsuario:
        sumaU += i
    return sumaU


def ganar(eleccionesPC, eleccionesUsuario):  # Define si alguien gana o no
    sumaUsuario = sumaU(eleccionesUsuario)
    sumaCompu = sumaPC(eleccionesPC)
    if sumaCompu == sumaUsuario and sumaCompu == 15 and sumaUsuario == 15:
        print('\nEmpate')
        return True
    elif sumaCompu == 15:
        print('\nGana compu')
        return True
    elif sumaUsuario == 15:
        print('\nGana usuario')
        return True
    else:
        return False


# --------------------------------Volver a jugar--------------------------------------
def volverAJugar():
    volverAlJuego = int(input("¿Desea volver al juego? (1 = Sí / 2 = No) : "))
    if volverAlJuego not in range(1, 3):
        volverAlJuego = int(input("\nSeleccione un opcion valida\n¿Desea volver al juego? (1 = Sí / 2 = No) : "))
    if volverAlJuego == 1:
        jugar = True
    elif volverAlJuego == 2:
        jugar = False
    return jugar


# ----------------------------------- Programa Principal -----------------------------
print('Bienvenido al juego de 15 en fichas :D', "\nElije una opcion")
pantallaDeInicio = input('\n1. JUGAR\n2. COMO JUGAR\n3. SALIR\n\nDigita el numero de la opcion deseada: \n')
while pantallaDeInicio != '3':
    if pantallaDeInicio == '1':
        jugar = True
        while jugar == True:
            opciones = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            eleccionesUsuario = []
            eleccionesPC = []
            pc1 = 0
            pc2 = 0
            pc3 = 0
            f1 = 0
            f2 = 0
            f3 = 0
            turno = 0
            iniciar = input('\n¿Quién desea iniciar?\n1.Usuario\n2.Computadora\nSu elección: ')
            if iniciar == '1':
                tablero()
                turno = iniciaUsuario(turno)
                print(turno)
                gana = ganar(eleccionesPC, eleccionesUsuario)
            elif iniciar == '2':
                tablero()
                turno = iniciaPC(turno)
                print(turno)
                gana = ganar(eleccionesPC, eleccionesUsuario)
            if gana == True:
                jugar = volverAJugar()
            else:
                cambiandoFichas(turno)
                jugar = volverAJugar()
            if jugar == False:
                pantallaDeInicio = '3'
    elif pantallaDeInicio == '2':
        print(
            "\nEl juego es simple, primero seleccionas 3 fichas. Para ganar, esas fichas \nsumadas deben dar 15. Jugaras contra el computador. \nEl primero que consiga llegar a 15 con 3 fichas gana.")
        print("Aparecera una fila de numeros con espacios en blanco debajo, esto seran las fichas a elegir.\nCuando selecciones una ficha aparecera debajo de ella una 'U' marcando que la seleccionaste")
        print("Asi como tambien aparecera una 'C' indicando la seleccionada por el computador")
        print("Si ninguno gana tras elegir 3 fichas, podran cambiar una ficha por turno hasta que alguno gane,\n para cambiar la ficha escribe el numero de ficha a cambiar y luego selecciona una nueva\n¡A divertirnos!")
        pantallaDeInicio = input('\n1. JUGAR\n2. COMO JUGAR\n3. SALIR\n\nDigita el numero de la opcion deseada: \n')
    if pantallaDeInicio == '':
        print("Escribe una opcion")
        pantallaDeInicio = input('\n1. JUGAR\n2. COMO JUGAR\n3. SALIR\n\nDigita el numero de la opcion deseada: \n')
    if pantallaDeInicio == '3':
        print("\nGracias por jugar\nVuelve pronto\n\nCreadores: Roberto Méndez & Daniel Calero")