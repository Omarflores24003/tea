try:
    #defino programas
    def mostrarmaximo(m):
        print("∖nEl numero maximo es: ",m)

    def mostrarminimo(M):
        print("∖nEl numero minimo es: ",M)

    def pedirdato():
        minimo=None
        maximo=None
        while True:
            n=input("Ingrese un numero: ")
            if n=="fin":
                break
            if maximo is None or n>maximo:
                maximo=n 
            if minimo is None or n <minimo:
                minimo=n
        mostrarmaximo(maximo)
        mostrarminimo(minimo)
#Comienza Programa
    pedirdato()
#Fin del programa
except:
    print("∖nError!! Ingrese un numero o la palabra (Fin) ∖nE1 prgrama ha finalizado")
    



