extends LineEdit

var _depth = 1


func _on_DepthEdit_text_changed(new_text):
	if int(new_text) == 0:
		self.text = str(_depth)
		return
		
	_depth = int(new_text)


func _on_DepthEdit_text_entered(new_text):
	_on_DepthEdit_text_changed(new_text)
