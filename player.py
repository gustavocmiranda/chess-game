from pieces.king import King
from board import Board

class Player:
    def __init__(self, board:Board, white:bool) -> None:
        self.white = white
        self.pieces = {}
        self.king = board.display[7][5] if white else board.display[0][4]
    
    def select_piece(self, all_sprites_list, x,y, white_moves):
        for sprite in all_sprites_list:
            if x >= sprite.rect.x and x <= (sprite.rect.x + sprite.rect.width):
                if y >= sprite.rect.y and y <= (sprite.rect.y + sprite.rect.height):
                    if sprite.white == white_moves:
                        #print('hit')
                        #print(sprite.x)
                        #print(sprite.y)
                        print(sprite)
                        return sprite
                    else:
                        print('not your turn')

    def select_second_piece(self, all_sprites_list, x,y):
        for sprite in all_sprites_list:
            if x >= sprite.rect.x and x <= (sprite.rect.x + sprite.rect.width):
                if y >= sprite.rect.y and y <= (sprite.rect.y + sprite.rect.height):
                    """ print('hit')
                    print(sprite.x)
                    print(sprite.y) """
                    print(sprite)
                    return sprite

    def move_piece(self, board, sprite1, sprite2):
        #board.print_display()
        board.change_pieces(sprite1, sprite2)
        #board.print_display()
        # changing logical position
        sprite1.x, sprite2.x = sprite2.x, sprite1.x
        sprite1.y, sprite2.y = sprite2.y, sprite1.y
        # changing drawing position
        sprite1.rect.x, sprite2.rect.x = sprite2.rect.x, sprite1.rect.x
        sprite1.rect.y, sprite2.rect.y = sprite2.rect.y, sprite1.rect.y
        print('changed')

    def capture(self, board, sprite1, sprite2, sprites_list):
        board.create_new_empty(sprite1.x, sprite1.y, sprite1.rect.x, sprite1.rect.y, sprites_list)
        sprite1.rect.x = sprite2.rect.x
        sprite1.rect.y = sprite2.rect.y
        sprite1.x = sprite2.x
        sprite1.y = sprite2.y
        sprite2.kill()