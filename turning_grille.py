import numpy as np;

def imprimir_matriz(charar,tamano):
    for i in range(tamano):
        for j in range(tamano):
            print(charar[i][j].decode(), "\t", end='')
        print("\n");

def imprimir_matriz_ex(tamano):
    for i in range(tamano):
        for j in range(tamano):
            msj=str(i)+","+str(j)
            print(msj, "\t", end='')
        print("\n");

def girar_matriz(charar,tamano,sentido):
    n_matriz=np.chararray((tamano,tamano))
    if sentido==2:
        #Antihorario
        auxj = tamano - 1
        for i in range(tamano):
            auxi = tamano - 1
            for j in range(tamano):
                n_matriz[i][auxi]=charar[auxi][auxj]
                auxi-=1
            auxj-=1
    else:
        # Horario
        auxj = tamano - 1
        for i in range(tamano):
            auxi = tamano - 1
            for j in range(tamano):
                n_matriz[i][j] = charar[auxi][i]
                auxi -= 1
            auxj -= 1
    return n_matriz

Rta=int(input("Cifrado Turning Grille.\n\n1. Cifrar\n2. Descifrar\n\nRta: "))

if Rta==1:
    #Cifrar
    #Solicitar Datos
    Texto = input("Por favor introduzca el texto a cifrar: ");
    #Texto="jim attacksatdawn"
    Texto = Texto.upper().strip().replace(" ", "");
    tamano=int(input("Por favor introduzca el tamaño de la reticula: "))
    #tamano=4
    Reticula = np.chararray((tamano, tamano));
    Reticula[:]="*"


    print("La reticula está compuesta por una serie de posiciones de la forma i,j desde 0 hasta n-1 siendo n el tamaño de la reticula, por favor ingrese las coordenadas i,j que desea perforar\n")

    while True:

        print("Ingrese la posición para agregar agujero\n")
        imprimir_matriz_ex(tamano)
        i=int(input("Posición i: "))
        j=int(input("Posición j: "))
        Reticula[i][j]="O"
        print("Reticula actual\n")
        imprimir_matriz(Reticula, tamano)

        rta2=int(input("¿Desea agregar otro agujero?\n1. Si\n2. No\n\nRta: "))
        if rta2==1:
            continue
        else:
            break;

    imprimir_matriz(Reticula, tamano)

    rta2 = int(input("¿En que sentido desea cifrar?\n1. Sentido horario\n2. Sentido antihorario\n\nRta: "))
    m_res=np.chararray((tamano,tamano));

    aux=0
    for k in range(4):
        for i in range(tamano):
            for j in range(tamano):
                if Reticula[i][j]==b'O':
                    m_res[i][j]=Texto[aux]
                    aux += 1
        Reticula = girar_matriz(Reticula, tamano, rta2)
    print("\nMatriz resultado\n")
    imprimir_matriz(m_res,tamano)

    print("\nTexto Cifrado\n")
    for i in range(tamano):
        for j in range(tamano):
            print(m_res[i][j].decode()," ",end="")
        print("\t",end="")


else:
    #Descifrar
    # Solicitar Datos
    Texto = input("Por favor introduzca el texto a descifrar: ");
    #Texto="JKTD SAAT WIAM CNAT"
    Texto = Texto.upper().strip().replace(" ", "");

    tamano = int(input("Por favor introduzca el tamaño de la reticula: "))
    #tamano=4

    Reticula = np.chararray((tamano, tamano));
    Reticula[:] = "*"


    print("La reticula está compuesta por una serie de posiciones de la forma i,j desde 0 hasta n-1 siendo n el tamaño de la reticula, por favor ingrese las coordenadas i,j que desea perforar\n")

    while True:

        print("Ingrese la posición para agregar agujero\n")
        imprimir_matriz_ex(tamano)
        i = int(input("Posición i: "))
        j = int(input("Posición j: "))
        Reticula[i][j] = "O"
        print("Reticula actual\n")
        imprimir_matriz(Reticula, tamano)

        rta2 = int(input("¿Desea agregar otro agujero?\n1. Si\n2. No\n\nRta: "))
        if rta2 == 1:
            continue
        else:
            break;
            """
    Reticula[0][0] = "O"
    Reticula[0][3] = "O"
    Reticula[0][5] = "O"
    Reticula[1][2] = "O"
    Reticula[1][8] = "O"
    Reticula[2][1] = "O"
    Reticula[2][6] = "O"
    Reticula[3][2] = "O"
    Reticula[3][4] = "O"
    Reticula[3][7] = "O"
    Reticula[4][4] = "O"
    Reticula[4][6] = "O"
    Reticula[4][8] = "O"
    Reticula[5][3] = "O"
    Reticula[5][7] = "O"
    Reticula[6][0] = "O"
    Reticula[6][5] = "O"
    Reticula[7][1] = "O"
    Reticula[7][4] = "O"
    Reticula[7][8] = "O"
    Reticula[8][2] = "O"
    """
    

    m_ciph=np.chararray((tamano,tamano))
    aux=0

    for i in range(tamano):
        for j in range(tamano):
            try:
                m_ciph[i][j]=Texto[aux]
                aux+=1
            except:
                m_ciph[i][j]="_"

    print("Reticula\n")
    imprimir_matriz(Reticula, tamano)
    print("\nMatriz de texto cifrado\n")
    imprimir_matriz(m_ciph, tamano)

    rta2 = int(input("¿En que sentido desea descifrar?\n1. Sentido horario\n2. Sentido antihorario\n\nRta: "))
    m_res = np.chararray((tamano, tamano));

    Descifrado=""
    for k in range(4):
        for i in range(tamano):
            for j in range(tamano):
                if Reticula[i][j] == b'O':
                    Descifrado+=m_ciph[i][j].decode()
                    #aux += 1
        Reticula = girar_matriz(Reticula, tamano, rta2)
    print("\nTexto descifrado\n",Descifrado)


