import random

def revisarEleccion():
    eleccion = input('Elija un número de 1 a 9: ')
    while len(eleccion) != 1 or eleccion not in '123456789':
        eleccion = input('Elija un número de 1 a 9: ')
    return eleccion

def revisarEleccionPC():
    eleccion = random.choice(opciones)
    while eleccion in f1 or eleccion in f2 or eleccion in f3 or eleccion in pc1 or eleccion in pc2 or eleccion in pc3:
        eleccion = random.choice(opciones)
    return eleccion

def preguntaInicio():
    iniciar = input('¿Quién desea iniciar?\n1.Usuario\n2.Computadora\nSu elección: ')
    return iniciar

def ganar(f1,f2,f3,pc1,pc2,pc3):
    f1 = int(f1)
    f2 = int(f2)
    f3 = int(f3)
    pc1 = int(pc1)
    pc2 = int(pc2)
    pc3 = int(pc3)
    sumaUsuario = f1 + f2 + f3
    sumaCompu = pc1 + pc2 + pc3
    if sumaCompu == 15:
        print ('Gana compu') 
    elif sumaUsuario == 15:
        print('Gana usuario')

def tablero(turno, fichasJugador, fichasCompu):
    print('Turno: ', turno)
    print('Fichas de usuario: ' + str(f1) + ' ' + str(f2) + ' ' + str(f3))
    print('Fichas de computadora: ' + str(pc1) + ' ' + str(pc2) + ' ' + str(pc3))


#----------------------------------------- PRINCIPAL -------------------------------------------------------------------------------

opciones = ['1','2','3','4','5','6','7','8','9']
continuar = True

while continuar:
    pc1 = 0
    pc2 = 0
    pc3 = 0
    f1 = 0
    f2 = 0
    f3 = 0
    turno = 0
    fichasCompu = ''
    fichasJugador = ''
    while True:
        tablero(turno, fichasJugador, fichasCompu)
        f1 = str(revisarEleccion())
        pc1 = random.choice(opciones)
        f2 = str(revisarEleccion())
        pc2 = random.choice(opciones)
        f3 = str(revisarEleccion())
        pc3 =random.choice(opciones) 
        turno += 1
        fichasJugador = f1,f2,f3
        fichasCompu = pc1, pc2, pc3


    


