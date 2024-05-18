import pygame
from pieces.piece import Piece

class Invisible (pygame.sprite.Sprite) :
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)        
        super().__init__()
        self.white = None

        self.image = pygame.Surface([10, 15])
        
        self.rect = self.image.get_rect()
        self.image.set_alpha(0)