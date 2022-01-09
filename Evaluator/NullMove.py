import chess
import Evaluator
import Engine
import chess.polyglot as poly

MAX = 999999
MIN = -999999

class NullMove(Engine.Engine):

    _evaluator = Evaluator.EvaluatorPosition()

    def findBestMove(self, chessBoard, depth):
        return self._findBestMove(chessBoard, depth)[1]

    def _findBestMove(self, chessBoard, depth):
        bestMove = chess.Move.null()
        alpha = -1e5
        beta = 1e5
        
        # Check this turn for White or Black
        if chessBoard.turn:
            bestScore = -999999
            for move in chessBoard.legal_moves:
                chessBoard.push(move)
                score = self._nullMoveP(chessBoard, depth - 1, alpha, beta, False, 1)
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
                score = self._nullMoveP(chessBoard, depth - 1, alpha, beta, True, 1)
                chessBoard.pop()
                if score < bestScore:
                    bestScore = score
                    bestMove = move
                if beta >= score:
                    beta = score
                if alpha >= beta:
                    break
            return bestScore, bestMove

    def _nullMoveP(self, chessBoard, depth, alpha, beta, isMax, NMP):
        # checkmate move
        if chessBoard.is_checkmate():
            if isMax:
                return MIN
            else:
                return MAX

        # draw
        elif chessBoard.is_stalemate():
            return 0
        
        # terminal node
        elif chessBoard.is_insufficient_material():
            return 0

        elif depth <= 0:
            return self._evaluator.Evaluate(chessBoard)
            # return algo._findBestMove(chessBoard, depth)[0]
        
        elif (NMP == 1 and depth >= 4):
            # chess.Move.null()
            move = move in chessBoard.legal_moves
            currentMove = move[0]
            chessBoard.push(currentMove)
            chessBoard.push(currentMove)
            score = -self._nullMoveP(chessBoard, depth / 2, -beta, 1 - beta, isMax, 0) #here we just set R = 1 for fast testing only
            chessBoard.pop()
            
            if (score >= beta):
                return beta
        else:
            if isMax:
                bestScore = MIN
                for move in chessBoard.legal_moves:
                    chessBoard.push(move)
                    score = self._nullMoveP(chessBoard, depth - 1, alpha, beta, False, 0)
                    chessBoard.pop()
                    # update alpha, bestScore
                    if alpha < score:
                        alpha = score
                    if bestScore < score:
                        bestScore = score
                
                    # cutoff
                    if alpha >= beta:
                        break
                return bestScore
            else:
                bestScore = MAX
                for move in chessBoard.legal_moves:
                    chessBoard.push(move)
                    score = self._nullMoveP(chessBoard, depth - 1, alpha, beta, True, 0)
                    chessBoard.pop()
                
                    # update beta, bestScore
                    if beta >= score:
                        beta = score
                    if bestScore > score:
                        bestScore = score
                    
                    # cutoff
                    if alpha >= beta:
                        break
                return bestScore
