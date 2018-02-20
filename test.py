import stbt
import keySend
import time

rack = "A03"
slot = "1-16"

# tune api test
# keySend.tune("500", rack, slot)

keySend.keyPressAPI(rack, "exit", slot)
time.sleep(1)
keySend.tune("205", rack, slot)
keySend.keyPressAPI(rack, "red", slot)
stbt.wait_for_match('images/tvapps1.png')
print "test file executed"


