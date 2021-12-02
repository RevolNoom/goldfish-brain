#!/usr/bin/python3

import Minimax
import chess

c = chess.Board()
engine = Minimax.Minimax()

print(engine.GetEvaluateTime(c, 3))
#
#while not c.is_game_over():
#    move = engine.NextBestMove(c)
#    if c.turn == chess.WHITE:
#        print(str(c.ply()//2+1) + "." + c.san(move))
#    else:
#        print(str(c.ply()//2+1) + "..." + c.san(move))
#    c.push(move)
#    print(c)
#    print("\n")
#
#print("Game ended")
