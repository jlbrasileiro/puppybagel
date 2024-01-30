import pygame 
from assets import *
from config import BLACK
#from game_screen import DONE, PLAYING

DONE = 0
PLAYING = 1
state = PLAYING

def game_over(tela):
    clock = pygame.time.Clock()

    #trecho extraido de chat.openai.com
    fonte = pygame.font.Font(None, 60)  # Você também pode fornecer o nome de uma fonte e o tamanho

    # Renderize o texto desejado
    texto = fonte.render("Game Over !!! :(", True, (255,255,255))

    # Posicione o texto no centro da tela
    pos_texto = texto.get_rect(center=(900// 2, 700 // 2))

    running = True
    while running:

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
                running = False

            if event.type == pygame.KEYUP:
                state = PLAYING
                running = False

        tela.fill(BLACK)

        tela.blit(texto, pos_texto)

        pygame.display.flip()

    return state