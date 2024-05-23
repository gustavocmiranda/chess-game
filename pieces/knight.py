import pygame
from pieces.piece import Piece

class Knight (Piece) :
    def __init__(self, white: bool) -> None:
        pygame.sprite.Sprite.__init__(self)        
        super().__init__(white)

        if white == True:
            self.image = pygame.image.load('assets\Piece=Knight, Side=White.png')
        else:
            self.image = pygame.image.load('assets\Piece=Knight, Side=Black.png')
        
        self.rect = self.image.get_rect()

    def move_allowed(self, x, y) -> bool:
        if (abs(self.x - x) != abs(self.y - y)) and (abs(self.x - x) in [1,2]) and (abs(self.y - y) in [1,2]):
            return True
        return False

    def move(self):
        pass