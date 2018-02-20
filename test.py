import stbt
import keySend

rack = "A03"
slot = "1-16"


keySend.keyPressAPI(rack, "menu", slot)
stbt.wait_for_match('images/tvapps1.png')
print "test file executed"

