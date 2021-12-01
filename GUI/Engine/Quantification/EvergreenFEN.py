#!/usr/bin/python3
import chess

evergreen = open("evergreen", "r")

board = chess.Board()


while 1:
    nextmove = evergreen.readline()
    if nextmove == "":
        break

    nextmove = nextmove.strip()

    board.push_san(nextmove)
    print(board.fen())
