#!/usr/bin/python
import sys
from optparse  import OptionParser
from datetime import datetime
import time


def main():
	usage = "python %prog --pin <pin-num as per GPIO.BOARD mode> --set <ON/OFF>"
	parser = OptionParser(usage)

	parser.add_option("--pin", "-p",
			dest = "pin",
			action = "store",
			default = -1,
			type = "int",
			help = "Specify pin number as per GPIO.BOARD mode"
			)


	parser.add_option("--set", "-s",
			dest = "set",
			action = "store",
			default = "",
			help = "Specify pin state ON/OFF"
			)

	parser.add_option("--test", "-t",
			dest = "test_mode",
			action = "store_true",
			default = False,
			help = "In test mode"
			)

	parser.add_option("--log", "-l",
			dest = "log_file",
			action = "store",
			default = "",
			help = "Log file, default is stdout"
			)
	(option, args) = parser.parse_args()

	if(option.pin == -1):
		parser.error("Specify the pin number")
	elif(option.set == ""):
		parser.error("Specify the pin state")

	test_mode = False
	if(option.test_mode):
		test_mode = True

	log_file = sys.stdout
	if(option.log_file != ""):
		log_file = open(option.log_file, "a")

	log_file.write(datetime.strftime(datetime.now(), "%d/%m/%Y %r: ") + "Setting PIN no " + str(option.pin) + " to " + option.set  + " state\n")

	if(not test_mode):
		import RPi.GPIO as GPIO
		GPIO.setwarnings(False)
		state = GPIO.HIGH
		if(option.set == "OFF"):
			state = GPIO.LOW
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(option.pin, GPIO.OUT)
		GPIO.output(option.pin, state)
#GPIO.cleanup()

	if(log_file != sys.stdout):
		log_file.close()

if __name__ == "__main__":
	main()

