

class Distancia():        

    def __init__(self):
        print("-Constructor-")

    def proceso(self, lista):
        print("proceso")
        n=len(lista)
        distancias=[]

        for i in range(n-1):
            dist= abs((lista[i+1]) - (lista[i]))           
            distancias.append(round(dist,2))
        
        print(distancias)
        n_distancia=len(distancias)

        status=[]
        for i in range(n_distancia-1):
            dist_1=distancias[i]
            dist_2=distancias[i+1]
            if(dist_1 == dist_2):
                pass
            else: 
                status.append(0)

        #Comparar si el arreglo tiene contenido.
        if(len(status)==0):
            iguales=True
        else:
            iguales=False

        return iguales

       
objeto=Distancia()
lista=[194,54,23,7,3,6,8]
print(objeto.proceso(lista))
