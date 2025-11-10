import chess
import random
import sys

def random_move(board, color):
    candidate = board.copy()
    candidate.turn = chess.WHITE if color == "white" else chess.BLACK
    legal_moves = list(candidate.legal_moves)
    if legal_moves:
        return random.choice(legal_moves)
    else:
        raise Exception("Draw or checkmate detected")

def main(board_fen, color):
    board = chess.Board(board_fen)
    move = random_move(board, color)
    return move

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 main.py '<fen_string>' <white|black>")
        sys.exit(1)

    fen = sys.argv[1]
    color = sys.argv[2].lower()

    move = main(fen, color)
    print(move)



