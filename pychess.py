#!/usr/bin/python3

import sys
import chess
import Minimax as mm


def PrintHelpThenExit():
    helpfile = open("pychess.help", "r")
    a = str(helpfile.read())
    print(a)
    quit()


def BestMove():
    if len(sys.argv) not in [4, 5]:
        PrintHelpThenExit()

    # Load the arguments

    board = chess.Board(sys.argv[2])

    AlgorithmName = sys.argv[3]
    AlgorithmTable = {"minimax" : mm.Minimax()}
    algorithm = AlgorithmTable[AlgorithmName]
    if algorithm == None:
        print("Unknown Algorithm: " + algorithm)

    depth = None
    if len(sys.argv) == 5:
        depth = sys.argv[4]
    
    # Return the result
    print(algorithm.NextBestMove(board))


# MAIN EXECUTION:

if len(sys.argv) == 1 or sys.argv[1] == "help" or sys.argv[1] == "--help":
    PrintHelpThenExit()

BestMove()

