import random
def comoJugar():
    """ 
    El juego es simple, primero seleccionas 3 fichas. Para ganar, 
    esas fichas sumadas deben dar 15. Jugarás contra el computador.
    El primero que consiga llegar a 15 con 3 fichas gana.

    Aparecera una fila de números con espacios en blanco debajo, 
    estas serán las fichas a elegir. Cuando selecciones una ficha 
    aparecera debajo de ella una 'U', marcando que la seleccionaste
    Así como también aparecerá una 'C' indicando la seleccionada por 
    el computador. 

    Si ninguno gana tras elegir 3 fichas, podrán cambiar 
    una ficha por turno hasta que alguno gane, para cambiar 
    la ficha escribe el número de ficha a cambiar y luego
    selecciona una nueva.

    ¡A divertirnos!
    """


# ------------------------------ Tablero --------------------------------------------
def tablero():
    print("\n" * 50)
    cinta()


def cinta():
    numeros = ['|  1  |', '|  2  |', '|  3  |', '|  4  |', '|  5  |', '|  6  |', '|  7  |', '|  8  |', '|  9  |']
    espacio = ['|     |', '|     |', '|     |', '|     |', '|     |', '|     |', '|     |', '|     |', '|     |']
    cinta = ['|  _  |', '|  _  |', '|  _  |', '|  _  |', '|  _  |', '|  _  |', '|  _  |', '|  _  |', '|  _  |']
    n = 0
    n2 = 0

    for i in eleccionesUsuario:  # Pone una U en los lugares de las fichas del usuario
        if i in opciones:
            indice = opciones.index(i)
            n += 1
            cinta[indice] = '|  U' + '  |'

    for i in eleccionesPC:  # Pone una C en los lugares de las fichas de la compu
        if i in opciones:
            indice = opciones.index(i)
            n2 += 1
            cinta[indice] = '|  C'+ '  |'

    print(numeros)
    print(espacio)
    print(cinta)


# ------------------------------Revisi�n de elecciones-------------------------------
def revisarEleccion():  # Evita que el usuario ponga otra cosa que no sea un n�mero del 1 al 9 y evita que se repitan fichas
    eleccion = input('\nSeleccione una ficha: ')
    while len(eleccion) != 1 or eleccion not in '123456789' or eleccion in str(eleccionesUsuario) or eleccion in str(eleccionesPC) or eleccion == '':
        eleccion = input('Ficha no válida. Seleccione otra ficha: ')
    return int(eleccion)


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
    print('\nLa computadora eligió la ficha: ',pc1)

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
    print('\nLa computadora eligió la ficha: ',pc2)

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
    print('\nLa computadora eligió la ficha: ',pc3)

    return turno

def iniciaPC(turno):  # Primer turno si va a iniciar primero la computadora
    pc1 = revisarEleccionPC()
    eleccionesPC.append(pc1)
    turno += 1
    tablero()
    print('\nLa computadora eligió la ficha: ',pc1)

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
    print('\nLa computadora eligió la ficha: ',pc2)

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
    print('\nLa computadora eligió la ficha: ',pc3)

    f3 = revisarEleccion()
    eleccionesUsuario.append(f3)
    turno += 1
    tablero()

    return turno

# -----------------------------Cambio de fichas---------------------------------------
def cambioFichaUsuario():  # Pide la ficha a cambiar y la cambia por otra
    numFicha = input('\n¿Cuál posición de ficha desea cambiar?\nFicha en la posición: ')
    while numFicha not in str(eleccionesUsuario) or numFicha == '':
        numFicha = input('\nNúmero de ficha no es válido\n¿Cuál posición de ficha desea cambiar?\nFicha en la posición: ')
    fichaCambia = eleccionesUsuario.index(int(numFicha))
    fichaVieja = eleccionesUsuario[fichaCambia]
    fichaNueva = int(input('Nueva posición de ficha: '))
    while fichaNueva in eleccionesPC or fichaNueva in eleccionesUsuario\
    or fichaNueva == fichaVieja:
        fichaNueva = int(input('\nPosición de ficha inválida.\nDigite otra posición de ficha: ' ))
    eleccionesUsuario[fichaCambia] = fichaNueva

def busquedaDeFichaConveniente():
    cambiarFicha = 0
    suma1 = eleccionesPC[0]+eleccionesPC[1]
    suma2 = eleccionesPC[0]+eleccionesPC[2]
    suma3 = eleccionesPC[1]+eleccionesPC[2]
    if (15 - suma1) not in eleccionesPC and (15 - suma1) not in eleccionesUsuario and (15 - suma1) > 0:
        cambiarFicha = 2
    elif (15 - suma2) not in eleccionesPC and (15 - suma2) not in eleccionesUsuario and (15 - suma2) > 0:
        cambiarFicha = 1
    elif (15 - suma3) not in eleccionesPC or (15 - suma3) not in eleccionesUsuario and (15 - suma3) > 0:
        cambiarFicha = 0
    else:
        if suma1 > suma2 and suma1 < 15:
            if suma1 > suma3:
                cambiarFicha = 2
            elif suma3 < 15:
                cambiarFicha = 0
            else: 
                cambiarFicha = random.randint(0,2)
        elif suma2 > suma3 and suma2 < 15:
            cambiarFicha = 1
        elif suma3 < 15:
            cambiarFicha = 0
        else: 
            cambiarFicha = random.randint(0,2)
    return cambiarFicha

def cambioFichaPC(eleccionesPC):
    fichaCambia = busquedaDeFichaConveniente()
    fichaVieja = eleccionesPC[fichaCambia]
    eleccionesPC[fichaCambia] = 0
    fichaNueva = 15 - sumaPC(eleccionesPC)
    while fichaNueva in eleccionesUsuario or fichaNueva in eleccionesPC or fichaNueva not in opciones or fichaNueva == fichaVieja:
        fichaNueva = revisarEleccionPC()
    eleccionesPC[fichaCambia] = fichaNueva
    tablero()
    return fichaVieja,fichaNueva

def cambiandoFichas(turno):  # Va pidiendo cambio de ficha hasta que alguien gane
    gana = False
    while not gana:
        if turno % 2 == 0:
            fichaVieja,fichaNueva = cambioFichaPC(eleccionesPC)
            turno += 1
            tablero()
            print('\nComputadora cambió una ficha de la posición '+str(fichaVieja)+' hacia la posición '+str(fichaNueva)+'.')
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
        print('\nGana computadora\n')
        return True
    elif sumaUsuario == 15:
        print('\nGana usuario')
        return True
    else:
        return False


# --------------------------------Volver a jugar--------------------------------------
def volverAJugar():
    volverAlJuego = input("¿Desea volver al juego? (1 = Sí / 2 = No) : ")
    while volverAlJuego not in '12' or volverAlJuego == '': 
        volverAlJuego = int(input("\nSeleccione una opción válida\n¿Desea volver a jugar? (1 = Sí / 2 = No) : "))
    if volverAlJuego == '1':
        jugar = True
    elif volverAlJuego == '2':
        jugar = False
    return jugar


# ----------------------------------- Programa Principal -----------------------------
print('Bienvenido al juego de 15 en fichas :D', "\nElije una opción")
pantallaDeInicio = input('\n1. JUGAR\n2. CÓMO JUGAR\n3. SALIR\n\nDigita el número de la opción deseada: \n')
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
                gana = ganar(eleccionesPC, eleccionesUsuario)
            elif iniciar == '2':
                tablero()
                turno = iniciaPC(turno)
                gana = ganar(eleccionesPC, eleccionesUsuario)
            if gana == True:
                jugar = volverAJugar()
            else:
                cambiandoFichas(turno)
                jugar = volverAJugar()
            if jugar == False:
                pantallaDeInicio = '3'
    elif pantallaDeInicio == '2':
        print(comoJugar.__doc__)
        print('_'*50)
    pantallaDeInicio = input('\nMENÚ PRINCIPAL\n\n1. JUGAR\n2. CÓMO JUGAR\n3. SALIR\n\nDigita el número de la opción deseada: \n')
    if pantallaDeInicio == '' or pantallaDeInicio not in '123':
        print("OPCIÓN NO VÁLIDA")
        print('_'*50)
        pantallaDeInicio = input('\nMENÚ PRINCIPAL\n\n1. JUGAR\n2. CÓMO JUGAR\n3. SALIR\n\nDigita el número de la opción deseada: \n')
    if pantallaDeInicio == '3':
        print("\nGracias por usar este programa.\n¡Que tenga un lindo día!\nVuelva pronto :D\n\nCreadores: Roberto Méndez & Daniel Calero")