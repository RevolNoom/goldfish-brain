import time
import io
import sys

class Engine:
    def findBestMove(self, ChessBoard, Depth):
        print("zzz...")

    def GetEvaluateTime(self, ChessBoard, Depth):
        """Return (Position Evaluate time (s), Best Move)"""

        # I don't want to see anything printed on the screen
        text_trap = io.StringIO()
        sys.stdout = text_trap

        # Count running time 
        StartTime = time.time()
        Move = self.findBestMove(ChessBoard, Depth)
        EndTime = time.time()

        # now restore stdout function
        sys.stdout = sys.__stdout__

        return (EndTime-StartTime, Move)