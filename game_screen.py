import pygame
from config import FPS, WIDTH, HEIGHT, BLACK
from assets import carrega_arquivos

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    dicionario_de_arquivos = carrega_arquivos()

    DONE = 0
    PLAYING = 1
    state = PLAYING



    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor preta

        #carrega as imagens
        imagem = pygame.image.load('assets\\img\\cachorro_0.png')
        retangulo_imagem = imagem.get_rect()

        window.blit(imagem, retangulo_imagem)


        pygame.display.update()  # Mostra o novo frame para o jogador


    return state
