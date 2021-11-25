extends KinematicBody2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"

# I can't believe I have to resolve to string comparison
# for type checking
func get_class():
	return "ChessPiece"

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
