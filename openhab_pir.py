import RPi.GPIO as GPIO

def print_detect(channel):
	f = open("pir_count.txt", "r")
	count = f.read()
	count = int(count)
	count  += 1
	print "PIR trigger detected count = " + str(count)
	f.close()
	f = open("pir_count.txt", "w")
	f.write(str(count))
	f.close()


def main():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11, GPIO.IN)
	GPIO.add_event_detect(11, GPIO.RISING, callback=print_detect, bouncetime=300)


if __name__ == "__main__":
	f = open("pir_count.txt", "w")
	f.write("0")
	f.close()
	main()
	while(True):
		pass
