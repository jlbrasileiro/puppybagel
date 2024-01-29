import pygame
import os
from config import IMG_DIR, FNT_DIR

#Função para cortar as imagens
def carrega_imagens(puppy, linhas, colunas):
    # Percorre todos os sprites adicionando em uma lista.
    imagens = []
    largura_foto = puppy.get_width() // colunas
    altura_foto = puppy.get_height() // linhas

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
            image.blit(puppy, (0, 0), dest_rect)
            imagens.append(image)

    return imagens

def carrega_arquivos():
    dicionario_de_arquivos = {}
    dicionario_de_arquivos['btn'] = pygame.image.load(os.path.join(IMG_DIR, 'btn1.png')).convert()
    #mudando tamanho das imagens
    largura = dicionario_de_arquivos['btn'].get_rect().width * .25
    altura = dicionario_de_arquivos['btn'].get_rect().height * .25
    dicionario_de_arquivos['btn'] = pygame.transform.scale(dicionario_de_arquivos['btn'], (largura, altura))

    dicionario_de_arquivos['btn_hover'] = pygame.image.load(os.path.join(IMG_DIR, 'btn1_hover.png')).convert()
    dicionario_de_arquivos['btn_hover'] = pygame.transform.scale(dicionario_de_arquivos['btn_hover'], (largura, altura))

   

    #carregando Fonte
    dicionario_de_arquivos['font'] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 22)
    dicionario_de_arquivos['font_media'] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 30)
    #carregando a imagem completa

    puppy = pygame.image.load(os.path.join(IMG_DIR, 'PuppyOrBagel.jpg'))

    #obtendo todas as imagens da funçao carrega_imagens

    total = carrega_imagens(puppy, linhas=4, colunas=4)

    # separando as imagens dos cachorros e da rosquinha 

    for i in [0,2,5,7,8,10,13,15]:
        puppy_imagens = total[i]
    for i in [1,3,4,6,9,11,12,14]:
        bagel_imagens = total[i]


    dicionario_de_arquivos['puppy'] = puppy_imagens
    dicionario_de_arquivos['bagel'] = bagel_imagens






   

    return dicionario_de_arquivos



#--------------------------------------------------------------------------------