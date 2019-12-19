# RPI Hotspot with Mavlink Router Config

Hotspot Wifi and Route mavlink packets between endpoints.

Usage:  
Due to some of the dependencies not getting installed using sudo command, switch the user to root using sudo su  

wget https://raw.githubusercontent.com/lordcast/rpi_hotspot_mavlink/master/Rpihotspot_buster  
sudo chmod +x Rpihotspot_buster  
sudo ./Rpihotspot_buster

Next you have change the Raspberry Pi configuraation if you are using GPIO for telementry connection, else ignore this and just run the find_port.py file to get the port aurdopoilot connected to.  
  
sudo raspi-config  
select interface options > serial > select no > select yes > finish  
sudo reboot  

run the find_port.py which will provid the port which has to be update in main.conf file under URAT > Device



