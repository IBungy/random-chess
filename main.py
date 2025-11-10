import chess
import random

def random_move(board, color):
    candidate = board.copy()
    if color == "white":
        turn_bool = chess.WHITE
    elif color == "black":
        turn_bool = chess.BLACK
    candidate.turn = turn_bool
    legal_moves = list(candidate.legal_moves)
    if legal_moves:
        return random.choice(legal_moves)
    else:
        raise Exception("Draw or checkmate detected")

def main(board, color):
    move = random_move(board, color)
    return move


if __name__ == "__main__":
    main()




