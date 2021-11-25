extends Node

export var AlgorithmName = ""
export var Depth = 1

signal MoveConstructed(UCIMove)
# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


func HandleMoveRequest(Board):
	var output = []
# warning-ignore:return_value_discarded
	OS.execute("python3", ["./Engine/pychess.py", "bestmove", Board.GetFEN(), AlgorithmName, Depth], true, output)
	
	emit_signal("MoveConstructed", output[0])
