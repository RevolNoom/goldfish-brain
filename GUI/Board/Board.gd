extends Node2D

signal MovePlayed(SelfBoard)

var _PositionStack = []

var _WhitePlayer
var _BlackPlayer

# Mapping between char and piece, used for initializing pieces
var _CharToPiece = {'k': preload("res://ChessPiece/Black/KingBlack.tscn"),
					'p': preload("res://ChessPiece/Black/PawnBlack.tscn"),
					'r': preload("res://ChessPiece/Black/RookBlack.tscn"),
					'q': preload("res://ChessPiece/Black/QueenBlack.tscn"),
					'n': preload("res://ChessPiece/Black/KnightBlack.tscn"),
					'b': preload("res://ChessPiece/Black/BishopBlack.tscn"),
					
					'K': preload("res://ChessPiece/White/KingWhite.tscn"),
					'P': preload("res://ChessPiece/White/PawnWhite.tscn"),
					'R': preload("res://ChessPiece/White/RookWhite.tscn"),
					'Q': preload("res://ChessPiece/White/QueenWhite.tscn"),
					'N': preload("res://ChessPiece/White/KnightWhite.tscn"),
					'B': preload("res://ChessPiece/White/BishopWhite.tscn")}
					
# From Fen string, load pieces to the board
# I hope this is pass-by-value. 
# It'll be a disaster when I swap sides and then these args turn out to be references
func SetPlayers(whitePlayer, blackPlayer):
	if _WhitePlayer != null:
		_WhitePlayer.disconnect("MoveConstructed", self, "PlayMove")
	if _BlackPlayer != null:
		_BlackPlayer.disconnect("MoveConstructed", self, "PlayMove")
	_WhitePlayer = whitePlayer
	_WhitePlayer.connect("MoveConstructed", self, "PlayMove")
	_BlackPlayer = blackPlayer
	_BlackPlayer.connect("MoveConstructed", self, "PlayMove")
	
	
# From Fen string, load pieces to the board
func LoadBoard(FEN):
	UpdateBoard(FEN)
	_PositionStack.clear()
	_PositionStack.append(FEN)

# TODO: I don't have time to verify FEN though. Use with risk
func UpdateBoard(FEN):
	#print("FEN: " + FEN)
	# Dust off every pieces on the board
	for eachCell in get_children():
		for eachPiece in eachCell.get_children():
			if eachPiece.get_class() == "ChessPiece":
				eachCell.remove_child(eachPiece) # Out of the board
				eachPiece.free() # and out of memory
			
	var Col = "abcdefgh"
	var colNo = 0
	var row = 8
	
	for i in FEN:
		if str(i).is_valid_integer():	# Batches of blank cells. Ignore them
			colNo += int(i)
			
		# Go down a row
		elif i == "/":	
			colNo = 0 
			row -= 1
			
		# We encounter a piece. Instance it and put it on the board
		elif i in "kprqnbKPRQNB": 
			var currentCell = Col[colNo] + str(row)
			var newPiece = _CharToPiece[i].instance()
			get_node(currentCell).add_child(newPiece)
			colNo += 1 # Don't forget to advance to next cell!
			
		# A blank space between board pieces and player's turn
		# is cue for us to leave 
		elif i == " ": 
			break
			
		# Wtf is this character?
		else:
			printerr("Erroneous character found when loading board from FEN: " + i)
			return ERR_BUG

func GetFEN():
	return _PositionStack.back()

# Add a new FEN position on the position stack
# Update the board position
func PlayMove(UCIstr):
	print ("Got move: "+ UCIstr)
	
	# Bye bye stubborn newline
	UCIstr = KillPreSufSpace(UCIstr)
	
	# VERIFY that this is a valid move
	var output = []
	# warning-ignore:return_value_discarded
	$Pychess.Execute("legalmoves", [self.GetFEN()], output)
	output = output[0].split("\n")
	print(output)
	
	# Make a move if the move is a valid one
	if UCIstr in output:
		# warning-ignore:return_value_discarded
		var NextPosition = []
		$Pychess.Execute("move", [self.GetFEN(), UCIstr], NextPosition)
		print("NextPosition: ")
		print(NextPosition)
		# Add new position's FEN to the stack
		print("Appended position: " + NextPosition[0])
		_PositionStack.append(NextPosition[0])
		
	else:
		printerr("Invalid Move: \"" + UCIstr + "\"")
	
	# And update the board, obviously
	# Let's do it the Lazy way
	# Because I dun't have time for memory optimization
	# Destroy the whole board and then create new pieces again
	UpdateBoard(_PositionStack.back())
	emit_signal("MovePlayed", self)
		
	
# Ask a Player for their move
func PromptMove():
	# Find out the player-to-move
	var SideToMove = _PositionStack.back().split(" ")[1] 
	
	print("Board: " + self.GetFEN())
	print("SideToMove: " + SideToMove)
	if SideToMove == "w":
		_WhitePlayer.HandleMoveRequest(self)
	else:
		_BlackPlayer.HandleMoveRequest(self)

# Return the cell name this Piece is in
# Empty string if this Piece is in a strange world
func GetCellOf(Piece):
	# Piece's parent should be a Cell
	var cell = Piece.get_parent()
	if cell != null:
		return cell.get_name()
	return ""
	
func Status():
	var output = []
	# warning-ignore:return_value_discarded
	$Pychess.Execute("status", [self.GetFEN()], output)
	return KillPreSufSpace(output[0])
		
# For some reasons, the UCIstr in PlayMove has a very stubborn newline
# I have to do the aggressive way to destroy it
# Remove all Prefix and Suffix space from ONE string
func KillPreSufSpace(string):
	print("Trimming: \"" + str(string) + "\"")
	var regex = RegEx.new()
	regex.compile("^\\s*(\\S+)\\s*$")
	return regex.search(string).get_string(1)
