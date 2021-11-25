extends Node

var _BoardNeedsService
var _IsDraggingPiece
var _PickedPiece
var _HoveredPiece
var _HoveredCell
var _IsOurTurn

signal MoveConstructed(UCIMove)

func _ready():
	_BoardNeedsService = null
	_IsDraggingPiece = false
	_PickedPiece = null
	_HoveredPiece = null
	_IsOurTurn = false
	
func HandleMoveRequest(Board):
	_BoardNeedsService = Board
	_IsDraggingPiece = false
	_PickedPiece = null
	_IsOurTurn = true
	
	
	
# Handle pieces drag and drop
func _unhandled_input(event):
	
	# Filter Mouse events only
	if not event is InputEventMouse:
		return
	
	# Move the Pointer along with Mouse
	# And take note of the hovered piece
	if event is InputEventMouseMotion:
		var collideInfo = $Handpick.move_and_collide($Handpick.get_global_mouse_position() - $Handpick.get_position(), true, true, true)
		if collideInfo != null and collideInfo.get_collider() != null:
			_HoveredPiece = collideInfo.get_collider()
			#print("Hovered piece: " + _HoveredPiece.get_parent().get_name())
		$Handpick.set_global_position($Handpick.get_global_mouse_position())
			
		# Move the dragged piece with the mouse
		if _PickedPiece != null:
			print("Picked piece: " + _PickedPiece.get_name())
			_PickedPiece.add_collision_exception_with($Handpick)
			# Test collision with a Cell
			var colInfo = _PickedPiece.move_and_collide(Vector2(0,0.1), true, true, true)
			# Take note about where we are hovering this PickedPiece
			# Could be over a Cell, could be nothing (null)
			if colInfo != null:
				_HoveredCell = colInfo.get_collider()
				print("Collided with: "+_HoveredCell.get_name())
			# Move the piece along with our mouse
			_PickedPiece.set_global_position($Handpick.get_global_position())
	
	if not _IsOurTurn:
		return
		
	# Are we pressing?
	if event is InputEventMouseButton:
		
		# We're clicking for the first time in a while
		# Try grabbing a chess piece
		if event.is_pressed():
			if _PickedPiece == null:
				_PickedPiece = _HoveredPiece
				print("Picked piece: " + _PickedPiece.get_name())
				
		# Drop piece on a cell
		elif _PickedPiece != null:
			# Woooo hooo: The piece lands on a cell. Return the move in UCI
			if _HoveredCell != null:
				_IsOurTurn = false
				emit_signal("MoveConstructed",  _BoardNeedsService.GetCellOf(_PickedPiece) + _HoveredCell.get_name())
			
			# Drop the piece off our hand
			_PickedPiece = null
