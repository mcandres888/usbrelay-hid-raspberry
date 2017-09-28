# usbrelay-hid-raspberry


git clone this repository
run sudo sh install.sh

Usage:
  hidusb-relay-cmd on <num>  - turn relay <num> ON
  hidusb-relay-cmd off <num> - turn relay <num> OFF
  hidusb-relay-cmd state     - print states of the relays
  hidusb-relay-cmd enum      - print state of all found relay devices

Parameter ID=XXXXX selects one device if several are connected.
Example: sudo hidusb-relay-cmd ID=ABCDE ON 2
         sudo hidusb-relay-cmd on 1
         sudo hidusb-relay-cmd off 1



python usage:
from subprocess import call
command = "/usr/bin/hidusb-relay-cmd"
call([command, "on", "1"])

