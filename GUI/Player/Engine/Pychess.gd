extends Node

signal MoveConstructed(UCIMove)
# Called when the node enters the scene tree for the first time.

var _python

func _ready():
	_python = "python3"
	if OS.get_name() == "Windows":
		_python = "python"

func HandleMoveRequest(Board):
	var output = []
	
	# Hard-coded linkage between nodes:
	# Will probably be problematic in the future
	var algorithmName = get_node("../HBoxContainer/AlgorithmOptions/AlgorithmSelection")._algorithmPicked
	var depth = get_node("../HBoxContainer/AlgorithmOptions/HBoxContainer/DepthEdit")._depth
	
	print("Algorithm: " + algorithmName + ". Depth: " + str(depth))
# warning-ignore:return_value_discarded
	OS.execute(_python, ["./Engine/pychess.py", "bestmove", Board.GetFEN(), algorithmName, depth], true, output)
	
	emit_signal("MoveConstructed", output[0])

