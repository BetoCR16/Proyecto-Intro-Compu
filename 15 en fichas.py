import random

def revisarEleccion():
    eleccion = input('Elija un número de 1 a 9: ')
    while len(eleccion) != 1 or eleccion not in '123456789' or eleccion in pc1\
          or eleccion in pc2 or eleccion in pc3 or eleccion in str(f1)\
          or eleccion in str(f2) or eleccion in str(f3):
        eleccion = input('Elija un número de 1 a 9: ')
    return eleccion

def revisarEleccionCompu(f1,f2,f3):
    eleccionPC = random.choice(opciones)
    while eleccionPC in str(f1) or eleccionPC in str(f2)\
        or eleccionPC in str(f3) or eleccionPC in pc1 or eleccionPC in pc2 or eleccionPC in pc3:
        eleccionPC = random.choice(opciones) 
    return eleccionPC

def preguntaInicio():
    iniciar = input('¿Quién desea iniciar?\n1.Usuario\n2.Computadora\nSu elección: ')
    return iniciar

def ganar(f1,f2,f3,pc1,pc2,pc3):
    sumaUsuario = int(f1) + int(f2) + int(f3)
    sumaCompu = int(pc1) + int(pc2) + int(pc3)
    if sumaCompu == 15:
        print ('Gana compu')
        jugar = False
    elif sumaUsuario == 15:
        print('Gana usuario')
        jugar = False
    return jugar
    

def tablero(turno, fichasJugador, fichasCompu):
    print('Turno: ', turno)
    print('Fichas de usuario: ' + str(f1) + ' ' + str(f2) + ' ' + str(f3))
    print('Fichas de computadora: ' + str(pc1) + ' ' + str(pc2) + ' ' + str(pc3))
    

#----------------------------------------- PRINCIPAL -------------------------------------------------------------------------------

opciones = ['1','2','3','4','5','6','7','8','9']
continuar = True

while continuar:
    pc1 = '0'
    pc2 = '0'
    pc3 = '0'
    f1 = 0
    f2 = 0
    f3 = 0
    turno = 0
    fichasCompu = ''
    fichasJugador = ''
    jugar = True
    tablero(turno, fichasJugador, fichasCompu)
    f1 = revisarEleccion()
    pc1 = revisarEleccionCompu(f1,f2,f3)
    print('\nElección de computadora: ', pc1,'\n')
    f2 = revisarEleccion()
    pc2 = revisarEleccionCompu(f1,f2,f3)
    print('\nElección de computadora: ', pc2,'\n')
    f3 = revisarEleccion()
    pc3 = revisarEleccionCompu(f1,f2,f3)
    print('\nElección de computadora: ', pc3,'\n')
    turno += 1
    fichasJugador = f1,f2,f3
    fichasCompu = pc1, pc2, pc3
    tablero(turno, fichasJugador, fichasCompu)
    continuar = False
