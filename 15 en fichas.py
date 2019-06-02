import random
def revisarEleccion():
    eleccion = input('Elija un número de 1 a 9: ')
    while len(eleccion) != 1 or eleccion not in '123456789':
        eleccion = input('Elija un número de 1 a 9: ')
    return eleccion

def preguntaInicio():
    iniciar = input('¿Quién desea iniciar?\n1.Usuario\n2.Computadora\nSu elección: ')
    return iniciar

def tablero(turno, numDisponible, numCompu, numUsuario):
    print (turno)
    





opciones = ['1','2','3','4','5','6','7','8','9']

inicio = preguntaInicio()
if inicio == '1':
    f1 = revisarEleccion()
elif inicio == '2':
    pc1 = random.choice(opciones)

pc2 = random.choice(opciones)

f2 = revisarEleccion()
f3 = revisarEleccion()