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
rect = pygame.Rect((300, 200), (100, 100))

# Variavel para controlar o loop principal
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

    # Códigos de "desenho"
    pygame.draw.rect(screen, RED, rect)

    # Atualiza a tela com as informações que foram adicionadas até então
    pygame.display.update()

    # 60 frames por segundo
    clock.tick(60)

# Close the window and quit.
pygame.quit()
