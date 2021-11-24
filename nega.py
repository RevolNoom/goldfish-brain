import chess

ChessBoard = chess.Board
DEPTH = 4
CHECKMATE = 1e5

def nega(ChessBoard, Depth, Player):
    # The stop case: king is captured or draw play once
    # case: check-mate
    if ChessBoard.is_checkmate():
        return Player * CHECKMATE
    # case: draw once
    if ChessBoard.is_stalemate():
        return 0
    # case: Terminal node: Game over
    if ChessBoard.is_insufficient_material():
        return 0
    # case: find till the last children
    if Depth == 0:
        return Player * evaluate(ChessBoard)
    # backtrack and find children
    global bestMove
    max_score = -CHECKMATE
    for legal_move in ChessBoard.legal_moves:
        move = chess.Move.from_uci(str(legal_move))
        ChessBoard.push(move)
        score = -nega(ChessBoard, Depth-1, -Player)
        if score > max_score:
            max_score = score
            if Depth == Depth:
                bestMove = move
        ChessBoard.pop()
    return max_score

def findBestMove(self, ChessBoard, Depth):
    if ChessBoard.is_checkmate():
        return chess.Move.null()
    start = time.time()
    global bestMove
    bestMove = None
    # parse 1 if white's turn, -1 if black's turn
    nega(ChessBoard, Depth, 1 if ChessBoard.turn else -1)
    end = time.time()
    print("Time: {} s".format(end-start))
    return bestMove
