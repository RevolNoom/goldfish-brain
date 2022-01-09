"""
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
"""

import chess
import chess.polyglot as poly
import Evaluator
import Engine

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
            for move in chessBoard.legal_moves:
                chessBoard.push(move)
                score = self.nullMoveP(chessBoard, depth - 1, alpha, beta, False,1)
                chessBoard.pop()
                if score > bestScore:
                    bestScore = score
                    bestMove = move
                if score > alpha:
                    alpha = score
                if alpha >= beta:
                    break
            return bestScore, bestMove
        else:
            bestScore = MAX
            for move in chessBoard.legal_moves:
                chessBoard.push(move)
                score = self.nullMoveP(chessBoard, depth - 1, alpha, beta, True,1)
                chessBoard.pop()
                if score < bestScore:
                    bestScore = score
                    bestMove = move
                if beta >= score:
                    beta = score
                if alpha >= beta:
                    break
            return bestScore, bestMove


    def nullMoveP(self, chessBoard, depth, alpha, beta, isMax, NMP):
        if chessBoard.is_checkmate():
            if isMax:
                return MIN
            else:
                return MAX
        if chessBoard.is_insufficient_material(): 
            return 0
        if depth == 0:
            return self._evaluator.Evaluate(chessBoard)
        if (NMP == 1 and depth >= 4):
            move = chess.Move.null()
            chessBoard.push(move)
            score = -self.nullMoveP(chessBoard, depth - 3,-beta,1-beta, isMax, NMP)
            chessBoard.pop()
            if (score >= beta): 
                return beta 
        if isMax:
            bestScore = MIN
            for move in chessBoard.legal_moves:
                chessBoard.push(move)
                score = self.nullMoveP(chessBoard, depth - 1, alpha, beta, 0, NMP)
                chessBoard.pop()

                if alpha < score:
                    alpha = score

                if bestScore < score:
                    bestScore = score
                    
                if alpha >= beta:
                    break
            return bestScore               
        else:
            bestScore = MAX
            for move in chessBoard.legal_moves:
                chessBoard.push(move)
                score = self.nullMoveP(chessBoard, depth - 1, alpha, beta, True,0)
                chessBoard.pop()

                if beta >= score:
                    beta = score

                if bestScore > score:
                    bestScore = score

                if alpha >= beta:
                    break
            return bestScore
