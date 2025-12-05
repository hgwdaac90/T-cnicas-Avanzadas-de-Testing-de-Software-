def calcular_descuento_final(precio, es_vip):
    
    # --- ERROR GRAVE AQUÍ ARRIBA ---
    # Estoy tratando de sumar una variable que NO EXISTE.
    # VS Code TIENE que marcar esto en Rojo o Amarillo.
    total = variable_fantasma + 100

    # Variables que no se usan (deberían verse grises)
    impuesto_extra = 0.15 
    descuento = 10
    descuento = 0 

    if precio < 0:
        return 0
    
    if es_vip:
        return precio * 0.8
    else:
        return precio * 0.9