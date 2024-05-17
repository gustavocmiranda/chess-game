class Piece:
    def __init__(self, white:bool) -> None:
        self.white = white
    
    def move_allowed(self) -> bool:
        # check if this piece's king is going to get checked when this piece is moved
        # if it is -> false (move not allowed)
        # if it is not -> true (move is allowed)

        # check if position is occupied and cannot capture
        pass

