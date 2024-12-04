import pygame, random
from modulos.constantes import *
from modulos.funciones import *

def crear_mazo() -> list:
    mazo = [(valor, palo) for valor in VALORES for palo in PALOS ]
    return mazo

def mezclar(mazo: list) -> list:
    #Devuelve la secuencia pasada como argumento desordenada.
    #Cambia la lista y no devuelve una nueva
    random.shuffle(mazo)
    return mazo

def repartir(mazo: list) -> list:
    #usa slicing para tomar elementos
    cartas_jugador = mazo[0:3] #index 0,1,2
    cartas_maquina = mazo[3:6]#index 3,4,5
    return cartas_jugador, cartas_maquina

def seleccionar_carta(mouse_pos, cartas_jugador, pos_x_inicio, pos_y):
    """
    Selecciona una carta del jugador basada en la posición del mouse.
    
    Parámetros:
    - mouse_pos: tuple (x, y) posición del mouse.
    - cartas_jugador: lista de cartas [(número, palo), ...].
    - pos_x_inicio: posición X inicial de la primera carta en pantalla.
    - pos_y: posición Y de las cartas en pantalla.
    
    Retorna:
    - La carta seleccionada como tuple (número, palo) o `None` si no se selecciona ninguna.
    """
    ancho_carta = 60  # Ancho de cada carta
    alto_carta = 90   # Alto de cada carta
    espacio_entre_cartas = 20  # Espacio entre cartas

    # Iterar por las cartas del jugador
    for i, carta in enumerate(cartas_jugador):
        # Calcular las coordenadas de cada carta
        carta_x = pos_x_inicio + i * (ancho_carta + espacio_entre_cartas)
        carta_rect = pygame.Rect(carta_x, pos_y, ancho_carta, alto_carta)
        
        # Verificar si el clic está dentro del rectángulo de la carta
        if carta_rect.collidepoint(mouse_pos):
            return carta  # Retorna la carta seleccionada
    
        return None  # Si no se selecciona ninguna carta


def comparar_mano(cartas: tuple, jerarquia: dict ) -> str:
    '''Rtorna ganador mano'''
    carta_jugador, carta_maquina = cartas
    valor_jugador = jerarquia[f'{carta_jugador[0]} de {carta_jugador[1]}']
    valor_maquina = jerarquia[f'{carta_maquina[0]} de {carta_maquina[1]}']

    if valor_jugador > valor_maquina:
        return "jugador"
    elif valor_jugador < valor_maquina:
        return "maquina"
    else:
        return "empate"

def evaluar_ganador_ronda(ganador_manos: dict) -> str:
    if ganador_manos['jugador'] >= 2:
        return 'jugador'
    elif ganador_manos['maquina'] >= 2:
        return 'maquina'
    else:
        return 'empate'

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

