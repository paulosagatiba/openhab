import RPi.GPIO as GPIO

def print_detect(channel):
	global count
	count += 1
	print "PIR trigger detected"


def main():
	
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11, GPIO.IN)
	GPIO.add_event_detect(11, GPIO.RISING, callback=print_detect, bouncetime=300)
		

if __name__ == "__main__":
	global count
	count = 0
	main()
	while(count < 5):
		pass
	
	GPIO.cleanup()

