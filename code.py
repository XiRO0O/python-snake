import pygame, sys

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
test_surface = pygame.Surface((100,200))
test_surface.fill((200,100,0))
x_pos = 200

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((100,160,60))
    x_pos += 1
    screen.blit(test_surface,(x_pos,250))
    pygame.display.update()
    clock.tick(60)