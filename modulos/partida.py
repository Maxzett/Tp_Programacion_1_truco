import pygame
from modulos.constantes import *
from modulos.configuracion import *
from modulos.funciones import *
from modulos.juego import *
from modulos.envido import *

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
    cartas_jugador, cartas_maquina = repartir(mazo_mezclado)
    
    print(cartas_maquina)
    print(cartas_jugador)
    num_cartas = 3
    
    # Calcular la posición inicial para centrar las cartas en la pantalla
    pos_x_inicial_maquina = (ANCHO - (num_cartas * (ancho_carta + espacio) - espacio)) // 2
    pos_x_inicial_jugador = pos_x_inicial_maquina  # Igual ya que ambas están centradas horizontalmente
    # Alturas fijas para la máquina y el jugador
    pos_y_maquina = 50  # Por ejemplo, la fila superior
    pos_y_jugador = ALTO - alto_carta - 50  # Cerca de la parte inferior
    
    # Puntos iniciales
    puntos_jugador = 0
    puntos_maquina = 0
    
    envido_activo = False
    truco_activo = False    
    
    # Inicializar variables del juego
    juego_activo = True
    mano_actual = 'jugador'
    
    # Acumular resultados
    cartas_mesa = []
    
    while juego_activo:
        
        pantalla.fill(VIOLETA)
        dibujar_texto(f'PUNTOS TOTALES:', FUENTE_S, NEGRO, pantalla, 200, 70)
        dibujar_texto(f'Jugador: {puntos_jugador} - Maquina: {puntos_maquina}', FUENTE_S, NEGRO, pantalla, 200, 100)
        mouse_pos = pygame.mouse.get_pos()

        # dibujar_carta(pantalla, BLANCO, ANCHO // 2, ALTO // 2)
        
        mostrar_cartas(cartas_maquina, pos_x_inicial_maquina, pos_y_maquina, visible=False)
        mostrar_cartas(cartas_jugador, pos_x_inicial_jugador, pos_y_jugador, visible=True)

        actualizar_color_botones(botones_juego, mouse_pos, pantalla, FUENTE_M, ROSA, VERDE, NEGRO)
        
        pygame.display.flip()
        
        # Verificacion Truco activo y suma de puntos
        if truco_activo and evaluar_ganador_ronda == 'jugador':
            puntos_jugador += 2
        elif truco_activo and evaluar_ganador_ronda == 'maquina':
            puntos_maquina += 2
        
        # Verificar si alguien alcanzó los puntos objetivo
        if puntos_jugador >= puntos_objetivo or puntos_maquina >= puntos_objetivo:
            juego_activo = False
            
        # Manejar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                juego_activo = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                carta_seleccionada_jugador = seleccionar_carta(mouse_pos, cartas_jugador, pos_x_inicial_jugador, pos_y_jugador)
                print(carta_seleccionada_jugador)
                carta_seleccionada_maquina = seleccionar_carta_aleatoria(cartas_maquina)
                print(carta_seleccionada_maquina)
                
                # ganador_manos = comparar_mano(carta_seleccionada_jugador, carta_seleccionada_maquina,JERARQUIA)
                # print(ganador_manos)
                
                # # Evaluar el ganador de la ronda
                # resultado_ronda = evaluar_ganador_ronda(ganador_manos)
                # print("Ganador de la ronda:", resultado_ronda)
                        
                for boton in botones_juego:
                    if boton["rect"].collidepoint(evento.pos):
                        if boton["texto"] == "Envido":
                            if envido_activo == False:
                                puntos_jugador, puntos_maquina = jugar_envido(cartas_jugador, cartas_maquina, puntos_jugador, puntos_maquina, respuesta=True)
                                envido_activo = True
                        elif boton["texto"] == "Truco":
                            print("Truco")
                            truco_activo = True
                            dibujar_texto('Se canto truco !!!', FUENTE_M, BLANCO, pantalla, ANCHO // 2, ALTO // 2)
                            pygame.display.flip()
                            pygame.time.wait(3000)
                        elif boton["texto"] == "Mazo":
                                print('mazo')
                                puntos_maquina += 1
            
    # actualizar pantalla   
    pygame.display.flip()