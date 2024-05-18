import pygame
from pieces.piece import Piece

class Queen (Piece) :
    def __init__(self, white: bool) -> None:
        pygame.sprite.Sprite.__init__(self)        
        super().__init__(white)

        if white == True:
            self.image = pygame.image.load('./assets/W_Queen.png')
        else:
            self.image = pygame.image.load('./assets/B_Queen.png')
        
        self.rect = self.image.get_rect()

    def move(self):
        pass