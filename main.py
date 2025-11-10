import chess
import random
import sys

def random_move(board):
    candidate = board.copy()
    legal_moves = list(candidate.legal_moves)
    if legal_moves:
        return random.choice(legal_moves)
    else:
        raise Exception("Draw or checkmate detected")

def main(board_fen):
    board = chess.Board(board_fen)
    move = random_move(board)
    return move

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py '<FEN>'")
        sys.exit(1)

    fen = sys.argv[1]
    

    move = main(fen)
    print(move)



