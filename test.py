import stbt
import keySend
import time

rack = "A03"
slot = "1-16"

def main():
	keySend.keyPressAPI(rack, "exit", slot)
	time.sleep(1)
	# tune to sports mix
	keySend.tune("205", rack, slot)

	# verify snipe red button
	stbt.wait_for_match('images/red_button.png')

	# verify blue cells
	verify_cell_highlight()

	# verify higlights can navigate to all cells
	keySend.keyPressAPI(rack, "rightArrow", slot)

	# open app
	keySend.keyPressAPI(rack, "red", slot)

	keySend.keyPressAPI(rack, "downArrow", slot)
	stbt.wait_for_match('images/scoreguide_highlight.png')
	print "test file executed"


def verify_cell_highlight():
	stbt.wait_for_match('images/blue_cell_vertical.png')
	stbt.wait_for_match('images/blue_cell_horizontal.png')
	print "blue cells detected"

if __name__ == '__main__':
	main()
