# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from config import WIDTH, HEIGHT, INIT, GAME, QUIT
from init_screen import init_screen
from game_screen import game_screen
from inicio import tela_inicial
from game_over import game_over

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Puppy or Bagel')

state = INIT
while state != QUIT:
    if state == INIT:
        #state = tela_inicial(window)
        state = init_screen(window)
        if state != QUIT:
            state = tela_inicial(window)
        
    elif state == GAME:
        state = game_screen(window)
        state = game_over(window)
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

