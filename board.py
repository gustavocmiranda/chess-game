from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.rook import Rook

class Board:
    def __init__(self) -> None:
        self.display = [[Rook(white=False), Knight(white=False), Bishop(white=False), Queen(white=False), King(white=False), Bishop(white=False), Knight(white=False), Rook(white=False)],
                        [Pawn(white=False), Pawn(white=False), Pawn(white=False), Pawn(white=False), Pawn(white=False), Pawn(white=False), Pawn(white=False), Pawn(white=False)],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [Pawn(white=True), Pawn(white=True), Pawn(white=True), Pawn(white=True), Pawn(white=True), Pawn(white=True), Pawn(white=True), Pawn(white=True)],
                        [Rook(white=True), Knight(white=True), Bishop(white=True), King(white=True), Queen(white=True), Bishop(white=True), Knight(white=True), Rook(white=True)],]