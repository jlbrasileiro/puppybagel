import pygame 
from assets import *
from config import BLACK
from game_screen import game_screen

DONE = 0
PLAYING = 1
state = PLAYING

tempo = pygame.time.get_ticks()

def game_over(tela):

    #PRINTAR O NOME NA TELA
    clock = pygame.time.Clock()

    agora = pygame.time.get_ticks()
    a = (int((agora - tempo)/1000))

    fonte =pygame.font.SysFont(None, 48)
    text2 = fonte.render(f'{a}', True, (255,215,0))

    fonte = pygame.font.Font(None, 40) #nome da fonte e tamanho dela

    # Renderize o TEMPO
    texto2 = fonte.render('Game Over !!!', True, (255,255,255))
    texto = fonte.render(f" Seu time foi de: {a} segundos", True, (255,255,255))

    # Posicione o texto no centro da tela
    pos_texto = texto.get_rect(center=(900// 2, 700 // 2))


    running = True
    while running:

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
                running = False

        tela.fill(BLACK)

        tela.blit(texto2,(350,100))

        tela.blit(texto, pos_texto)

        pygame.display.flip()
        

    return state