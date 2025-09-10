import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Definir dimensões da tela
LARGURA = 800
ALTURA = 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("PONG com IA")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Raquetes
raquete_largura = 10
raquete_altura = 100
vel_raquete = 7

# Bola
bola_tam = 20
bola_x = LARGURA // 2
bola_y = ALTURA // 2
vel_bola_x = 5
vel_bola_y = 5

# Posições iniciais
raquete1_y = ALTURA // 2 - raquete_altura // 2
raquete2_y = ALTURA // 2 - raquete_altura // 2

# Loop principal
relogio = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Controles do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and raquete1_y > 0:
        raquete1_y -= vel_raquete
    if teclas[pygame.K_s] and raquete1_y < ALTURA - raquete_altura:
        raquete1_y += vel_raquete

    # Movimento da "IA" (simplesmente segue a bola)
    if raquete2_y + raquete_altura // 2 < bola_y:
        raquete2_y += vel_raquete
    elif raquete2_y + raquete_altura // 2 > bola_y:
        raquete2_y -= vel_raquete

    # Movimento da bola
    bola_x += vel_bola_x
    bola_y += vel_bola_y

    # Colisão com o topo e fundo
    if bola_y <= 0 or bola_y >= ALTURA - bola_tam:
        vel_bola_y *= -1

    # Colisão com as raquetes
    if (bola_x <= 20 and raquete1_y < bola_y < raquete1_y + raquete_altura) or \
       (bola_x >= LARGURA - 20 - bola_tam and raquete2_y < bola_y < raquete2_y + raquete_altura):
        vel_bola_x *= -1

    # Resetar bola se sair da tela
    if bola_x < 0 or bola_x > LARGURA:
        bola_x = LARGURA // 2
        bola_y = ALTURA // 2
        vel_bola_x *= -1

    # Desenhar tudo
    TELA.fill(PRETO)
    pygame.draw.rect(TELA, BRANCO, (10, raquete1_y, raquete_largura, raquete_altura))
    pygame.draw.rect(TELA, BRANCO, (LARGURA - 20, raquete2_y, raquete_largura, raquete_altura))
    pygame.draw.ellipse(TELA, BRANCO, (bola_x, bola_y, bola_tam, bola_tam))
    pygame.draw.aaline(TELA, BRANCO, (LARGURA // 2, 0), (LARGURA // 2, ALTURA))

    pygame.display.flip()
    relogio.tick(60)
