#!/usr/bin/python3

import time
import io
import sys

class Engine:
    def findBestMove(self, ChessBoard, Depth):
        print("zzz...")

    def GetEvaluateTime(self, ChessBoard, Depth):
        """Return the Engine Evaluate time of the position
        in nanoseconds"""

        # I don't want to see anything printed on the screen
        text_trap = io.StringIO()
        sys.stdout = text_trap

        # Count running time 
        StartTime = time.monotonic()
        self.findBestMove(ChessBoard, Depth)
        EndTime = time.monotonic()

        # now restore stdout function
        sys.stdout = sys.__stdout__

        return EndTime-StartTime


#class DeriveEngine(Engine):
#    def __init__(self):
#        printf("Powerful Engine!")
#
#    def NextBestMove(ChessBoard)
#        printf("BRMM BRMMM")
