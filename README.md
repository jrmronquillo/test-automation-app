# test-automation-app


This is an automated test script designed to assist in software testing.

1. User Starts Script
2. Server sends command to device
3. Server observes video output of device.
4. Server compares video output to a predefined image that represents a passing test
5. If Server finds a match, the script moves on to the next script step
6. If Server does not find a match within 10 seconds, the script stops and reports test failure.

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
stbt run Scoreguide/test.py
```
Server should execute the predefined script steps. See example below where the script sends a command and looks for the result.
```
def main():
	keySend.keyPressAPI(rack, "exit", slot)

	# verify snipe red button
	stbt.wait_for_match('images/red_button.png')

```
* ## Additional Notes
This codebase contains more complex experimentations of the test script API bundled into python functions.
