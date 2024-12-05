import pygame
from modulos.constantes import *
from modulos.juego import calcular_puntaje_envido

def dibujar_texto(texto: str, fuente: any, color: tuple, superficie: any, x: int, y: int) -> None:
    '''Dibujar texto en pantalla'''
    texto_obj = fuente.render(texto, True, color)
    texto_rect = texto_obj.get_rect(center=(x, y))
    superficie.blit(texto_obj, texto_rect)

def dibujar_carta(superficie: any, color: tuple, x: int, y: int, ancho=100, alto=150):
    carta = pygame.Rect(x, y, ancho, alto)
    pygame.draw.rect(superficie, color, carta)
    return carta

def actualizar_color_botones(botones: tuple, mouse_pos: tuple, 
                             pantalla: any, fuente: any, color_normal: tuple, 
                             color_hover: tuple, color_txt: tuple) -> None:
    '''Cambiar color si el mouse está sobre el botón'''
    for boton in botones:
        color_boton = color_hover if boton["rect"].collidepoint(mouse_pos) else color_normal
        pygame.draw.rect(pantalla, color_boton, boton["rect"])
        dibujar_texto(boton["texto"], fuente, color_txt, 
                      pantalla, boton["rect"].centerx, boton["rect"].centery)
        
def cargar_imagen(ruta: str, ancho: int, alto: int) -> any:
    '''Cargar y escalar imagen'''
    imagen = pygame.image.load(ruta)
    return pygame.transform.scale(imagen, (ancho, alto))

#mostrar cartas 
def mostrar_cartas(cartas: list, x: any, y: any, visible: bool) -> None:
    
    for i, (valor, palo) in enumerate(cartas):
        if visible == True:
            ruta_carta = f"images/{valor} de {palo}.jpg"
        else:
            ruta_carta = "images/dorso_carta.jpg"
        imagen_carta = cargar_imagen(ruta_carta, ancho_carta, alto_carta)
        carta_x = x + (i * (ancho_carta + espacio))
        carta_y = y
        pygame.draw.rect(pantalla, BLANCO, (carta_x, carta_y, ancho_carta, alto_carta))
        pantalla.blit(imagen_carta, (carta_x, carta_y))

def seleccionar_carta(mouse_pos: any, cartas: list, pos_x: int, pos_y: int) -> None:
    
    for i, (valor, palo) in enumerate(cartas):
        x = pos_x + i * (ancho_carta + espacio)
        if x <= mouse_pos[0] <= x + ancho_carta and pos_y <= mouse_pos[1] <= pos_y + alto_carta:
            return i
    return None
