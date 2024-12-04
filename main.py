import pygame
from modulos.constantes import *
from modulos.ranking import mostrar_ranking
from modulos.funciones import dibujar_texto, actualizar_color_botones
from modulos.partida import iniciar_partida
pygame.init()

botones_menu = (
        {"texto": "Iniciar nuevo juego", "rect": pygame.Rect( ANCHO // 2 - 150, 300, 300, 50)},
        {"texto": "Ver ranking", "rect": pygame.Rect( ANCHO // 2 - 150, 400, 300, 50)},
        {"texto": "Salir", "rect": pygame.Rect( ANCHO // 2 - 150, 500, 300, 50)}
)

ejecutar = True
while ejecutar:
    pantalla.fill(AZUL)
    mouse_pos = pygame.mouse.get_pos()

    # Título del menú
    dibujar_texto("Menú Principal", FUENTE_TITULO, BLANCO, pantalla, ANCHO // 2, 100)
    dibujar_texto("Seleccione una opcion:", FUENTE_M, BLANCO, pantalla, ANCHO // 2, 200)
    # Hover botones
    actualizar_color_botones(botones_menu, mouse_pos, pantalla, FUENTE_M, ROSA, VERDE, NEGRO)
    
    # Manejo de eventos
    for evento in pygame.event.get():
        #salir con la X de la esquina
        if evento.type == pygame.QUIT:
            ejecutar = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Click izquierdo
                
                for boton in botones_menu:
                    if boton["rect"].collidepoint(evento.pos):
                        if boton["texto"] == "Iniciar nuevo juego":
                            print("Iniciando nuevo juego...")
                            # Aquí puedes llamar a la función para iniciar el juego
                            iniciar_partida()
                        elif boton["texto"] == "Ver ranking":
                            print("Mostrando ranking...")
                            # Aquí puedes llamar a la función para mostrar el ranking
                            mostrar_ranking()
                        elif boton["texto"] == "Salir":
                            ejecutar = False

    pygame.display.flip() #actualizo pantalla
pygame.quit() #apagar pygame