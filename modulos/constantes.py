import pygame

# Dimensiones de la pantalla
ANCHO, ALTO = 1280, 720
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# Colores
BLANCO = (254, 250, 224)
NEGRO = (0, 0, 0)
GRIS = (180, 180, 180)
GRIS_CLARO = (220, 220, 220)

AZUL = (53, 80, 112)
VIOLETA = (109, 89, 122)
VERDE = (96, 108, 56)
ROJO = (255, 0, 0)
ROSA = (239, 71, 111) 

# Fuente
pygame.font.init()
FUENTE_TITULO = pygame.font.Font(None, 80)
FUENTE_S = pygame.font.Font(None, 30)
FUENTE_M = pygame.font.Font(None, 45)
FUENTE_L = pygame.font.Font(None, 60)

# Cartas medidas
ancho_carta = 100
alto_carta = 150
espacio = 20

PALOS = ("Espada", "Basto", "Oro", "Copa")
VALORES = (1, 2, 3, 4, 5, 6, 7, 10, 11, 12)
JERARQUIA = {
    (1, "Espada"): 14, (1, "Basto"): 13, 
    (7, "Espada"): 12, (7, "Oro"): 11,   
    (3, "Espada"): 10, (3, "Basto"): 10, (3, "Oro"): 10, (3, "Copa"): 10,  
    (2, "Espada"): 9, (2, "Basto"): 9, (2, "Oro"): 9, (2, "Copa"): 9,      
    (1, "Oro"): 8, (1, "Copa"): 8,
    (12, "Espada"): 7, (12, "Basto"): 7, (12, "Oro"): 7, (12, "Copa"): 7,
    (11, "Espada"): 6, (11, "Basto"): 6, (11, "Oro"): 6, (11, "Copa"): 6,
    (10, "Espada"): 5, (10, "Basto"): 5, (10, "Oro"): 5, (10, "Copa"): 5,
    (7, "Basto"): 4, (7, "Copa"): 4,
    (6, "Espada"): 3, (6, "Basto"): 3, (6, "Oro"): 3, (6, "Copa"): 3,
    (5, "Espada"): 2, (5, "Basto"): 2, (5, "Oro"): 2, (5, "Copa"): 2,
    (4, "Espada"): 1, (4, "Basto"): 1, (4, "Oro"): 1, (4, "Copa"): 1,
}