# you can use subprocess to exec commands
from subprocess import call
command = "/usr/bin/hidusb-relay-cmd"
call([command, "on", "1"])

