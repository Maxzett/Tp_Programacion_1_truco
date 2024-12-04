import pygame
from modulos.constantes import *
from modulos.configuracion import *
from modulos.funciones import *
from modulos.juego import *

botones_juego = [
    {"texto": "Envido", "rect": pygame.Rect(50, ALTO - 200 + 50, 200, 50)},
    {"texto": "Truco", "rect": pygame.Rect(ANCHO - 250, ALTO - 200 + 50, 200, 50)},
    {"texto": "Mazo", "rect": pygame.Rect(ANCHO - 250, ALTO - 300 + 50, 200, 50)}
]


def iniciar_partida():
    pygame.display.set_caption("Juego de Truco")
    
    #registro de nombre jugador
    nombre_jugador = entrada_nombre()
    
    #seleccion de puntos
    puntos_objetivo = elegir_puntos()

    pantalla.fill(AZUL)
    # resumen nombre y puntos selccionados
    dibujar_texto(f"¡Hola, {nombre_jugador}! Inicias siendo Mano", FUENTE_L, NEGRO, pantalla, ANCHO // 2, ALTO // 2 - 50)
    dibujar_texto(f"Jugaremos a {puntos_objetivo} puntos.", FUENTE_L, NEGRO, pantalla, ANCHO // 2, ALTO // 2 + 50)
    pygame.display.flip()
    pygame.time.wait(2000)
    
    mazo = crear_mazo()  # Crear mazo
    mazo_mezclado = mezclar(mazo) # Mezclar
    
    # Puntos iniciales
    puntos_jugador = 0
    puntos_maquina = 0
        
    # Inicializar variables del juego
    juego_activo = True
    mano_actual = 'jugador'
    
    while juego_activo:
        pantalla.fill(VIOLETA)
        
        dibujar_texto(f'P. Jugador: {puntos_jugador} - P.Maquina: {puntos_maquina}', FUENTE_S, NEGRO, pantalla, 200, 100)
        pygame.display.flip()
        
        mouse_pos = pygame.mouse.get_pos()

        cartas_jugador, cartas_maquina = repartir(mazo_mezclado)

        # Centrado de las cartas
        maquina_pos_x = (ANCHO - (len(cartas_maquina) * (ancho_carta + espacio) - espacio)) // 2
        jugador_pos_x = (ANCHO - (len(cartas_jugador) * (ancho_carta + espacio) - espacio)) // 2

        mostrar_cartas(cartas_maquina, maquina_pos_x, 50, visible=False)
        mostrar_cartas(cartas_jugador, jugador_pos_x, ALTO - alto_carta - 50, visible=True)

        actualizar_color_botones(botones_juego, mouse_pos, pantalla, FUENTE_M, ROSA, VERDE, NEGRO)

        rondas_jugador = 0
        rondas_maquina = 0
        
        
    
            
        # Alternar la mano para la próxima ronda
        mano_actual = "maquina" if mano_actual == "jugador" else "jugador"
        
        # Actualizar visualización de rondas ganadas
        dibujar_texto(f'R. Jugador: {rondas_jugador} - R.Maquina: {rondas_jugador}', FUENTE_S, NEGRO, pantalla, 200, 200)
        pygame.display.flip()
        pygame.time.wait(1000)
        
        # Verificar si alguien alcanzó los puntos objetivo
        if puntos_jugador >= puntos_objetivo or puntos_maquina >= puntos_objetivo:
            juego_activo = False
                    
        # Manejar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                juego_activo = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                
                for boton in botones_juego:
                    if boton["rect"].collidepoint(evento.pos):
                        if boton["texto"] == "Envido":
                            print(calcular_puntaje_envido(cartas_jugador))
                            print(calcular_puntaje_envido(cartas_maquina))
                            # cantar_envido('jugador',cartas_jugador, cartas_maquina, pantalla, FUENTE_S)
                        elif boton["texto"] == "Truco":
                            print("Truco")
                        elif boton["texto"] == "Mazo":
                                print('mazo')
    # actualizar pantalla   
    pygame.display.flip()