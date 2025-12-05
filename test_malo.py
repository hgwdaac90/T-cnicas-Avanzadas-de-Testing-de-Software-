from busqueda import busqueda_binaria

lista = [1, 2, 3, 4, 5]

print("--- Ejecutando Test Completo ---")
# 1. Encontrar (Camino if)
busqueda_binaria(lista, 3)
# 2. Buscar derecha (Camino elif)
busqueda_binaria(lista, 5)
# 3. Buscar izquierda (Camino else)
busqueda_binaria(lista, 1)
# 4. No encontrar (Camino return -1)
busqueda_binaria(lista, 20)

print("¡Todos los caminos recorridos!")