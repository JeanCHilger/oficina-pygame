import pygame

# Cria algumas cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Inicializa os módulos pygame
pygame.init()

# Permite repetição de eventos quando segurar uma tecla
pygame.key.set_repeat(1)

# Estabelece o tamanho da tela (largura, altura)
screen_size = (700, 500)
screen = pygame.display.set_mode(screen_size)

# Adiciona titulo à janela criada
pygame.display.set_caption("Simple Pong")

# Cria o player
player_x = 310
player_y = 490     # (posição X, posição Y), (largura, altura)
player = pygame.Rect((player_x, player_y), (80, 5))

# Cria a "bola"
ball_move_x = 3
ball_move_y = 3
ball = pygame.Rect((347, 247), (6, 6))

# Variável para controlar a pontuação
score = 0

# Função para desenhar o retangulos
def draw_rect(screen, rect, color=WHITE):
    pygame.draw.rect(screen,  color, rect)

# Função para renderizar textos
def render_text(screen, text_str):
    font = pygame.font.SysFont("Consolas", 20)
    text = font.render("Pontuação: " + str(text_str), True, WHITE)
    screen.blit(text, (5, 5))

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

        # Eventos do teclado
        elif event.type == pygame.KEYDOWN:
            # Seta para a esquerda
            if event.key == pygame.K_LEFT:
                player.x -= 5
            # Seta para a direita
            if event.key == pygame.K_RIGHT:
                player.x += 5

    # "Limpa" a tela
    screen.fill(BLACK)

    # Controla a posição da bola
    # se a bola tocar em alguma parede, a movimentação é invertida
    if ball.x <= 0:
        ball_move_x = ball_move_x * -1

    if ball.x >= screen_size[0]:
        ball_move_x = ball_move_x * -1

    if ball.y <= 0:
        ball_move_y = ball_move_y * -1

    # Se a bola cruzar a parede inferior, a pontuação é zerada
    # e a velocidade e posição da bola é restaurada
    if ball.y >= screen_size[1]:
        ball_move_y = 3
        ball_move_x = 3
        ball = pygame.Rect((347, 247), (6, 6))
        score = 0

    # Verifica se a bola tocou o player
    # cada vez que a bola tocar o player
    # um ponto é feito e a velocidade da bola é
    # levemente aumentada
    if player.colliderect(ball):
        ball_move_y = ball_move_y * -1
        score = score + 1
        ball_move_y = ball_move_y + 0.3 * (ball_move_y / abs(ball_move_y))
        ball_move_x = ball_move_x + 0.3 * (ball_move_x / abs(ball_move_x))

    # Atualiza a posição da bola
    ball.move_ip(ball_move_x, ball_move_y)

    # Desenha o player com a nova posição
    draw_rect(screen, player)
    # Desenha a bola com a nova posição
    draw_rect(screen, ball, RED)

    # Desenha na tela o texto com a pontuação
    render_text(screen, score)

    # Atualiza a tela com as informações que foram
    # adicionadas até então
    pygame.display.update()

    # 60 frames por segundo
    clock.tick(60)

# Close the window and quit.
pygame.quit()
