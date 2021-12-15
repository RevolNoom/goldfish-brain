#!/usr/bin/python3

import chess
import Engine
import Evaluator


class Minimax(Engine.Engine):
    _evaluator = Evaluator.EvaluatorPosition()

    def findBestMove(self, ChessBoard, Depth):
        """ Return the next best move for the player-to-move """
        return self.Evaluate(ChessBoard, Depth)[0]


    def Evaluate(self, ChessBoard, Depth):
        """ Return (BestMove, Score) for the player-to-move """

        # Terminate condition
        # Return the latest move, with the score of the furthest position on the search tree
        if Depth < 1:
            return (ChessBoard.peek(), self._evaluator.Evaluate(ChessBoard))

        AllPossibleMoves = ChessBoard.legal_moves

        BestMove = None
        BestScore = 9999999
        if ChessBoard.turn == chess.WHITE:
            BestScore = -9999999
        
        for Move in AllPossibleMoves:
            ChessBoard.push(Move)
        
            # How to unpack tuple automatically?
            # CurrentMove, CurrentScore = self.EvaluateMove(ChessBoard, Move, Depth-1)
            em = self.Evaluate(ChessBoard, Depth-1)

            # If we're evaluating white's move
            # Then we've made a move for white, and thus it's currently black's turn 
            # That's why the condition for "if" is reversed
            updateCondition = em[1] < BestScore
            if not (ChessBoard.turn == chess.WHITE):    
                updateCondition = em[1] > BestScore

            if updateCondition:
                BestMove = ChessBoard.peek() #The current move
                BestScore = em[1] 

            ChessBoard.pop()

        return (BestMove, BestScore)
