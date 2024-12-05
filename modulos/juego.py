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

def comparar_mano(carta_jugador: tuple, carta_maquina: tuple, jerarquia: dict) -> dict:
    '''Retorna ganador mano'''
    
    valor_jugador = jerarquia[carta_jugador]
    valor_maquina = jerarquia[carta_maquina]

    if valor_jugador > valor_maquina:
        return {'jugador': 1, 'maquina': 0, 'empate': 0}
    elif valor_jugador < valor_maquina:
        return {'jugador': 0, 'maquina': 1, 'empate': 0}
    else:
        return {'jugador': 0, 'maquina': 0, 'empate': 1}

def evaluar_ganador_ronda(ganador_manos: dict) -> str:
    if ganador_manos['jugador'] >= 2:
        return 'jugador'
    elif ganador_manos['maquina'] >= 2:
        return 'maquina'
    else:
        return 'empate'

