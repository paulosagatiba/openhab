Internet of Things: Smart Home
===============================

This project aims to build a smart extensible home automation system based on IoT concept. Traditional smart home systems which do not use IoT are limited by various factors including range, extensibility, ease of used and integration. In our project have solved these issues by using IoT concepts. Our application also provides additional features like realtime surveillance and infotaninmet.

1) Used linux based Development board (RaspberryPi)

2) Smart Home features: Realtime Video Surivellance, Motion detector, Power Button Control, Temperature Monitoring, Fire alaram (direct call to phone), Infotainment (Audio playback control)

2) IOS, Android and Web based UI for control 

![Smart Home Sample UI] (http://www.openhab.org/images/ui/classicui.png)

3) Extensible UI from [OpenHAB] (http://www.openhab.org)


Cloning the repository
--------------------------

All the configuration and sitemap files for the openhab will be here. 
Clone this repository to the runtime directory of openhab.

```bash
cd runtime
git clone https://github.com/shivukumar/openhab.git .
```

Running openhab server
----------------------
```bash
cd runtime
sudo bash
sh start.sh
```
