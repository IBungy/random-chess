import chess
import random

def random_move(board, color=None):
    if color == "white":
        turn_bool = chess.WHITE
    elif color == "black":
        turn_bool = chess.BLACK
    candidate.turn = turn_bool
    legal_moves = list(candidate.legal_moves)
    if legal_moves not None:
        return random.choice(legal_moves)
    else:
        raise Exception("Draw or checkmate detected")

def main(board):
    move = random_move(board)
    return move


if __name__ == "__main__":
    main()




