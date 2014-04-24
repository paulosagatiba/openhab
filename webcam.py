import sys
import os
from optparse import OptionParser

def main():
	usage = "python %prog --start [--stop]"
	parser = OptionParser(usage)

	parser.add_option("--start",
					action = "store_true",
					default = False,
					dest = "start",
					help = "Start webcam"
			)


	parser.add_option("--stop",
					action = "store_true",
					default = False,
					dest = "stop",
					help = "Stop webcam"
			)

	(option, args) = parser.parse_args()

	if(option.start):
		os.system("raspistill --nopreview -w 640 -h 480 -q 5 -o /home/pi/stream/pic.jpg -tl 100 -t 9999999 -th 0:0:0 > /dev/null  2>&1 &")
		os.system("mjpg_streamer -i \"input_file.so -f /home/pi/stream -n pic.jpg\" -o \"output_http.so -w /usr/local/www -p 8090\"  &")
	elif(option.stop):
		os.system("pgrep raspistill | xargs kill ")
		os.system("pgrep mjpg_streamer | xargs kill ")
	else:
		parser.error("Specify start or stop option")

if __name__ == "__main__":
	main()
