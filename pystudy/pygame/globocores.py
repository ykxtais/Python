import pygame
from pygame.locals import QUIT
import math

pygame.init()

screen = pygame.display.set_mode((800, 600), 0, 32)
clock = pygame.time.Clock()

sair = False
frame = 0

while not sair:
    screen.fill((0, 0, 0))

    altura_max = 300
    largura_max = 400

    # cores variando com seno e cosseno 
    r = int(127 + 128 * math.sin(frame * 0.05))
    g = int(127 + 128 * math.sin(frame * 0.07))
    b = int(127 + 128 * math.sin(frame * 0.09))
    cor1 = (r, g, b)
    cor2 = (b, r, g)

    for i in range(10):
        altura = 30 * (i + 1)
        deslocamento = altura // 2
        y = altura_max - (100 + deslocamento)
        pygame.draw.ellipse(screen, cor1, ((100, y), (400, altura)), 3)

    for i in range(10):
        largura = 40 * (i + 1)
        deslocamento = largura // 2
        x = largura_max - (100 + deslocamento)
        pygame.draw.ellipse(screen, cor2, ((x, y), (largura, altura)), 3)

    pygame.display.update()
    clock.tick(30)  # 30 fps
    frame += 1

    for event in pygame.event.get():
        if event.type == QUIT:
            sair = True
