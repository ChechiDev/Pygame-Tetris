# main.py

# Importamos las librerías necesarias:
# pygame: para crear el juego y manejar gráficos, eventos, etc.
# sys: para poder cerrar el programa completamente
import pygame, sys
from cfg.config import *
from core.game import Game

# Inicializamos todos los módulos de Pygame
pygame.init()

# Establecemos el título de la ventana (aparece en la barra superior)
pygame.display.set_caption("Python Tetris")
# Configuramos el tamaño de la ventana del juego
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Creamos un reloj para controlar la velocidad del juego (FPS)
clock = pygame.time.Clock()
game = Game()

# Event personalizado para el movimiento automático hacia abajo
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200) # Trigger(event, time in milisencond)

# Loop principal del juego:
# Se ejecuta constantemente hasta que el usuario cierre la ventana
while True:
    # Procesamos todos los eventos que ocurren (teclado, ratón, cerrar ventana, etc.)
    for event in pygame.event.get():
        # Si el evento es de tipo 'QUIT' (cuando el usuario cierra la ventana)
        if event.type == pygame.QUIT:
            # Cerramos Pygame correctamente
            pygame.quit()
            # Salimos completamente del programa
            sys.exit()

        # Configuramos el movimiento (arrow keys)
        if event.type == pygame.KEYDOWN:
            # Checkeamos si game over si es true => False y reset:
            if game._game_over == True:
                game._game_over = False
                game.reset()

            if event.key == pygame.K_LEFT  and game._game_over == False:
                game.move_left()

            if event.key == pygame.K_RIGHT and game._game_over == False:
                game.move_right()

            if event.key == pygame.K_DOWN and game._game_over == False:
                game.move_down()

            if (event.key == pygame.K_UP or event.key == pygame.K_SPACE)  and game._game_over == False:
                game.rotate()

        if event.type == GAME_UPDATE and game._game_over == False: # Check amos si event es GAME_UPDATE o Game over:
            game.move_down()


    # Drawing screen fill
    screen.fill(BACKGROUND_COLOR)
    game.draw(screen)

    # Actualizamos la pantalla para mostrar cualquier cambio realizado en la ventana
    pygame.display.update()

    # Limitamos el Loop a 60 iteraciones por segundo (60 FPS)
    clock.tick(60)
