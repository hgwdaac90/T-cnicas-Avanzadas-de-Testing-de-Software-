def busqueda_binaria(lista, objetivo):
    bajo = 0
    alto = len(lista) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        
        # Si lo encuentra va al (Camino 1)
        if lista[medio] == objetivo:
            return medio
        # Si es mayor, busca en la derecha (Camino 2)
        elif lista[medio] < objetivo:
            bajo = medio + 1
        # Si es menor, busca en la izquierda (Camino 3)
        else:
            alto = medio - 1
            
    return -1 # Si no existe va al (Camino 4)