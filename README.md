openhab
=======

All the configuration and sitemap files for the openhab will be here. 
Clone this repository to the runtime directory of openhab.

```bash
cd runtime
git clone https://github.com/shivukumar/openhab.git .
```


Running the openhab_gpio.py script
----------------------------------

```bash
sudo python openhab_gpio.py --pin=<pin number as per GPIO.BOARD mode> --set=<ON/OFF>
```

Running openhab server

```bash
cd runtime
sudo bash
sh start.sh
```
