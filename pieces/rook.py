import pygame
from pieces.piece import Piece

class Rook (Piece) :
    def __init__(self, white: bool) -> None:
        pygame.sprite.Sprite.__init__(self)        
        super().__init__(white)

        if white == True:
            self.image = pygame.image.load('assets\Piece=Rook, Side=White.png')
        else:
            self.image = pygame.image.load('assets\Piece=Rook, Side=Black.png')
        
        self.rect = self.image.get_rect()

    def move(self):
        pass