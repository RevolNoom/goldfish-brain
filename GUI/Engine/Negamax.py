import chess
import Engine
import Evaluator

CHECKMATE = 1e5

class Negamax(Engine.Engine):
    _evaluator = Evaluator.EvaluatorSunfish()

    def nega(self, ChessBoard, Depth):
        Player = (ChessBoard.turn-0.5)*2

        # The stop case: king is captured or draw play once
        # case: check-mate
        if ChessBoard.is_checkmate():
            return Player * CHECKMATE
        # case: Terminal node: Game over
        if ChessBoard.is_insufficient_material():
            return 0
        # case: find till the last children
        if Depth == 0:
            return Player * self._evaluator.Evaluate(ChessBoard)
        # backtrack and find children
        bestMove = None
        max_score = -CHECKMATE
        for legal_move in ChessBoard.legal_moves:
            move = chess.Move.from_uci(str(legal_move))
            ChessBoard.push(move)
            score = -self.nega(ChessBoard, Depth-1)[1]
            if score > max_score:
                max_score = score
                if Depth == Depth:
                    bestMove = move
            ChessBoard.pop()
        return (bestMove, max_score)

    def findBestMove(self, ChessBoard, Depth):
        return self.nega(ChessBoard, Depth)[0]

n = Negamax()
n.findBestMove(chess.Board(),3)
