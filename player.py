from pieces.king import King

class Player:
    def __init__(self, white:bool) -> None:
        self.white = white
        self.pieces = {}
        self.king = King(white=white)
    
    def move_piece(self):
        pass