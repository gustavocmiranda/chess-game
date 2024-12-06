from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.rook import Rook
from pieces.invi import Invisible

class Board:
    def __init__(self) -> None:
        self.display = [[Rook(white=False), Knight(white=False), Bishop(white=False), King(white=False), Queen(white=False), Bishop(white=False), Knight(white=False), Rook(white=False)],
                        [Pawn(white=False), Pawn(white=False), Pawn(white=False), Pawn(white=False), Pawn(white=False), Pawn(white=False), Pawn(white=False), Pawn(white=False)],
                        [Invisible(), Invisible(), Invisible(), Invisible(), Invisible(), Invisible(), Invisible(), Invisible()],
                        [Invisible(), Invisible(), Invisible(), Invisible(), Invisible(), Invisible(), Invisible(), Invisible()],
                        [Invisible(), Invisible(), Invisible(), Invisible(), Invisible(), Invisible(), Invisible(), Invisible()],
                        [Invisible(), Invisible(), Invisible(), Invisible(), Invisible(), Invisible(), Invisible(), Invisible()],
                        [Pawn(white=True), Pawn(white=True), Pawn(white=True), Pawn(white=True), Pawn(white=True), Pawn(white=True), Pawn(white=True), Pawn(white=True)],
                        [Rook(white=True), Knight(white=True), Bishop(white=True), Queen(white=True), King(white=True), Bishop(white=True), Knight(white=True), Rook(white=True)],]
        

    def allocate_sprites(self, sprites_list) -> None:
        for row in range(8):
            for column in range(8):
                self.display[row][column].rect.x = (column)*68.5+8
                self.display[row][column].rect.y = (row)*72+7
                self.display[row][column].x = column
                self.display[row][column].y = row
                sprites_list.add(self.display[row][column])

    def print_display(self):
        for row in self.display:
            print(row)

    def create_new_empty(self, x,y,rectx,recty, sprites_list) -> None:
        new_invi = Invisible()
        new_invi.x = x
        new_invi.y = y
        new_invi.rect.x = rectx
        new_invi.rect.y = recty
        sprites_list.add(new_invi)

    def change_pieces(self, sprite1, sprite2) -> None:
        self.display[sprite1.y][sprite1.x] = sprite2
        self.display[sprite2.y][sprite2.x] = sprite1