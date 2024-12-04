import pygame, csv
from modulos.constantes import *
from modulos.funciones import *

def mostrar_ranking():
    """Muestra la pantalla de ranking con datos leídos de un archivo CSV."""
    pygame.display.set_caption("Ranking Jugadores")
    
    corriendo = True
    ruta_csv = "ranking.csv"  # Archivo CSV con los datos del ranking
    boton_volver = pygame.Rect(ANCHO // 2 - 150, ALTO - 100, 300, 50)

    while corriendo:
        pantalla.fill(AZUL)
        mouse_pos = pygame.mouse.get_pos()

        # Título del ranking
        dibujar_texto("Ranking de Jugadores", FUENTE_TITULO, NEGRO, pantalla, ANCHO // 2, 50)

        # Leer datos del archivo CSV
        try:
            with open(ruta_csv, "r") as archivo_csv:
                lector_csv = csv.reader(archivo_csv)
                datos = list(lector_csv)
        except FileNotFoundError:
            datos = [["Sin datos disponibles"]]

        # Mostrar los datos en pantalla
        y_offset = 150
        for fila in datos:
            texto = " | ".join(fila)
            dibujar_texto(texto, FUENTE_S, NEGRO, pantalla, ANCHO // 2, y_offset)
            y_offset += 40

        # Dibujar el botón para volver al menú
        color_boton = VERDE if boton_volver.collidepoint(mouse_pos) else ROSA
        pygame.draw.rect(pantalla, color_boton, boton_volver)
        dibujar_texto('Volver', FUENTE_M, NEGRO, pantalla, boton_volver.centerx, boton_volver.centery)
        
        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # Click izquierdo
                    if boton_volver.collidepoint(evento.pos):
                        corriendo = False

        # Actualizar pantalla
        pygame.display.flip()