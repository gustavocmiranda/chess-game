import pygame
from pieces.piece import Piece

class Invisible (pygame.sprite.Sprite) :
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)        
        super().__init__()

        self.image = pygame.Surface([10, 15]) 
        self.image.fill((167, 255, 100)) 
        
        self.rect = self.image.get_rect()