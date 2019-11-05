import pygame

# Cria algumas cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Inicializa os módulos pygame
pygame.init()

# Estabelece o tamanho da tela (largura, altura)
size = (700, 500)
screen = pygame.display.set_mode(size)

# Adiciona titulo à janela criada
pygame.display.set_caption("My First Game")

# Cria um retângulo

# Variavel para controlar o loop principal
# quando for 'true', sai do loop, executando os
# códigos de encerramento
done = False

# Utilizado para controlar a taxa de atualização da tela
clock = pygame.time.Clock()

######## Loop principal ########
while not done:
    ### Loop de eventos ###
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # "Limpa" a tela
    screen.fill(WHITE)

    # Lógica do jogo deve vir aqui:
    # ---

    # ---

    # Códigos de "desenho" devem vir aqui:
    # ---

    # ---

    # Atualiza a tela com as informações que foram adicionadas até então
    pygame.display.update()

    # 60 frames por segundo
    clock.tick(60)

# Close the window and quit.
pygame.quit()
