import pygame

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

#essa lista imagens possui esses indices cachorros: [0, 2, 5, 7, 8, 10, 13, 15]
#e esses indices donuts: [1, 3, 4, 6, 9, 11, 12, 14]

# Chamada da função
imagens_cachorros = carrega_imagens(cachorros, linhas, colunas)

# Exemplo de como utilizar as imagens carregadas
for i, imagem in enumerate(imagens_cachorros):
    pygame.image.save(imagem, f'cachorro_{i}.png')



