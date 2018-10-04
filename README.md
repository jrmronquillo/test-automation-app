# test-automation-app

This is an automated test script that executes a set of commands while looking for the expected predefined result. If an unexpected result appears, the script reports the defect.

1. User Starts Script
2. Server sends command to device
3. Server Observes Output of Device
4. Server compares video output to a predefined screenshot
5. If Server finds a match, move on to the next script step
6. If Server does not find a match within 10 seconds, stop script and report.

* ## Installation
Install stb-tester on Ubuntu Server
```
sudo apt-get install stb-tester

```
API Reference: <https://stb-tester.com/manual-stb-tester-one/python-api> 

Clone or Download test-automation-app project to Ubuntu Server.
Change directory into test-automation-app project.
```
cd test-automation-app
```

* ## Usage
Start Script
```
python Scoreguide/test.py
```
Server should execute the predefined script steps. See example below where the script sends a command and looks for the result.
```
def main():
	keySend.keyPressAPI(rack, "exit", slot)

	# verify snipe red button
	stbt.wait_for_match('images/red_button.png')

```
