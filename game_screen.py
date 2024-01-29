import pygame
from config import FPS, WIDTH, HEIGHT, BLACK
from assets import carrega_arquivos
import random


def sorteia_imagem():
    eh_cachorro = random.choice([True, False])

    if eh_cachorro:
        imagem =  random.choice(carrega_arquivos()['puppy'])
    else:
        imagem = random.choice(carrega_arquivos()['bagel'])

    x = random.randint(0, WIDTH - imagem.get_width())

    y = -imagem.get_height()

    velocidade = random.randint(1, 5)

    return {'imagem': imagem,
            'eh_cachorro': eh_cachorro,
            'x': x,
            'y': y,
            'velocidade': velocidade}

imagens = []
for _ in range(5):
    imagens.append(sorteia_imagem())



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
        for imagem in imagens:
            window.blit(imagem['imagem'], (imagem['x'], imagem['y']))
            imagem['y'] += imagem['velocidade']

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor preta

        #carrega as imagens
        imagem = pygame.image.load('assets\\img\\cachorro_0.png')
        retangulo_imagem = imagem.get_rect()

        window.blit(imagem, retangulo_imagem)


        pygame.display.update()  # Mostra o novo frame para o jogador


    return state

def sorteia_imagem():
    eh_cachorro = random.choice([True, False])

    if eh_cachorro:
        imagem =  random.choice(carrega_arquivos()['puppy'])
    else:
        imagem = random.choice(carrega_arquivos()['bagel'])

    x = random.randint(0, WIDTH - imagem.get_width())

    y = -imagem.get_height()

    velocidade = random.randint(1, 5)

    return {'imagem': imagem,
            'eh_cachorro': eh_cachorro,
            'x': x,
            'y': y,
            'velocidade': velocidade}



