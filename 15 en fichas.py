import random

def revisarEleccion():
    eleccion = input('Elija un número de 1 a 9: ')
    while len(eleccion) != 1 or eleccion not in '123456789' or eleccion in f1 or eleccion in f2 \
        or eleccion in f3 or eleccion in pc1 or eleccion in pc2 or eleccion in pc3:
        eleccion = input('Elija un número de 1 a 9: ')
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
    

#----------------------------------------- PRINCIPAL -------------------------------------------------------------------------------

opciones = ['1','2','3','4','5','6','7','8','9']
pc1 = '7'
pc2 = '6'
pc3 = '2'
f1 = '9'
f2 = '6'
f3 = '1'

ganar(f1,f2,f3,pc1,pc2,pc3)