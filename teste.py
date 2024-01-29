import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura_tela = 900
altura_tela = 700
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Puppy or Bagel")

# Carregar imagem
imagem = pygame.image.load('assets\\img\\cachorro_1.png')  

# Obter retângulo da imagem
retangulo_imagem = imagem.get_rect()

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Limpar a tela
    tela.fill((0, 0,0))  # Preencher a tela com branco

    # Desenhar a imagem na tela usando blit
    tela.blit(imagem, retangulo_imagem)

    # Atualizar a tela
    pygame.display.flip()



