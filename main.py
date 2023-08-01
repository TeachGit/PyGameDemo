import pygame

pygame.init()
sw = 400
sh = 500
SCREEN = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("pygame test")

clock = pygame.time.Clock()
playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left key pressed")
            if event.key == pygame.K_RIGHT:
                print("right key pressed")
            if event.key == pygame.K_UP:
                print("up key pressed")
            if event.key == pygame.K_DOWN:
                print("down key pressed")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                print("left key pressed")
            if event.key == pygame.K_RIGHT:
                print("right key pressed")
            if event.key == pygame.K_UP:
                print("up key pressed")
            if event.key == pygame.K_DOWN:
                print("down key pressed")

    clock.tick(60)
