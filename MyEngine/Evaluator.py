import chess

class Evaluator:
    def evaluatePoint(self, chessBoard):
        pass

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

    def evaluatePoint(self, chessBoard):
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

