import stbt
import keySend
import time

rack = "A03"
slot = "1-16"

# tune api test
# keySend.tune("500", rack, slot)

keySend.keyPressAPI(rack, "exit", slot)
time.sleep(1)
# tune to sports mix
keySend.tune("205", rack, slot)
# open app
keySend.keyPressAPI(rack, "red", slot)

keySend.keyPressAPI(rack, "downArrow", slot)
stbt.wait_for_match('images/scoreguide_highlight.png')
print "test file executed"


