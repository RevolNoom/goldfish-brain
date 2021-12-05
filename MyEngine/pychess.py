#!/usr/bin/python3

import sys
import chess
import AlphaBeta as ab


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
    AlgorithmTable = {"alphabeta" : ab.AlphaBeta}
    algorithm = AlgorithmTable[AlgorithmName]
    if algorithm == None:
        print("Unknown Algorithm: " + algorithm)

    depth = None
    if len(sys.argv) == 5:
        depth = int(sys.argv[4])
    
    # Return the result
    print(algorithm.findBestMove(board, depth))


def LegalMoves():
    if len(sys.argv) != 3:
        PrintHelpThenExit()

    board = chess.Board(sys.argv[2])
    for i in board.legal_moves:
        print(i)


def Move():
    if len(sys.argv) != 4:
        PrintHelpThenExit()

    board = chess.Board(sys.argv[2])
    try:
        board.push_uci(sys.argv[3])
        print(board.fen())

    except:
        print("ERROR")


def Status():

    if len(sys.argv) != 3:
        PrintHelpThenExit()

    board = chess.Board(sys.argv[2])

    outcome = board.outcome()

    if outcome == None:
        print("-")
    else:
        print(outcome.result())


# MAIN EXECUTION:

if len(sys.argv) == 1 or sys.argv[1] == "help" or sys.argv[1] == "--help":
    PrintHelpThenExit()

# A mapping between arguments and what we need to do
CommandTable = {
    "bestmove": BestMove,
    "legalmoves": LegalMoves,
    "move": Move,
    "status": Status}

#try:
# Look up what we need to do
command = CommandTable[sys.argv[1]]
# And then do it
command()
#except:
    # There's an error, which indicate that we can't match
    # argument 1 with any Command 
#    print("Unknown command: " + sys.argv[1])
                

