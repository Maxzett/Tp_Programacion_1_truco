import pygame
from modulos.constantes import *
from modulos.funciones import *

botones_puntos = [
        {"texto": "15 Puntos", "rect": pygame.Rect( ANCHO // 2 - 150, 300, 300, 50)},
        {"texto": "30 Puntos", "rect": pygame.Rect( ANCHO // 2 - 150, 400, 300, 50)},
]
botones_confirmar = [
    {"texto": "Confirmar", "rect": pygame.Rect(ANCHO // 2 - 100, 400, 200, 50)}
]

def entrada_nombre() -> str:
    """Pantalla para registrar el nombre del jugador."""
    input_activo = True
    texto_entrada = ""
    max_caracteres = 15  # Limitar la longitud del nombre

    while input_activo:
        pantalla.fill(VIOLETA)
        mouse_pos = pygame.mouse.get_pos()        
        dibujar_texto("Ingrese su nombre:", FUENTE_L, NEGRO, pantalla, ANCHO // 2, 200)

        # Mostrar cuadro de texto
        cuadro_rect = pygame.Rect(ANCHO // 2 - 200, 300, 400, 60)
        pygame.draw.rect(pantalla, GRIS, cuadro_rect)
        dibujar_texto(texto_entrada, FUENTE_M, NEGRO, pantalla, cuadro_rect.centerx, cuadro_rect.centery)

        # Botón "Confirmar"
        boton_confirmar = pygame.Rect(ANCHO // 2 - 100, 400, 200, 50)
        pygame.draw.rect(pantalla, GRIS, boton_confirmar)
        dibujar_texto("Confirmar", FUENTE_M, NEGRO, pantalla, boton_confirmar.centerx, boton_confirmar.centery)

        actualizar_color_botones(botones_confirmar, mouse_pos, pantalla, FUENTE_M, ROSA, VERDE, NEGRO)
        
        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:  # Borrar último carácter
                    texto_entrada = texto_entrada[:-1]
                elif evento.key == pygame.K_RETURN:  # Confirmar con Enter
                    if texto_entrada.strip():  # No permitir confirmar si está vacío
                            input_activo = False
                else:
                    if len(texto_entrada) < max_caracteres:
                        texto_entrada += evento.unicode

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # Click izquierdo
                    if boton_confirmar.collidepoint(evento.pos):  # Confirmar con el botón
                        if texto_entrada.strip():  # No permitir confirmar si está vacío
                            input_activo = False

        # Actualizar pantalla
        pygame.display.flip()

    return texto_entrada

def elegir_puntos() -> int:
    """Pantalla para seleccionar los puntos del juego."""
    
    seleccion = None
    while seleccion is None:
        pantalla.fill(VIOLETA)
        mouse_pos = pygame.mouse.get_pos()
        # Título
        dibujar_texto("¿A cuántos puntos quieres jugar?", FUENTE_L, NEGRO, pantalla, ANCHO // 2, 200)

        # Botón 15 puntos
        boton_15 = pygame.Rect(ANCHO // 2 - 100, 300, 200, 50)                
        pygame.draw.rect(pantalla, GRIS, boton_15)
        dibujar_texto("15 Puntos", FUENTE_M, NEGRO, pantalla, boton_15.centerx, boton_15.centery)

        # Botón 30 puntos
        boton_30 = pygame.Rect(ANCHO // 2 - 100, 400, 200, 50)
        pygame.draw.rect(pantalla, GRIS, boton_30)
        dibujar_texto("30 Puntos", FUENTE_M, NEGRO, pantalla, boton_30.centerx, boton_30.centery)

        actualizar_color_botones(botones_puntos, mouse_pos, pantalla, FUENTE_M, ROSA, VERDE, NEGRO)
        
        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # Click izquierdo
                    if boton_15.collidepoint(evento.pos):
                        seleccion = 15
                    elif boton_30.collidepoint(evento.pos):
                        seleccion = 30

        # Actualizar pantalla
        pygame.display.flip()

    return seleccion
