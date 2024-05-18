import pygame
from pieces.piece import Piece

class Pawn (Piece) :
    def __init__(self, white: bool) -> None:
        pygame.sprite.Sprite.__init__(self)        
        super().__init__(white)

        if white == True:
            self.image = pygame.image.load('./assets/W_Pawn.png')
        else:
            self.image = pygame.image.load('./assets/B_Pawn.png')
        
        self.rect = self.image.get_rect()

    def move(self):
        # if white -> y should move up,
        # if not white -> y should move down
        pass