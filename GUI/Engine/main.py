#!/usr/bin/python3

import Minimax
import AlphaBeta
import chess

c = chess.Board()
engine = AlphaBeta.AlphaBeta() 

#print(engine.GetEvaluateTime(c, 3))

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
