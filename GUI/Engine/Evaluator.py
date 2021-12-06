#!/usr/bin/python3

# For testing purpose
# Tested with python-chess version 1.999
# https://github.com/niklasf/python-chess
import chess

# AVAILABLE EVALUATORS:
# +) EvaluatorSunfish
# +)


class Evaluator:
    def Evaluate(self, ChessBoard):
        print("I'm doing nothing! You asked the wrong guy to do your job.")


class EvaluatorSunfish(Evaluator):
    """ This evaluator uses piece-position values from Sunfish engine
        https://github.com/thomasahle/sunfish/blob/master/sunfish.py """

    _piece = { 'P': 100, 'N': 280, 'B': 320, 'R': 479, 'Q': 929, 'K': 60000, 
                'p': -100, 'n': -280, 'b': -320, 'r': -479, 'q': -929, 'k': -60000 }
    _pst = {
        'P': (   0,   0,   0,   0,   0,   0,   0,   0,
                78,  83,  86,  73, 102,  82,  85,  90,
                 7,  29,  21,  44,  40,  31,  44,   7,
               -17,  16,  -2,  15,  14,   0,  15, -13,
               -26,   3,  10,   9,   6,   1,   0, -23,
               -22,   9,   5, -11, -10,  -2,   3, -19,
               -31,   8,  -7, -37, -36, -14,   3, -31,
                 0,   0,   0,   0,   0,   0,   0,   0),
        'N': ( -66, -53, -75, -75, -10, -55, -58, -70,
                -3,  -6, 100, -36,   4,  62,  -4, -14,
                10,  67,   1,  74,  73,  27,  62,  -2,
                24,  24,  45,  37,  33,  41,  25,  17,
                -1,   5,  31,  21,  22,  35,   2,   0,
               -18,  10,  13,  22,  18,  15,  11, -14,
               -23, -15,   2,   0,   2,   0, -23, -20,
               -74, -23, -26, -24, -19, -35, -22, -69),
        'B': ( -59, -78, -82, -76, -23,-107, -37, -50,
               -11,  20,  35, -42, -39,  31,   2, -22,
                -9,  39, -32,  41,  52, -10,  28, -14,
                25,  17,  20,  34,  26,  25,  15,  10,
                13,  10,  17,  23,  17,  16,   0,   7,
                14,  25,  24,  15,   8,  25,  20,  15,
                19,  20,  11,   6,   7,   6,  20,  16,
                -7,   2, -15, -12, -14, -15, -10, -10),
        'R': (  35,  29,  33,   4,  37,  33,  56,  50,
                55,  29,  56,  67,  55,  62,  34,  60,
                19,  35,  28,  33,  45,  27,  25,  15,
                 0,   5,  16,  13,  18,  -4,  -9,  -6,
               -28, -35, -16, -21, -13, -29, -46, -30,
               -42, -28, -42, -25, -25, -35, -26, -46,
               -53, -38, -31, -26, -29, -43, -44, -53,
               -30, -24, -18,   5,  -2, -18, -31, -32),
        'Q': (   6,   1,  -8,-104,  69,  24,  88,  26,
                14,  32,  60, -10,  20,  76,  57,  24,
                -2,  43,  32,  60,  72,  63,  43,   2,
                 1, -16,  22,  17,  25,  20, -13,  -6,
               -14, -15,  -2,  -5,  -1, -10, -20, -22,
               -30,  -6, -13, -11, -16, -11, -16, -27,
               -36, -18,   0, -19, -15, -15, -21, -38,
               -39, -30, -31, -13, -31, -36, -34, -42),
        'K': (   4,  54,  47, -99, -99,  60,  83, -62,
               -32,  10,  55,  56,  56,  55,  10,   3,
               -62,  12, -57,  44, -67,  28,  37, -31,
               -55,  50,  11,  -4, -19,  13,   0, -49,
               -55, -43, -52, -28, -51, -47,  -8, -50,
               -47, -42, -43, -79, -64, -32, -29, -32,
                -4,   3, -14, -50, -57, -18,  13,   4,
                17,  30,  -3, -14,   6,  -1,  40,  18),


        # Procedurely flipped the valued vertically
        # And then hand-formatted
        # Yah, not right now. I need to finish Evaluate() first
        'k': ( -17,  -30,  3, 14, -6,  1,-40,-18,
                 4,   -3, 14, 50, 57, 18,-13, -4,  
                47,   42, 43, 79, 64, 32, 29, 32,
                55,   43, 52, 28, 51, 47,  8, 50,
                55,  -50,-11,  4, 19,-13,  0, 49,
                62,  -12, 57,-44, 67,-28,-37, 31,
                32,  -10,-55,-56,-56,-55,-10, -3,
                -4,  -54,  -47, 99, 99,-60,-83, 62),
        'q': (  39, 30, 31, 13, 31, 36, 34, 42,
                36, 18,   0, 19, 15, 15, 21, 38,
                30,  6, 13, 11, 16, 11, 16, 27,
                14, 15,  2,  5,  1, 10, 20, 22,
                -1, 16,  -22,  -17,  -25,  -20, 13,  6,
                 2,  -43,  -32,  -60,  -72,  -63,  -43,   -2,
               -14,  -32,  -60, 10,  -20,  -76,  -57,  -24,
                -6,   -1,  8,104,  -69,  -24,  -88,  -26),
        'r': (  30, 24, 18,   -5,  2, 18, 31, 32,
                53, 38, 31, 26, 29, 43, 44, 53,
                42, 28, 42, 25, 25, 35, 26, 46,
                28, 35, 16, 21, 13, 29, 46, 30,
                 0,   -5,  -16,  -13,  -18,  4,  9,  6,
                -19,  -35,  -28,  -33,  -45,  -27,  -25,  -15,
                -55,  -29,  -56,  -67,  -55,  -62,  -34,  -60,
                -35,  -29,  -33,   -4,  -37,  -33,  -56,  -50),
        'b': (      7,   -2, 15, 12, 14, 15, 10, 10,
                    -19,  -20,  -11,   -6,   -7,   -6,  -20,  -16,
                    -14,  -25,  -24,  -15,   -8,  -25,  -20,  -15,
                    -13,  -10,  -17,  -23,  -17,  -16,   0,   -7,
                    -25,  -17,  -20,  -34,  -26,  -25,  -15,  -10,
                    9,  -39, 32,  -41,  -52, 10,  -28, 14,
                   11,  -20,  -35, 42, 39,  -31,   -2, 22,
                    59, 78, 82, 76, 23,107, 37, 50),
        'n': (   74, 23, 26, 24, 19, 35, 22, 69,
               23, 15,   -2,   0,   -2,   0, 23, 20,
               18,  -10,  -13,  -22,  -18,  -15,  -11, 14,
                1,   -5,  -31,  -21,  -22,  -35,   -2,   0,
                -24,  -24,  -45,  -37,  -33,  -41,  -25,  -17,
                -10,  -67,   -1,  -74,  -73,  -27,  -62,  2,
                3,  6, -100, 36,   -4,  -62,  4, 14,
                 66, 53, 75, 75, 10, 55, 58, 70),

        'p': (     0,   0,   0,   0,   0,   0,   0,   0,
                   31,   -8,  7, 37, 36, 14,   -3, 31,
                   22,   -9,   -5, 11, 10,  2,   -3, 19, 
                   26,   -3,  -10,   -9,   -6,   -1,   0, 23,
                   17,  -16,  2,  -15,  -14,   0,  -15, 13,
                    -7,  -29,  -21,  -44,  -40,  -31,  -44,   -7,
                    -78,  -83,  -86,  -73, -102,  -82,  -85,  -90,
                    0,   0,   0,   0,   0,   0,   0,   0)
    }


    def Evaluate(self, ChessBoard):

        gameResult = ChessBoard.outcome()

        WIN_SCORE = 999999

        # The game ended
        if gameResult is not None:
            if gameResult.result() == "1-0":
                return WIN_SCORE

            elif gameResult.result() == "0-1":
                return -WIN_SCORE
                
            elif gameResult.result() == "1/2-1/2":
                return 0
        

        # Help keeping track of traversed position on the board
        Row = 0
        Column = 0

        score = 0

        fen = ChessBoard.board_fen()

        # Sum up the score of each piece on each cell 
        for i in range(0, len(fen)):
            if fen[i] == '/':
                Row += 1
                Column = 0
            elif fen[i].isnumeric():
                Column += int(fen[i])
            elif fen[i].isalpha():   
                positionScore = self._pst[fen[i]][Row*8 + Column]
                pieceScore = self._piece[fen[i]]
                score += pieceScore + positionScore
                #print("Piece " + fen[i] + " at " + str(Row) + ", " + str(Column) + " score: " + str(pieceScore))
                Column += 1
            else:   #We're out of board representation section. Time to depart
               break

        return score




# Minh's Evaluator
class EvaluatorPosition(Evaluator):
    """
    This evaluater uses self-built piece position value 
    and the difference of the number of pieces between 
    two player.
    """

    # Value of the position of each piece in the chess board
    _pawnTable = [ 0, 0, 0, 0, 0, 0, 0, 0,
                   5, 10, 10, -20, -20, 10, 10, 5,
                   5, -5, -10, 0, 0, -10, -5, 5,
                   0, 5, 10, 20, 20, 10, 5, 0,
                   5, 5, 10, 25, 25, 10, 5, 5,
                   10, 10, 20, 30, 30, 20, 10, 10,
                   50, 50, 50, 50, 50, 50, 50, 50,
                   90, 90, 90, 90, 90, 90, 90, 90 ]

    _knightsTable = [ -50, -40, -30, -30, -30, -30, -40, -50,
                      -40, -20, 0, 5, 5, 0, -20, -40,
                      -30, 5, 10, 15, 15, 10, 5, -30,
                      -30, 0, 15, 20, 20, 15, 0, -30,
                      -30, 5, 15, 20, 20, 15, 5, -30,
                      -30, 0, 10, 15, 15, 10, 0, -30,
                      -40, -20, 0, 0, 0, 0, -20, -40,
                      -50, -40, -30, -30, -30, -30, -40, -50 ]

    _bishopsTable = [ -20, -10, -10, -10, -10, -10, -10, -20,
                      -10, 10, 0, 0, 0, 0, 10, -10,                  
                      -15, 10, 10, 10, 10, 10, 10, -15,
                      -10, 0, 10, 10, 10, 10, 0, -10,
                      -10, 5, 5, 10, 10, 5, 5, -10,
                      -10, 0, 5, 10, 10, 5, 0, -10,
                      -10, 0, 0, 0, 0, 0, 0, -10,
                      -20, -10, -10, -10, -10, -10, -10, -20 ]

    _rooksTable = [ 0, 0, 0, 5, 5, 0, 0, 0,
                    -5, 0, 0, 0, 0, 0, 0, -5,
                    -5, 5, 5, 5, 5, 5, 5, -5,
                    -5,5, 5, 5, 5, 5, 5, -5,
                    -5, 5, 5, 5, 5, 5, 5, -5,
                    -5, 5, 5, 5, 5, 5, 5, -5,
                     5, 10, 10, 10, 10, 10, 10, 5,
                     5, 5, 0, 0, 0, 0, 5, 5]

    _queensTable = [ -20, -10, -10, -5, -5, -10, -10, -20,
                     -10, 0, 0, 0, 0, 0, 0, -10,
                     -10, 5, 5, 5, 5, 5, 0, -10,
                     0, 0, 5, 5, 5, 5, 0, -5,
                     -5, 0, 5, 5, 5, 5, 0, -5,
                     -10, 0, 5, 5, 5, 5, 0, -10,
                     -10, 0, 0, 0, 0, 0, 0, -10,
                     -20, -10, -10, -5, -5, -10, -10, -20]

    _kingsTable = [ 20, 30, 10, 0, 0, 10, 30, 20,
                    20, 20, 0, 0, 0, 0, 20, 20,
                   -10, -20, -20, -20, -20, -20, -20, -10,
                   -20, -30, -30, -40, -40, -30, -30, -20,
                   -30, -40, -40, -50, -50, -40, -40, -30,
                   -30, -40, -40, -50, -50, -40, -40, -30,
                   -30, -40, -40, -50, -50, -40, -40, -30,
                   -30, -40, -40, -50, -50, -40, -40, -30 ]
    
    def _materialPoint(self, chessBoard):
        """
        This function calculate the point of chessBoard from the difference of the number of piece between White and Black.
        """
        # Pawn difference = # of white pawns - # of black pawns
        pawnDiff = len(chessBoard.pieces(chess.PAWN, chess.WHITE)) - len(chessBoard.pieces(chess.PAWN, chess.BLACK))
        # Knight difference = # of white knight - # of black knight
        knightDiff = len(chessBoard.pieces(chess.KNIGHT, chess.WHITE)) - len(chessBoard.pieces(chess.KNIGHT, chess.BLACK))
        # Bishop difference = # of white bishop - # of black bishop
        bishopDiff = len(chessBoard.pieces(chess.BISHOP, chess.WHITE)) - len(chessBoard.pieces(chess.BISHOP, chess.BLACK))
        # Rook difference = # of white rook - # of black rook
        rookDiff = len(chessBoard.pieces(chess.ROOK, chess.WHITE)) - len(chessBoard.pieces(chess.ROOK, chess.BLACK))
        # Queen difference = # of white queen - # of black queen
        queenDiff = len(chessBoard.pieces(chess.QUEEN, chess.WHITE)) - len(chessBoard.pieces(chess.QUEEN, chess.BLACK))
        return 100*pawnDiff + 320*knightDiff + 330*bishopDiff + 500*rookDiff + 900*queenDiff

    def _positionPoint(self, chessBoard):
        """
        This function calculate the point of chessBoard from the position value of each piece in chess board.
        """
        # pawn_pos = pawn_white_point + pawn_black_point
        pawnPos = sum([self._pawnTable[i] for i in chessBoard.pieces(chess.PAWN, chess.WHITE)]) + sum([-self._pawnTable[chess.square_mirror(i)] for i in chessBoard.pieces(chess.PAWN, chess.BLACK)])
        # knight_pos = knight_white_point + knight_black_point
        knightPos = sum([self._knightsTable[i] for i in chessBoard.pieces(chess.KNIGHT, chess.WHITE)]) + sum([-self._knightsTable[chess.square_mirror(i)] for i in chessBoard.pieces(chess.KNIGHT, chess.BLACK)])
        # bishop_pos = bishop_white_point + bishop_black_point
        bishopPos = sum([self._bishopsTable[i] for i in chessBoard.pieces(chess.BISHOP, chess.WHITE)]) + sum([-self._bishopsTable[chess.square_mirror(i)] for i in chessBoard.pieces(chess.BISHOP, chess.BLACK)])
        # rook_pos = rook_white_point + rook_black_point
        rookPos = sum([self._rooksTable[i] for i in chessBoard.pieces(chess.ROOK, chess.WHITE)]) + sum([-self._rooksTable[chess.square_mirror(i)] for i in chessBoard.pieces(chess.ROOK, chess.BLACK)])
        # queen_pos = queen_white_point + queen_black_point
        queenPos = sum([self._queensTable[i] for i in chessBoard.pieces(chess.QUEEN, chess.WHITE)]) + sum([-self._queensTable[chess.square_mirror(i)] for i in chessBoard.pieces(chess.QUEEN, chess.BLACK)])
        # king_pos = king_white_point + king_black_point
        kingPos = sum([self._kingsTable[i] for i in chessBoard.pieces(chess.KING, chess.WHITE)]) + sum([-self._kingsTable[chess.square_mirror(i)] for i in chessBoard.pieces(chess.KING, chess.BLACK)])
        return pawnPos + knightPos + bishopPos + rookPos + queenPos + kingPos

    def Evaluate(self, chessBoard):
        gameResult = chessBoard.outcome()

        WIN_SCORE = 999999

        # The game ended
        if gameResult is not None:
            if gameResult.result() == "1-0":
                return WIN_SCORE

            elif gameResult.result() == "0-1":
                return -WIN_SCORE
                
            elif gameResult.result() == "1/2-1/2":
                return 0

        return self._materialPoint(chessBoard) + self._positionPoint(chessBoard)

