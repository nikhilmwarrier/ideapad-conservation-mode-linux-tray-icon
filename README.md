# Battery Conservation Mode tray icon for Lenovo Ideapad / V14 / V15 laptops running Linux

Tested on:
- Lenovo V15 Gen 2 running Fedora 36 KDE Plasma Spin
- Ideapad Gaming 3 running Kali Linux  
  
(This should work on most Ideapads and V14/V15 laptops.)
  
"Conservation Mode" is a feature in some Lenovo laptops which keeps the battery
at around 60% charge while running on AC. This supposedly slows down the
degradation of the battery in the long run.
  
This mode can be toggled by using the Lenovo Vantage app, which is not available
for Linux. 
  
I recently discovered that this mode can also be toggled by modifying the file
at `/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode`. This
script provides a simple graphical interface to handle this using a system tray
icon. 

## How to use:

1. Clone this repo    
```bash  
$ git clone 'https://github.com/nikhilmwarrier/ideapad-conservation-mode-linux-tray-icon' conservation-mode-tray-icon && cd conservation-mode-tray-icon
```  

2. Install dependencies   
```bash  
$ pip install -r ./requirements.txt
```
  
3. Make the script executable and run it  
```bash  
$ sudo chmod +x ./tray.py
$ ./tray.py
```  
  
It is recommended to add this script to your list of autostart programs.

Icon credits: [Papirus Icon Theme](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme/)
