import pygame
from modulos.constantes import *
from modulos.funciones import dibujar_texto

def jugar_envido(cartas_emisor: list, cartas_receptor: list, puntos_emisor: int, puntos_receptor: int, respuesta: bool) -> int:
    
    def calcular_puntaje_envido(cartas: list) -> int:
        #dict de equivalencias para envido
        valores = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 10: 0, 11: 0, 12: 0}
        palos = {}
        for valor, palo in cartas:
            if palo not in palos:
                palos[palo] = []
            palos[palo].append(valores[valor])
        max_puntaje = 0
        for palo, cartas_palo in palos.items():
            if len(cartas_palo) > 1:
                cartas_palo.sort(reverse=True)
                max_puntaje = max(max_puntaje, 20 + cartas_palo[0] + cartas_palo[1])
            else:
                max_puntaje = max(max_puntaje, cartas_palo[0])
        return max_puntaje
    
    tantos_emisor = calcular_puntaje_envido(cartas_emisor)
    tantos_receptor = calcular_puntaje_envido(cartas_receptor)

    if respuesta == True:
        if tantos_emisor > tantos_receptor:
            puntos_emisor += 2
            mensaje_resultado = f"Emisor gano Envido con {tantos_emisor} puntos contra {tantos_receptor}."
        else:
            puntos_receptor += 2
            mensaje_resultado = f"Receptor gano Envido con {tantos_receptor} puntos contra {tantos_emisor}."
    else:
        puntos_emisor += 1
        mensaje_resultado = f"Emisor gano Envido con {tantos_emisor} por ser mano."
    
    # Mostrar el resultado del envido
    dibujar_texto(mensaje_resultado, FUENTE_M, BLANCO, pantalla, ANCHO // 2, ALTO // 2)
    pygame.display.flip()
    pygame.time.wait(3000)
    
    return puntos_emisor, puntos_receptor