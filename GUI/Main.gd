extends Node

# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var STARTING_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

# Called when the node enters the scene tree for the first time.
func _ready():
	$Board.LoadBoard(STARTING_FEN)
	$Board.SetPlayers($Human, $Pychess)
	$Board.connect("MovePlayed", self, "AMoveCompleted")
	
	# Start the game
	$Board.PromptMove()
	
func AMoveCompleted(Board):
	var status = Board.Status()
	# "-" means the game hasn't ended yet
	if status == "-":
		Board.PromptMove()
	else:
		print("Game ended: " + status)


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
