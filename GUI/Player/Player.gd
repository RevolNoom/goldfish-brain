# PLAYER INTERFACE
# Defines how a player (Human or engine or alien or zombie or vampire or...)
# will make their move
extends Node

# warning-ignore:unused_signal
signal MoveConstructed(UCIMove)

# OVERRIDE ME!
func HandleMoveRequest(_Board):
	pass
