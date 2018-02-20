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

	# verify highlights can navigate to all cells
	keySend.keyPressAPI(rack, "rightArrow", slot)
	verify_cell_highlight()
	keySend.keyPressAPI(rack, "rightArrow", slot)
	verify_cell_highlight()
	keySend.keyPressAPI(rack, "downArrow", slot)
	verify_cell_highlight()
	keySend.keyPressAPI(rack, "leftArrow", slot)
	verify_cell_highlight()
	keySend.keyPressAPI(rack, "leftArrow", slot)
	verify_cell_highlight()
	keySend.keyPressAPI(rack, "upArrow", slot)
	
	# verify app transitions to channel when press select
	# beware of possible false positive if info banner for 205 shows up
	# first cell
	keySend.keyPressAPI(rack, "select", slot)
	verify_channel_tune()

	# second cell
	keySend.keyPressAPI(rack, "rightArrow", slot)
	keySend.keyPressAPI(rack, "select", slot)
	verify_channel_tune()
	
	# return to mix channel
	keySend.tune("205", rack, slot)
	
	# open app
	keySend.keyPressAPI(rack, "red", slot)

	keySend.keyPressAPI(rack, "downArrow", slot)
	stbt.wait_for_match('images/scoreguide_highlight.png')
	print "test file executed"


def verify_cell_highlight():
	stbt.wait_for_match('images/blue_cell_vertical.png')
	stbt.wait_for_match('images/blue_cell_horizontal.png')
	print "blue cells detected"

def verify_channel_tune():
	# note: this only check if the info banner was detected, it does not validate the specific channel it was tuned to
	stbt.wait_for_match('images/info_banner_corner.png')
        keySend.keyPressAPI(rack, "prev", slot)
        time.sleep(6)
	

if __name__ == '__main__':
	main()
