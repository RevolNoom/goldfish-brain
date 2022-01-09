#!/usr/bin/python3
import sys
import chess
import Minimax as mm
import Negamax as ng 
import AlphaBeta as ab
import NullMove as nm
import Quiescence as qu


class Pychess:

    def __init__(self):
        # Mapping between arguments and what we need to do
        self.CommandTable = {
            "timing": self.Timing,
            "bestmove": self.BestMove,
            "legalmoves": self.LegalMoves,
            "move": self.Move,
            "status": self.Status}

        # Mapping between names and actual algorithms
        self.AlgorithmTable = {  "minimax" : mm.Minimax(),
                            "negamax" : ng.Negamax(),
                            "alphabeta" : ab.AlphaBeta(),
                            "nullmove": nm.NullMove(),
                            "quiescence": qu.Quiescence()}


    
    def Execute(self):
        if len(sys.argv) == 1 or sys.argv[1] == "help" or sys.argv[1] == "--help":
            self.PrintHelpThenExit()
    
        # Look up what we need to do
        command = self.CommandTable[sys.argv[1]]
        # And then do it
        command()


    def PrintHelpThenExit(self):
        helpfile = open("help.pychess", "r")
        a = str(helpfile.read())
        print(a)
        quit()


    def Timing(self):
        if len(sys.argv) not in [4, 5]: 
            self.PrintHelpThenExit()

        # Load the arguments

        board = chess.Board(sys.argv[2])

        AlgorithmName = sys.argv[3]

        algorithm = self.AlgorithmTable[AlgorithmName]
        if algorithm == None:
            print("Unknown Algorithm: " + algorithm)

        depth = None
        if len(sys.argv) == 5:
            depth = int(sys.argv[4])
        
        # Return the result
        print(str(algorithm.GetEvaluateTime(board, depth)[0]) + "s")


    def BestMove(self):
        if len(sys.argv) not in [4, 5]: 
            self.PrintHelpThenExit()

        # Load the arguments

        board = chess.Board(sys.argv[2])

        AlgorithmName = sys.argv[3]

        algorithm = self.AlgorithmTable[AlgorithmName]
        if algorithm == None:
            print("Unknown Algorithm: " + algorithm)

        depth = None
        if len(sys.argv) == 5:
            depth = int(sys.argv[4])
        
        # Return the result
        print(algorithm.findBestMove(board, depth))



    def LegalMoves(self):
        if len(sys.argv) != 3:
            self.PrintHelpThenExit()

        board = chess.Board(sys.argv[2])
        for i in board.legal_moves:
            print(i)


    def Move(self):
        if len(sys.argv) != 4:
            self.PrintHelpThenExit()

        board = chess.Board(sys.argv[2])
        try:
            board.push_uci(sys.argv[3])
            print(board.fen())

        except:
            print("ERROR")


    def Status(self):

        if len(sys.argv) != 3:
            self.PrintHelpThenExit()

        board = chess.Board(sys.argv[2])

        outcome = board.outcome()

        if outcome == None:
            print("-")
        else:
            print(outcome.result())



pychess = Pychess()
pychess.Execute()
