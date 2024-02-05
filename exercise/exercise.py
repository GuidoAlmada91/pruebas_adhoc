lista_personas = [
    ('11111111', 'Pedro', 'Paez', 24),
    ('22222222', 'Fito', 'Garcia', 23),
    ('33333333', 'Leo', 'Peralta', 26),
    ('44444444', 'Bruno', 'Mac', 25),
    ('55555555', 'Nico', 'Zaoral', 27),
    ('44444444', 'Bruno', 'Mac', 25),
]

def obtener_edad(persona):
    return persona[3]

def ordenar(lista_personas):
    """Devuelve una lista con las edades ordenadas de menor a mayor."""
    try:
        edades_ordenadas = sorted(lista_personas, key=obtener_edad)
        
        edades = [persona[3] for persona in edades_ordenadas]
        
        return edades
    except:
        print("Error, algo salio mal.")
        return None
 
    pass


def convertir_a_diccionario(lista_personas):
        """ Hacer un diccionario que tenga como claves los “dni” y como valores tuplas con nombre, apellido y edad """
        diccionario = {}
        for persona in lista_personas:
            
            identificacion = persona[0]
        
            valores = persona[1:]
    
            diccionario[identificacion] = valores
    
        return diccionario
    

def devolver_edad(lista_personas, dni):
    """ Para la 'lista_personas' devuelve la edad de la persona que tenga el dni definido.
    Tip: intentar usar el método convertir_a_diccionario"""
    diccionario = convertir_a_diccionario(lista_personas)
    if dni in diccionario:
        edad = diccionario[dni][-1]
        return edad
    else:
        return None
    pass


def eliminar_repetidos(lista_personas):
    """ El metodo debe devolver los elementos unicos """
    return list(set(lista_personas))
    # Completar
    pass


def separar_por_edad(lista_personas):
    """ Devolver dos listas
    * lista 1: mayores de 25 (incluido)
    * lista 2: menores de 25
    """
    mayores25 = []
    menores25 = []

    for persona in lista_personas:
        edad = persona[3] 

        if edad >= 25:
            mayores25.append(persona)
        else:
            menores25.append(persona)

    return mayores25, menores25
    return [], []


def obtener_promedio(lista):
    """ Implementar obtener el promedio de la lista de números que se recibe.
    Capturar con un try/except la excepción de dividir por cero"""
    try:
        promedio = sum(lista) / len(lista)
        return promedio
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
        return None

    pass


def main():
    """ Este metodo no debe modificarse y es solo a fines de probar el codigo """
    print('Resultados:\n')
    print(' * Edades ordenadas: %s\n' % ordenar(lista_personas))
    print(' * Elementos como diccionario: %s\n' % convertir_a_diccionario(lista_personas))
    print(' * La edad para dni 55555555 es: %s\n' % devolver_edad(lista_personas, '55555555'))
    print(' * Elementos únicos: %s\n' % eliminar_repetidos(lista_personas))
    print(' * Los mayores de 25 son: %s\n' % separar_por_edad(lista_personas)[0])
    print(' * Los menores de 25 son: %s\n' % separar_por_edad(lista_personas)[1])
    print(' * El promedio de las edades es: %s\n' % obtener_promedio(ordenar(lista_personas)))
    print(' * El promedio de una lista vacía es: %s\n' % obtener_promedio([]))

main()