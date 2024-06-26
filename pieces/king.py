import pygame
from pieces.piece import Piece

class King (Piece) :
    def __init__(self, white: bool) -> None:
        pygame.sprite.Sprite.__init__(self)        
        super().__init__(white)

        if white == True:
            self.image = pygame.image.load('assets\Piece=King, Side=White.png')
        else:
            self.image = pygame.image.load('assets\Piece=King, Side=Black.png')
        
        self.rect = self.image.get_rect()

    def move_allowed(self, x, y) -> bool:
        if abs(self.x - x) <= 1 and abs(self.y - y) <= 1:
            return True
        return False

    def move(self):
        pass

    def is_checked(self):
        pass

    def is_mated(self):
        pass