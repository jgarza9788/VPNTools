VPNTools **OBSOLITE**
---
just some scripts i use to manage my VPN  (NordVPN)


# **THIS IS OBSOLITE**
this tool is no longer being used by it's author.  



<!--TOC-->
<!--TOC-->


# install requirements
```
pip install requirements.txt
```
>note NordVPN and OpenVPN are required

# VPN.py
## main()
this function will activate or deactivate the VPN
> please read the script

## config.zip
contains the config files from `C:\Program Files\OpenVPN\config`

# FAQs
1. if it doesn't look right.
termcolor and/or nerdfonts might not work with your terminal


## Files
### templates
contains templates that OpenVPN will use to close and open programs based on the VPN status
### utilities
contains bar.py ... for the cool looking bar
### output
contains the output files from running the `server_files.py` script
### .gitattributes
git stuff
### .gitignore
git stuff
### activate_VPN.cmd
will turn on the VPN
### config.zip 
is missing, since those are the openVPN scripts that will be unique to your PC.
### kill_VPN.cmd
this will kill the VPN
### OpenVPN-Config.lnk
this should be a link to your openVPN configuration files
### ping_VPN.cmd
this will ping your VPN servers
### README.md
that is this file
### requirements.txt
this is the requirements file for python
### results.log
will those you the ping history 
### Server recommended by NordVPN - NordVPN.url
link to the VPN website
### server_files.py
will customize the server files based on the ones you downloed and place them in root/output/ folder
### VPN_Term_App.cmd
will open a terminal app
### VPN_Term_App.py
you can launch this of the terminal app also
### VPN.py
this is your main file with all the goodies



