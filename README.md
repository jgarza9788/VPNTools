VPNTools
---
just some scripts i use to manage my VPN  

<!--TOC-->
<!--TOC-->

# versions
* [current Python version](https://github.com/jgarza9788/VPNTools)
* [batch/cmd](https://github.com/jgarza9788/VPNTools/tree/e203c2e575159864e16a711ee72c2e0c78aeefec)

# install requirements
```
pip install requirements.txt
```

# VPN.py
## main()
this function will activate or deactivate the VPN

## kill_vpn()
this will disconnect the VPN

## activate_vpn()
this will enable the VPN
1. kill
2. wait 
3. ping nordVPN servers 
4. connect to the fastest one

## config.zip
contains the config files from `C:\Program Files\OpenVPN\config`

# FAQs
1. if it doesn't look right.
termcolor and/or nerdfonts might not work with your terminal


## Files
### templates
contains templates that OpenVPN will use to close and open programs based on the VPN status
### .gitattributes
git stuff
### .gitignore
git stuff
### findVPNServer.bat
kills OpenVPN and tests servers and picks the lowest ping to reconnected to.
### findVPNServerWT.cmd
same as `findVPNServer.bat`, but opens in windows terminal
### killVPNandQBit.bat
kills VPN and QBittorrent 
### killVPNandQBit_withToast.ps1
same as killVPNandQBit.bat, but runs with powershell and displays a notification
### OpenVPN-Config.lnk
opens a link to where the config files are stored (locally)
### output
contains the output files from running the `server_files.py` script
### README.md
this file...silly goose
### results.log
logs when `findVPNServer.bat` is ran. (i.e. date,time. what VPN, and pingtime)
### Server recommended by NordVPN - NordVPN.url
link to nord's website
download the "OpenVPN UDP" one
### server_files.py
this will take the files i download from the nordVPN website and edit them and place them in the output folder
### wt_launcher.cmd
this will launch `findVPNServer.bat` in windows terminal


