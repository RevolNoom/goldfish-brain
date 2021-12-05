import chess
import chess.polyglot as poly
import Evaluator
import Engine

class AlphaBeta(Engine.Engine):

    _evaluator = Evaluator.EvaluatorPosition()

    def findBestMove(self, chessBoard, depth):
        """
        This function returns the next move of the computer
        """
        return self._evaluate(chessBoard, depth)[0]

    def _evaluate(self, chessBoard, depth):
        """
        Return the next move and score for the computer 
        """
        try:
            move = poly.MemoryMappedReader("human.bin").weighted_choice(chessBoard).move
            return self._evaluator.evaluatePoint(chessBoard), move
        except:
            # Initial the bestMove is null, alpha = -INF, beta = INF
            bestMove = chess.Move.null()
            alpha = -999999
            beta = 999999

            # Check this turn for White or Black
            if chessBoard.turn:
                bestScore = -999999
                for move in chessBoard.legal_moves:
                    chessBoard.push(move)
                    score = self._alphaBeta(chessBoard, depth - 1, alpha, beta, False)
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
                    score = self._alphaBeta(chessBoard, depth - 1, alpha, beta, True)
                    chessBoard.pop()
                    if score < bestScore:
                        bestScore = score
                        bestMove = move
                    if beta >= score:
                        beta = score
                    if alpha >= beta:
                        break
                return bestScore, bestMove


    def _alphaBeta(self, chessBoard, depth, alpha, beta, isMax):
        # Faster calculate point in some situation
        # Checkmate
        if chessBoard.is_checkmate():
            if isMax:
                return -999999
            else:
                return 999999
        # Insufficient Material: Not enough condition to have the win player
        if chessBoard.is_insufficient_material(): 
            return 0

        if depth == 0:
            return self._evaluator.evaluatePoint(chessBoard)
        
        if isMax:
            bestScore = -999999
            for move in chessBoard.legal_moves:
                chessBoard.push(move)
                score = self._alphaBeta(chessBoard, depth - 1, alpha, beta, False)
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
                score = self._alphaBeta(chessBoard, depth - 1, alpha, beta, True)
                chessBoard.pop()

                if beta >= score:
                    beta = score

                if bestScore > score:
                    bestScore = score

                if alpha >= beta:
                    break
            return bestScore
