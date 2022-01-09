extends Node

signal MoveConstructed(UCIMove)
# Called when the node enters the scene tree for the first time.

var _python

func _ready():
	if OS.get_name() == "Windows":
		_python = "python"
	else:
		if OS.get_name() != "X11":
			printerr("Your host hasn't been tested for compatibility yet.")
		_python = "python3"

func HandleMoveRequest(Board):
	var output = []
	
	# Hard-coded linkage between nodes:
	# Will probably be problematic in the future
	var algorithmName = get_node("../../HBoxContainer/AlgorithmOptions/AlgorithmSelection")._algorithmPicked
	var depth = get_node("../../HBoxContainer/AlgorithmOptions/HBoxContainer/DepthEdit")._depth
	
	print("Algorithm: " + algorithmName + ". Depth: " + str(depth))
# warning-ignore:return_value_discarded
	OS.execute(_python, ["./Engine/pychess.py", "bestmove", Board.GetFEN(), algorithmName, depth], true, output)
	
	emit_signal("MoveConstructed", output[0])

# commandName: A command pychess.py can understand
# argv: An array of arguments to pass to pychess
# output: your array to store what pychess has to offer
func Execute(commandName, argv, output):
	var ARGV = ["./Engine/pychess.py", commandName]
	ARGV.append_array(argv)
	OS.execute(_python, ARGV, true, output)
