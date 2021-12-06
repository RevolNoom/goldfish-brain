
import chess
import Engine
import Evaluator

CHECKMATE = 1e5

class NegamaxAlphaBetaPruning(Engine.Engine):
    _evaluator = Evaluator.EvaluatorSunfish()

    def negaAbp(self, ChessBoard, Depth, Alpha, Beta, Player):
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
            return Player * self._evaluator.Evaluate(ChessBoard)
        # backtrack and find children
        # imply move-ordering: moves that produce better score should be examined first
        bestMove = None
        max_score = -CHECKMATE
        for legal_move in ChessBoard.legal_moves:
            move = chess.Move.from_uci(str(legal_move))
            ChessBoard.push(move)
            # since next Player is the opposite so -beta becomes alpha of next Player, and -alpha becomes beta
            score = -self.negaAbp(ChessBoard, Depth-1, -Beta, -Alpha, -Player)
            if score > max_score:
                max_score = score
                if Depth == Depth:
                    bestMove = move
            ChessBoard.pop()
            if max_score > Alpha: # pruning
                Alpha = max_score
            if Alpha >= Beta:
                break
        return (bestMove, max_score)

    def findBestMove(self, ChessBoard, Depth):
        return self.negaAbp(ChessBoard, Depth, -CHECKMATE, CHECKMATE, 1 if ChessBoard.turn else -1)[0]
