
import chess

ChessBoard = chess.Board
DEPTH = 4
CHECKMATE = 1e5

def negaAbp(ChessBoard, Depth, Alpha, Beta, Player):
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
    # imply move-ordering: moves that produce better score should be examined first
    global bestMove
    max_score = -CHECKMATE
    for legal_move in ChessBoard.legal_moves:
        move = chess.Move.from_uci(str(legal_move))
        ChessBoard.push(move)
        # since next Player is the opposite so -beta becomes alpha of next Player, and -alpha becomes beta
        score = -negaAbp(ChessBoard, Depth-1, -Beta, -Alpha, -Player)
        if score > max_score:
            max_score = score
            if Depth == Depth:
                bestMove = move
        ChessBoard.pop()
        if max_score > Alpha: # pruning
            Alpha = max_score
        if Alpha >= Beta:
            break
    return max_score

def findBestMove(self, ChessBoard, Depth):
    if ChessBoard.is_checkmate():
        return chess.Move.null()
    start = time.time()
    global bestMove
    bestMove = None
    # parse 1 if white's turn, -1 if black's turn
    # initial: alpha = -CHEKMATE, beta = CHECKMATE
    negaAbp(ChessBoard, Depth, -CHECKMATE, CHECKMATE, 1 if ChessBoard.turn else -1)
    end = time.time()
    print("Time: {} s".format(end-start))
    return bestMove
