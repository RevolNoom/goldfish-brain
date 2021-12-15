#from IPython.display import SVG, display
import chess
import Evaluator
#import chess.engine
import Engine
#import chess.svg
import chess.polyglot as poly
#import time


"""
This class for implement quiescence search algorithm
@author: Dao Duc Manh
@version: 1.0.0
"""
class Quiescence(Engine.Engine):

    _evaluator = Evaluator.EvaluatorPosition()
	
    """
    @returns: move the next move of computer
    """
    def findBestMove(self, chessBoard, depth):
        return self._findBestMove(chessBoard, depth)[1]
	
    """
    Take the value of each piece to compare
    @return value of selected piece
    """	
    def _get_piece_val(self, piece):
        if(piece == None):
            return 0
        value = 0
        if piece == "P" or piece == "p":
            value = 10
        if piece == "N" or piece == "n":
            value = 30
        if piece == "B" or piece == "b":
            value = 30
        if piece == "R" or piece == "r":
            value = 50
        if piece == "Q" or piece == "q":
            value = 90
        if piece == 'K' or piece == 'k':
            value = 900
        #value = value if (board.piece_at(place)).color else -value
        return value
    
    """
    Take the favorable move for current player
    @returns: boolean True/False for favorable move
    """	
    def _is_favorable_move(self, board: chess.Board, move: chess.Move) -> bool:
        if move.promotion is not None:
            return True
        if board.is_capture(move) and not board.is_en_passant(move):
            if (self._get_piece_val(board.piece_type_at(move.from_square)) < self._get_piece_val(board.piece_type_at(move.to_square))) or (len(board.attackers(board.turn, move.to_square)) > len(board.attackers(not board.turn, move.to_square))):
                return True
        return False
    	
    """
    Take all the captured move that may be not quiet
    @returns: list of capture move
    """
    def _list_favorable_move(self, chessBoard):
        re_list = []
        for move in chessBoard.legal_moves:
            if chessBoard.is_capture(move):
                re_list.append(move)
        return re_list
    	
    """
    Extend quiescence search applied minimax
    @returns: bestScore
    """
    def _quiescence_search(self, chessBoard, depth, isMax):
        # check-mate
        if chessBoard.is_checkmate():
            if isMax:
                return -10000
            else:
                return 10000
        
        # draw
        elif chessBoard.is_stalemate():
            return 0
    
        # terminal note
        elif chessBoard.is_insufficient_material():
            return 0
    
        elif depth == 0:
            return self._evaluator.Evaluate(chessBoard)
            
        else:
            # recursively search node children
            if isMax:
                bestScore = -1e5
                for move in chessBoard.legal_moves:
                    chessBoard.push(move)
                    score = self._quiescence_search(chessBoard, depth-1, False)
                    chessBoard.pop()
                
                    # update bestScore
                    bestScore = max(score, bestScore)
                return bestScore
                
            else:
                bestScore = 1e5
                for move in chessBoard.legal_moves:
                    chessBoard.push(move)
                    score = self._quiescence_search(chessBoard, depth-1, True)
                    chessBoard.pop()
                
                    # upadate bestScore
                    bestScore = min(score, bestScore)
                return bestScore
            	
    """
    Normal search applied here: alpha-beta
    @retuns: bestScore
    """
    def _alpha_beta(self, chessBoard, depth, alpha, beta, isMax):
        # check-mate
        if chessBoard.is_checkmate():
            if isMax:
                return -10000
            else:
                return 10000
               
        # draw
        elif chessBoard.is_stalemate():
            return 0
    
        # terminal node
        elif chessBoard.is_insufficient_material():
            return 0
    
        elif depth == 0:
            # check if node is quite
            # allPossibleMove = [move for move in chessBoard.legal_moves if self._is_favorable_move(chessBoard, move)]
            allPossibleMove = self._list_favorable_move(chessBoard)
            for move in chessBoard.legal_moves:
                if move not in allPossibleMove:
                    return self._evaluator.Evaluate(chessBoard)
                # node isn quite
                else:
                    if isMax:
                        return self._quiescence_search(chessBoard, 1, False)
                    else:
                        return self._quiescence_search(chessBoard, 1, True)
        else:
            # recursively search node children with alpha_beta
            if isMax:
                bestScore = -10000
                for move in chessBoard.legal_moves:
                    chessBoard.push(move)
                    score = self._alpha_beta(chessBoard, depth-1, alpha, beta, False)
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
                bestScore = 10000
                for move in chessBoard.legal_moves:
                    chessBoard.push(move)
                    score = self._alpha_beta(chessBoard, depth-1, alpha, beta, True)
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
    
    """
    Static function for findding the best move
    @returns: bestScore, move
    """	
    def _findBestMove(self, chessBoard, depth):
        # LAM'S NOTE: Manh is using absolute path here, which does not exist in my machine
        #try:
        #    move = poly.MemoryMappedReader("/home/genkibaskervillge/Documents/goldfish-brain/human.bin").weighted_choice(chessBoard).move
            # return self._evaluator.Evaluate(chessBoard), move
        #    return self._evaluator.Evaluate(chessBoard), move
        #except:

        # Initial the bestMove is null, alpha = -INF, beta = INF
        bestMove = chess.Move.null()
        alpha = -1e5
        beta = 1e5
        
        # Check this turn for White or Black
        if chessBoard.turn:
            bestScore = -999999
            for move in chessBoard.legal_moves:
                chessBoard.push(move)
                score = self._alpha_beta(chessBoard, depth - 1, alpha, beta, False)
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
                score = self._alpha_beta(chessBoard, depth - 1, alpha, beta, True)
                chessBoard.pop()
                if score < bestScore:
                    bestScore = score
                    bestMove = move
                if beta >= score:
                    beta = score
                if alpha >= beta:
                    break
            return bestScore, bestMove
            
