import pygame
import os
from config import*

def carrega_arquivos():
    dicionario_de_arquivos = {}
    dicionario_de_arquivos['btn'] = pygame.image.load(os.path.join(IMG_DIR, 'btn1.png')).convert()
    #mudando tamanho das imagens
    largura = dicionario_de_arquivos['btn'].get_rect().width * .25
    altura = dicionario_de_arquivos['btn'].get_rect().height * .25
    dicionario_de_arquivos['btn'] = pygame.transform.scale(dicionario_de_arquivos['btn'], (largura, altura))

    dicionario_de_arquivos['btn_hover'] = pygame.image.load(os.path.join(IMG_DIR, 'btn1_hover.png')).convert()
    dicionario_de_arquivos['btn_hover'] = pygame.transform.scale(dicionario_de_arquivos['btn_hover'], (largura, altura))

    dicionario_de_arquivos['puppy'] = pygame.image.load(os.path.join(IMG_DIR, 'PuppyOrBagel.jpg')).convert()
    dicionario_de_arquivos['puppy'] = pygame.transform.scale(dicionario_de_arquivos['puppy'], (largura, altura))
    dicionario_de_arquivos['bagel'] = pygame.image.load(os.path.join(IMG_DIR, 'PuppyOrBagel.jpg')).convert()
    dicionario_de_arquivos['bagel'] = pygame.transform.scale(dicionario_de_arquivos['bagel'], (largura, altura))

    #carregando Fonte
    dicionario_de_arquivos['font'] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 22)
    dicionario_de_arquivos['font_media'] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 30)

    #essa lista imagens possui esses indices cachorros: [0, 2, 5, 7, 8, 10, 13, 15]
    #e esses indices donuts: [1, 3, 4, 6, 9, 11, 12, 14]
    
    #cachorros
    dicionario_de_arquivos['puppy0'] = pygame.image.load('cachorro_0.png')
    dicionario_de_arquivos['puppy2'] = pygame.image.load('cachorro_2.png')
    dicionario_de_arquivos['puppy5'] = pygame.image.load('cachorro_5.png')
    dicionario_de_arquivos['puppy7'] = pygame.image.load('cachorro_7.png')
    dicionario_de_arquivos['puppy8'] = pygame.image.load('cachorro_8.png')
    dicionario_de_arquivos['puppy10'] = pygame.image.load('cachorro_10.png')
    dicionario_de_arquivos['puppy13'] = pygame.image.load('cachorro_13.png')
    dicionario_de_arquivos['puppy15'] = pygame.image.load('cachorro_15.png')

    #bagel
    dicionario_de_arquivos['bagel1'] = pygame.image.load('cachorro_1.png')
    dicionario_de_arquivos['bagel3'] = pygame.image.load('cachorro_3.png')
    dicionario_de_arquivos['bagel4'] = pygame.image.load('cachorro_4.png')
    dicionario_de_arquivos['bagel6'] = pygame.image.load('cachorro_6.png')
    dicionario_de_arquivos['bagel9'] = pygame.image.load('cachorro_9.png')
    dicionario_de_arquivos['bagel11'] = pygame.image.load('cachorro_11.png')
    dicionario_de_arquivos['bagel12'] = pygame.image.load('cachorro_12.png')
    dicionario_de_arquivos['bagel14'] = pygame.image.load('cachorro_14.png')


    return dicionario_de_arquivos

#outra função ----------------------------------------
#cachorro imagem
cachorros = pygame.image.load('assets\\img\\PuppyOrBagel.jpg')

colunas = 4
linhas = 4
#dados
largura_foto = cachorros.get_width() // colunas
altura_foto = cachorros.get_height() // linhas

#Função para cortar as imagens
def carrega_imagens(cachorros, linhas, colunas):
    # Percorre todos os sprites adicionando em uma lista.
    imagens = []
    for linha in range(linhas):
        for coluna in range(colunas):
            # Calcula posição do sprite atual
            x = coluna * largura_foto
            y = linha * altura_foto
            # Define o retângulo que contém o sprite atual
            dest_rect = pygame.Rect(x, y, largura_foto, altura_foto)

            # Cria uma imagem vazia do tamanho do sprite
            image = pygame.Surface((largura_foto, altura_foto), pygame.SRCALPHA)

            # Copia o sprite atual (do spritesheet) na imagem
            image.blit(cachorros, (0, 0), dest_rect)
            imagens.append(image)

    return imagens

imagens_cachorros = carrega_imagens(cachorros, linhas, colunas)

#transforma a imagem em png
for i, imagem in enumerate(imagens_cachorros):
    pygame.image.save(imagem, f'cachorro_{i}.png')

#--------------------------------------------------------------------------------