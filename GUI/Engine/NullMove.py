import chess.polyglot as poly
import Evaluator
import Engine
import chess
import math

MAX = 999999
MIN = -999999

class NullMove(Engine.Engine):

    _evaluator = Evaluator.EvaluatorPosition()

    def findBestMove(self, chessBoard, depth):
        return self.evaluate(chessBoard, depth)[1]

    def evaluate(self, chessBoard, depth):
        bestMove = chess.Move.null()
        alpha = MIN
        beta = MAX

        if chessBoard.turn:
            bestScore = MIN
        else:
            bestScore = MAX


        for move in chessBoard.legal_moves:
            chessBoard.push(move)
            score = self.nullMoveP(chessBoard, depth - 1, alpha, beta, 1)

            if chessBoard.turn and score >= bestScore:
                bestMove = move
                bestScore = score
                alpha = max(alpha, score)

            if not chessBoard.turn and score < bestScore:
                bestMove = move
                bestScore = score
                beta = min(beta, score)

            chessBoard.pop()

            if alpha >= beta:
                break

        return bestScore, bestMove




    def nullMoveP(self, chessBoard, depth, alpha, beta, NMP):
        bestScore = MAX
        if chessBoard.turn:
            bestScore = MIN

        if depth == 0:
            return self._evaluator.Evaluate(chessBoard)

        if NMP == 1:
            move = chess.Move.null()
            chessBoard.push(move)
            score = -self.nullMoveP(chessBoard, depth/2 , -beta, 1-beta, 0)

            chessBoard.pop()
            if (score >= beta): 
                return beta 

        for move in chessBoard.legal_moves:
            chessBoard.push(move)
            score = self.nullMoveP(chessBoard, depth - 1, alpha, beta, 0)
            chessBoard.pop()

            if chessBoard.turn:
                alpha = max(alpha, score)
                bestScore = max(bestScore, score)
            else:
                beta = min(beta, score)
                bestScore = min(bestScore, score)

            if alpha >= beta:
                break

        return bestScore
