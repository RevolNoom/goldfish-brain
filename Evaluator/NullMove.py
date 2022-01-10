import chess
import chess.polyglot as poly
import Evaluator
import Engine

class NullMove(Engine.Engine):

    _evaluator = Evaluator.EvaluatorPosition()

    def findBestMove(self, chessBoard, depth):
        return self._evaluate(chessBoard, depth)[1]

    def _evaluate(self, chessBoard, depth):
            bestMove = chess.Move.null()
            alpha = -999999
            beta = 999999

            # Check this turn for White or Black
            if chessBoard.turn:
                bestScore = -999999
                for move in chessBoard.legal_moves:
                    chessBoard.push(move)
                    score = self._NullMoveP(chessBoard, depth - 1, alpha, beta, False, True)
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
                bestScore = 999999
                for move in chessBoard.legal_moves:
                    chessBoard.push(move)
                    score = self._NullMoveP(chessBoard, depth - 1, alpha, beta, True,True)
                    chessBoard.pop()
                    if score < bestScore:
                        bestScore = score
                        bestMove = move
                    if beta >= score:
                        beta = score
                    if alpha >= beta:
                        break
                return bestScore, bestMove


    def _NullMoveP(self, chessBoard, depth, alpha, beta, isMax,NMP):
        if chessBoard.is_checkmate():
            if isMax:
                return -999999
            else:
                return 999999
        if chessBoard.is_insufficient_material(): 
            return 0

        if depth == 0:
            return self._evaluator.Evaluate(chessBoard)
        
        if (NMP == True and depth >= 4):
            currentMove = chess.Move.null()
            # move = move in chessBoard.legal_moves
            # currentMove = move[0]
            chessBoard.push(currentMove)
            # chessBoard.push(currentMove)
            score = -self._nullMoveP(chessBoard, depth-3, -beta, 1 - beta, isMax, False)
            chessBoard.pop()
            if (score >= beta):
                return score  #found cut-off
            else:
                depth += 3 #if cut-off not found, return initial depth
        if isMax:
            bestScore = -999999
            for move in chessBoard.legal_moves:
                chessBoard.push(move)
                score = self._NullMoveP(chessBoard, depth - 1, alpha, beta, False,False)
                chessBoard.pop()

                if alpha < score:
                    alpha = score

                if bestScore < score:
                    bestScore = score
                    
                if alpha >= beta:
                    break
            return bestScore
                
        else:
            bestScore = 999999
            for move in chessBoard.legal_moves:
                chessBoard.push(move)
                score = self._NullMoveP(chessBoard, depth - 1, alpha, beta, True, False)
                chessBoard.pop()

                if beta >= score:
                    beta = score

                if bestScore > score:
                    bestScore = score

                if alpha >= beta:
                    break
            return bestScore

