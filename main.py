import chess
import random

def random_move(board):
    LegalMoves = list(board.legal_moves)
    if LegalMoves not None:
        return random.choice(LegalMoves)
    else:
        raise Exception("Draw or checkmate detected")

def main(board):
    move = random_move(board)
    return move


if __name__ == "__main__":
    main()




