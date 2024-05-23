from pieces.piece import Piece
import pygame

class Bishop (Piece) :
    def __init__(self, white: bool) -> None:
        pygame.sprite.Sprite.__init__(self)
        super().__init__(white)
        if white == True:
            self.image = pygame.image.load('assets\Piece=Bishop, Side=White.png')
        else:
            self.image = pygame.image.load('assets\Piece=Bishop, Side=Black.png')
        
        self.rect = self.image.get_rect() 


    def move_allowed(self, x, y) -> bool:
        if abs(self.x - x) == abs(self.y - y):
            return True
        return False
    
    def move(self):
        pass