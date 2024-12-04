import pygame
from modulos.constantes import *
from modulos.juego import calcular_puntaje_envido

def dibujar_texto(texto: str, fuente: any, color: tuple,
                  superficie: any, x: int, y: int) -> None:
    '''Dibujar texto en pantalla'''
    texto_obj = fuente.render(texto, True, color)
    texto_rect = texto_obj.get_rect(center=(x, y))
    superficie.blit(texto_obj, texto_rect)
    
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
        carta_x = x + i * (ancho_carta + espacio)
        carta_y = y
        pygame.draw.rect(pantalla, BLANCO, (carta_x, carta_y, ancho_carta, alto_carta))
        pantalla.blit(imagen_carta, (carta_x, carta_y))

def seleccionar_carta(mouse_pos: any, cartas: list, pos_x: int, pos_y: int) -> None:
    
    for i, (valor, palo) in enumerate(cartas):
        x = pos_x + i * (ancho_carta + espacio)
        if x <= mouse_pos[0] <= x + ancho_carta and pos_y <= mouse_pos[1] <= pos_y + alto_carta:
            return i
    return None

#Funcion cantar envido
def cantar_envido(emisor, cartas_jugador, cartas_maquina, pantalla, fuente,):
    """
    Lógica para cantar envido, recibir la respuesta del jugador ('quiero' o 'no quiero') 
    y calcular los puntos en consecuencia.
    
    Parámetros:
        cartas_jugador (list): Lista de cartas del jugador.
        cartas_maquina (list): Lista de cartas de la máquina.
        pantalla (pygame.Surface): Superficie de pygame para mostrar mensajes.
        fuente (pygame.font.Font): Fuente para los textos del juego.

    Retorna:
        tuple: (ganador, puntos_envido) donde 'ganador' es "jugador" o "maquina", 
               y 'puntos_envido' son los puntos ganados en esta jugada.
    """
    # Calcular puntos de envido
    tantos_jugador = calcular_puntaje_envido(cartas_jugador)
    tantos_maquina = calcular_puntaje_envido(cartas_maquina)

    # Mostrar mensaje inicial
    if emisor != 'jugador':
        mensaje = "Envido! ¿Qué respondes? (quiero/no quiero)"
        dibujar_texto(mensaje, fuente, BLANCO, pantalla, ANCHO // 2, ALTO // 2 - 50)
        pygame.display.flip()

    respuesta = ""
    if emisor == 'jugador':
        while respuesta not in ["quiero", "no quiero"]:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:  # 'q' para "quiero"
                        respuesta = "quiero"
                    elif evento.key == pygame.K_n:  # 'n' para "no quiero"
                        respuesta = "no quiero"

    else:
        if tantos_maquina >= 27:
            respuesta = 'quiero'
        else:
            respuesta = 'no quiero'
                
    # Resolver envido según respuesta
    if emisor == 'maquina':
        if respuesta == "quiero":
            if tantos_jugador > tantos_maquina:
                ganador = "jugador"
                puntos_envido = 2
                mensaje_resultado = f"Ganaste el Envido con {tantos_jugador} puntos contra {tantos_maquina}."
            elif tantos_maquina > tantos_jugador:
                ganador = "maquina"
                puntos_envido = 2
                mensaje_resultado = f"La máquina ganó el Envido con {tantos_maquina} puntos contra {tantos_jugador}."
            else:
                ganador = "maquina"  # Gana la máquina por ser mano en caso de empate
                puntos_envido = 2
                mensaje_resultado = "Empate en puntos. Gana la máquina por ser mano."
        else:
            # "No quiero": el jugador rechaza el envido
            ganador = "maquina"
            puntos_envido = 1
            mensaje_resultado = "Rechazaste el Envido. La máquina gana 1 punto."
    else:
        if respuesta == "quiero":
            if tantos_jugador > tantos_maquina:
                ganador = "jugador"
                puntos_envido = 2
                mensaje_resultado = f"Ganaste el Envido con {tantos_jugador} puntos contra {tantos_maquina}."
            elif tantos_maquina > tantos_jugador:
                ganador = "maquina"
                puntos_envido = 2
                mensaje_resultado = f"La máquina ganó el Envido con {tantos_maquina} puntos contra {tantos_jugador}."
            else:
                ganador = "maquina"  # Gana la máquina por ser mano en caso de empate
                puntos_envido = 2
                mensaje_resultado = "Empate en puntos. Gana la máquina por ser mano."
        else:
            ganador = "jugador"
            puntos_envido = 1
            mensaje_resultado = "La maquina rechazo el Envido. El jugador gana 1 punto."
            
    # Mostrar el resultado del envido
    dibujar_texto(mensaje_resultado, fuente, BLANCO, pantalla, ANCHO // 2, ALTO // 2 + 50)
    pygame.display.flip()
    pygame.time.wait(3000)  # Pausa para mostrar el mensaje

    return ganador, puntos_envido