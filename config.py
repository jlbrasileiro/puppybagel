from os import path
from assets import *
import pygame

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

# Dados gerais do jogo.
WIDTH = 900 # Largura da tela
HEIGHT = 700 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2


# DADOS DAS IMAGENS DOS CACHORROS
cachorros = pygame.image.load('assets\\img\\PuppyOrBagel.jpg')
colunas = 4
linhas = 4
#dados
largura_foto = cachorros.get_width() // colunas
altura_foto = cachorros.get_height() // linhas

