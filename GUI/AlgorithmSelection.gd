extends OptionButton

var _algorithmPicked

var Index_Name_Lookup = {}

# Called when the node enters the scene tree for the first time.
func _ready():
	AddItem("minimax")
	AddItem("negamax")
	AddItem("alphabeta")
	AddItem("nullmove")
	AddItem("quiescent")
	
	# Choose a default algorithm
	_on_AlgorithmSelection_item_selected(2)

func AddItem(AlgorithmName):
	Index_Name_Lookup[get_item_count()] = AlgorithmName
	add_item(AlgorithmName)

func _on_AlgorithmSelection_item_selected(index):
	_algorithmPicked = Index_Name_Lookup[index]
	self.selected = index
	self.text = _algorithmPicked
