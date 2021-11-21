import chess

current_board = chess.Board
DEPTH = 4
CHECKMATE = 1e5

def nega(current_board, depth, player):
    # The stop case: king is captured or draw play once
    # case: check-mate
    if current_board.is_checkmate():
        return player * CHECKMATE
    # case: draw once
    if current_board.is_stalemate():
        return 0
    # case: Terminal node: Game over
    if current_board.is_insufficient_material():
        return 0
    # case: find till the last children
    if depth == 0:
        return player * evaluate(current_board)
    # backtrack and find children
    global bestMove
    max_score = -CHECKMATE
    for legal_move in current_board.legal_moves:
        move = chess.Move.from_uci(str(legal_move))
        current_board.push(move)
        score = -nega(current_board, depth-1, -player)
        if score > max_score:
            max_score = score
            if depth == DEPTH:
                bestMove = move
        current_board.pop()
    return max_score

def findBestMoveNega(current_board):
    if current_board.is_checkmate():
        return chess.Move.null()
    start = time.time()
    global bestMove
    bestMove = None
    # parse 1 if white's turn, -1 if black's turn
    nega(current_board, DEPTH, 1 if current_board.turn else -1)
    end = time.time()
    print("Time: {} s".format(end-start))
    return bestMove

def negaAbp(current_board, depth, alpha, beta, player):
    # The stop case: king is captured or draw play once
    # case: check-mate
    if current_board.is_checkmate():
        return player * CHECKMATE
    # case: draw once
    if current_board.is_stalemate():
        return 0
    # case: Terminal node: Game over
    if current_board.is_insufficient_material():
        return 0
    # case: find till the last children
    if depth == 0:
        return player * evaluate(current_board)
    # backtrack and find children
    # imply move-ordering: moves that produce better score should be examined first
    global bestMove
    max_score = -CHECKMATE
    for legal_move in current_board.legal_moves:
        move = chess.Move.from_uci(str(legal_move))
        current_board.push(move)
        # since next player is the opposite so -beta becomes alpha of next player, and -alpha becomes beta
        score = -negaAbp(current_board, depth-1, -beta, -alpha, -player)
        if score > max_score:
            max_score = score
            if depth == DEPTH:
                bestMove = move
        current_board.pop()
        if max_score > alpha: # pruning
            alpha = max_score
        if alpha >= beta:
            break
    return max_score

def findBestMoveNegaAbp(current_board):
    if current_board.is_checkmate():
        return chess.Move.null()
    start = time.time()
    global bestMove
    bestMove = None
    # parse 1 if white's turn, -1 if black's turn
    # initial: alpha = -CHEKMATE, beta = CHECKMATE
    nega(current_board, DEPTH, -CHECKMATE, CHECKMATE, 1 if current_board.turn else -1)
    end = time.time()
    print("Time: {} s".format(end-start))
    return bestMove
