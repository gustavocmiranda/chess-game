import pygame
from pieces.piece import Piece

class Pawn (Piece) :
    def __init__(self, white: bool) -> None:
        pygame.sprite.Sprite.__init__(self)        
        super().__init__(white)

        if white == True:
            self.image = pygame.image.load('assets\Piece=Pawn, Side=White.png')
        else:
            self.image = pygame.image.load('assets\Piece=Pawn, Side=Black.png')
        
        self.rect = self.image.get_rect()

    def move_allowed(self, x,y) -> bool:
        # first move can be a 2 spaces move
        if self.white == True:
            if (self.x == x) and (self.y - y == 1): 
                return True
            else:
                return False
        else:
            if (self.x == x) and (y - self.y == 1): 
                return True
            else:
                return False
    
    def move(self, x, y) -> None:
        
        return super().move()