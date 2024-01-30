import pygame
from config import FPS, WIDTH, HEIGHT, BLACK
from assets import carrega_arquivos
import random

#Sorteia imagem -------------------------
def sorteia_imagem(dicionario_de_arquivos):
    eh_cachorro = random.choice([True, False])

    if eh_cachorro:
        imagem =  random.choice(dicionario_de_arquivos['puppy'])
    else:
        imagem = random.choice(dicionario_de_arquivos['bagel'])

    x = random.randint(0, WIDTH - imagem.get_width())

    y = -imagem.get_height()

    velocidade = random.randint(1, 5)

    return {'imagem': imagem,
            'eh_cachorro': eh_cachorro,
            'x': x,
            'y': y,
            'velocidade': velocidade}

#Colisão ---------------------------
def colisao_ponto_retangulo(posicao_x_ponto, posicao_y_ponto, posicao_x_retangulo, posicao_y_retangulo, largura_retangulo, altura_retangulo):
    
    if (posicao_x_ponto >= posicao_x_retangulo and posicao_x_ponto <= posicao_x_retangulo + largura_retangulo and
        posicao_y_ponto >= posicao_y_retangulo and posicao_y_ponto <= posicao_y_retangulo + altura_retangulo):
        return True
    else:
        return False

#Tela de jogo --------------------------
def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    dicionario_de_arquivos = carrega_arquivos()
    puppy_imagens = dicionario_de_arquivos['puppy']
    bagel_imagens = dicionario_de_arquivos['bagel']



    DONE = 0
    PLAYING = 1
    state = PLAYING

    vidas = 0
    imagens_sorteadas = []
    for _ in range(5):
        imagens_sorteadas.append(sorteia_imagem(dicionario_de_arquivos))
    

    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for imagem in imagens_sorteadas[:]:
                    if colisao_ponto_retangulo(mouse_x, mouse_y, imagem['x'], imagem['y'],imagem['imagem'].get_width(), imagem['imagem'].get_height()):
                        imagens_sorteadas.remove(imagem)
                        nova_imagem = sorteia_imagem(dicionario_de_arquivos)
                        imagens_sorteadas.append(nova_imagem)

                        if not imagem['eh_cachorro']:
                            vidas -= 1 
                        for _ in range(2):
                            imagem_nova = sorteia_imagem(dicionario_de_arquivos)
                            imagens_sorteadas.append(imagem_nova)
                        break


        #removendo imagens 
        for imagem in imagens_sorteadas[:]:
            if imagem['y'] > HEIGHT:
                imagens_sorteadas.remove(imagem)
                nova_imagem = sorteia_imagem(dicionario_de_arquivos)
                imagens_sorteadas.append(nova_imagem)
            
           

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor preta

        #desenhando imagens sorteadas
        for imagem in imagens_sorteadas:
            imagem['y'] += imagem['velocidade']
            window.blit(imagem['imagem'],(imagem['x'],imagem['y']))
            

       


        pygame.display.update()  # Mostra o novo frame para o jogador


    return state




