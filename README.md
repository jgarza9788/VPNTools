 VPNTools
---
just some scripts i use to manage my VPN 

<!--TOC-->
- [VPNTools](#vpntools)
- [Files](#files)
    - [templates](#templates)
    - [.gitattributes](#gitattributes)
    - [.gitignore](#gitignore)
    - [findVPNServer.bat](#findvpnserverbat)
    - [findVPNServerWT.cmd](#findvpnserverwtcmd)
    - [killVPNandQBit.bat](#killvpnandqbitbat)
    - [killVPNandQBit_withToast.ps1](#killvpnandqbit_withtoastps1)
    - [OpenVPN-Config.lnk](#openvpn-configlnk)
    - [output](#output)
    - [README.md](#readmemd)
    - [results.log](#resultslog)
    - [Server recommended by NordVPN - NordVPN.url](#server-recommended-by-nordvpn---nordvpnurl)
    - [server_files.py](#server_filespy)
    - [wt_launcher.cmd](#wt_launchercmd)
<!--TOC-->

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


