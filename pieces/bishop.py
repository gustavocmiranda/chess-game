from pieces.piece import Piece
import pygame

class Bishop (Piece) :
    def __init__(self, white: bool) -> None:
        pygame.sprite.Sprite.__init__(self)
        super().__init__(white)
        if white == True:
            self.image = pygame.image.load('./assets/W_Bishop.png')
        else:
            self.image = pygame.image.load('./assets/B_Bishop.png')
        
        self.rect = self.image.get_rect() 

    def move(self):
        pass