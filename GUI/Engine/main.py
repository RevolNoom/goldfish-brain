#!/usr/bin/python3
import Minimax
import AlphaBeta
import Negamax
import NullMove 
import chess
import Evaluator
import time

c = chess.Board()

# Count running time 
e = Evaluator.EvaluatorPosition()
StartTime = time.monotonic()
e.Evaluate(c)
EndTime = time.monotonic()
print(EndTime-StartTime)

"""
#engine = Minimax.Minimax() 
#engine = Negamax.Negamax() 
#engine = AlphaBeta.AlphaBeta() 
engine = NullMove.NullMove() 

while not c.is_game_over():
    move = engine.findBestMove(c, 5)
    if c.turn == chess.WHITE:
        print(str(c.ply()//2+1) + "." + str(move))
    else:
        print(str(c.ply()//2+1) + "..." + str(move))
    c.push(move)
    print(c)
    print("\n")

print("Game ended")
"""

