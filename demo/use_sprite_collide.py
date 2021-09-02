import sys, pygame

pygame.init()

size = width, height = 320,240
speed = [2, 2]
black = 255, 255, 255

screen = pygame.display.set_mode((320, 240))

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height, init_pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos

sprite_1 = Block(pygame.Color(255, 0 ,0), 50, 50, (50, 50))
sprite_2 = Block(pygame.Color(0, 255, 0), 50, 50, (90, 90))

while 1 :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(sprite_1.image, sprite_1.rect)
    screen.blit(sprite_2.image, sprite_2.rect)

    rest = pygame.sprite.collide_rect(sprite_1, sprite_2)
    print('rest', rest)

    rest2 = pygame.sprite.collide_rect_ratio(0.5)(sprite_1, sprite_2)
    print('rest2', rest2)

    pygame.display.flip()