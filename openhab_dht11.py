import re
import os



def main():
    #os.system("./dht_program_name  > dht11.txt")
    f = open("dht11.txt")
    text = f.read()
    f.close()
    temp_hum_regex = re.compile(r"^Temp\s*=\s*(\d+).*Hum\s*=\s*(\d+)", re.M)
    value = temp_hum_regex.findall(text)[0]
    f = open("temperature.txt", "w")
    f.write(value[0])
    f.close()
    f = open("humidity.txt", "w")
    f.write(value[1])
    f.close()


if __name__ == "__main__":
    main()
