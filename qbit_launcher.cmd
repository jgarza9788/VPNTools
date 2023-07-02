:: wait 30 seconds
timeout 30

@echo off

set "targetProgram=nordvpn-service.exe"
set "launcherProgram=C:\Program Files\qBittorrent\qbittorrent.exe"

tasklist /fi "imagename eq nordvpn-service.exe" 2>NUL | find /i "nordvpn-service.exe" 

tasklist /fi "imagename eq %targetProgram%" 2>NUL | find /i "%targetProgram%" >NUL

if %errorlevel% equ 0 (
    echo Target program is already running.
    echo Launching the launcher program...
    start "" "%launcherProgram%"
) else (
    echo Target program is not running.
    echo Not launching the launcher program.
)
