import pygame
from pieces.piece import Piece

class Knight (Piece) :
    def __init__(self, white: bool) -> None:
        pygame.sprite.Sprite.__init__(self)        
        super().__init__(white)

        if white == True:
            self.image = pygame.image.load('./assets/W_Knight.png')
        else:
            self.image = pygame.image.load('./assets/B_Knight.png')
        
        self.rect = self.image.get_rect()

    def move(self):
        pass