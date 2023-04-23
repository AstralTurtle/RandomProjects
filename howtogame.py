import os as os 
import pygame as pygame
from pygame import image
# Initialize the game engine
pygame.init()

charSprites = [    
    "bluedinosprites/tile000.png", "bluedinosprites/tile001.png", "bluedinosprites/tile002.png", "bluedinosprites/tile003.png", 
    "bluedinosprites/tile004.png", "bluedinosprites/tile004.png", "bluedinosprites/tile006.png", "bluedinosprites/tile007.png",    
    "bluedinosprites/tile008.png", "bluedinosprites/tile009.png", "bluedinosprites/tile010.png", "bluedinosprites/tile011.png",    
    "bluedinosprites/tile012.png", "bluedinosprites/tile013.png", "bluedinosprites/tile014.png", "bluedinosprites/tile015.png",    
    "bluedinosprites/tile016.png", "bluedinosprites/tile017.png", "bluedinosprites/tile018.png", "bluedinosprites/tile019.png",    
    "bluedinosprites/tile020.png", "bluedinosprites/tile021.png", "bluedinosprites/tile022.png", "bluedinosprites/tile023.png"]

# make window
size = (100, 100)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.image = pygame.image.load("bluedinosprites/tile000").convert_alpha()
        
        
        self.speed = 5
        self.sprites = charSprites
        self.currentSprite = 0
        self.heath = 100
        self.mana = 100
        self.image = pygame.image.load(self.sprites[self.currentSprite]).convert_alpha()
        self.rect = self.image.get_rect()

    
    def setSprite(self, sprite):
        self.curentSprite = sprite
        self.image = pygame.image.load(self.sprites[self.curentSprite]).convert_alpha()

playerChar = Player()
all_sprites_list = pygame.sprite.Group()
setup = True

# game loop
active = True
while active:
    if setup == True:
        screen.blit(playerChar.image, (0, 0))
        # all_sprites_list.add(playerChar)
        setup = False
        pygame.display.flip()
    
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        elif event.type == pygame.KEYDOWN:
            if pygame.K_ESCAPE in keys:
                active = False
    
    # draw background
    screen.fill((255, 255, 255))
    
    # update screen
    pygame.display.flip()