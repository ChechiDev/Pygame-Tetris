# main.py

# Importamos las librerías necesarias:
# pygame: para crear el juego y manejar gráficos, eventos, etc.
# sys: para poder cerrar el programa completamente
import pygame, sys

# Inicializamos todos los módulos de Pygame
pygame.init()

# Game colors:
screen_color = (44, 44, 127) # Black, dark-blue = (44, 44, 127)

# Configuramos el tamaño de la ventana del juego
screen = pygame.display.set_mode((400, 800))

# Establecemos el título de la ventana (aparece en la barra superior)
pygame.display.set_caption("Python Tetris")

# Creamos un reloj para controlar la velocidad del juego (FPS)
clock = pygame.time.Clock()

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

    # Drawing screen fill
    screen.fill(screen_color)

    # Actualizamos la pantalla para mostrar cualquier cambio realizado en la ventana
    pygame.display.update()

    # Limitamos el Loop a 60 iteraciones por segundo (60 FPS)
    clock.tick(60)
