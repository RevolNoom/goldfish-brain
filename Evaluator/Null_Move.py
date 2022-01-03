
import chess.polyglot as poly
import Evaluator
import Engine

MAX = 999999
MIN = -999999

class Null_Move(Engine.Engine):

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
            return self.evaluator.evaluatePoint(chessBoard)
        if (NMP == 1 and depth >= 4):
            move = chess.Move.null()
            board.push(move)
            score = -nullMoveP(chessBoard, depth - 3,-beta,1-beta, isMax, 0)
            board.pop()
            if (score >= beta): 
                return beta 
        if isMax:
            bestScore = MIN
            for move in chessBoard.legal_moves:
                chessBoard.push(move)
                score = self.nullMoveP(chessBoard, depth - 1, alpha, beta,0)
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