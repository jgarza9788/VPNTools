
:: set up for color text
@echo off
cls && color 08
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (set "DEL=%%a")
<nul set /p=""
::

:: killing programs
call :ColorText 04 "kill programs"
echo. 


taskkill /IM openvpn-gui.exe /f
call :ColorText 04 "X openvpn-gui.exe"
echo. &
taskkill /IM openvpn.exe /f
call :ColorText 04 "X openvpn.exe"
echo. &
taskkill /IM openvpnserv.exe /f
call :ColorText 04 "X openvpnserv.exe"
echo. &
taskkill /IM qbittorrent.exe /f
call :ColorText 04 "X qbittorrent.exe"
echo. &

::

call :ColorText 07 "10s timer"
timeout 10


call :ColorText 02 "Finding a VPN Connection"
set VPN=us8479
set Result=1000

::ECHO OFF
:: https://nordvpn.com/servers/tools/
::INSERT
CALL :TestVPN us8479
CALL :TestVPN us8494
CALL :TestVPN us8495
CALL :TestVPN us9618
CALL :TestVPN us9612
CALL :TestVPN us9616
CALL :TestVPN us8482


:: ECHO ON

echo VPN=%VPN% Result=%Result%

set this_date=%date%
set this_time=%time%
set type=udp

echo %this_date%,%this_time%,%VPN%.nordvpn.com.%type%.ovpn,%Result%>> results.log

taskkill /IM openvpn-gui.exe /f
taskkill /IM openvpn.exe /f
taskkill /IM openvpnserv.exe /f
timeout 0
"C:\Program Files\OpenVPN\bin\openvpn-gui.exe" --connect %VPN%.nordvpn.com.udp.ovpn



goto:eof


:TestVPN

FOR /F "delims=" %%G in ('ping -n 1 "%~1".nordvpn.com ^| find "Reply"') DO SET pingreply=%%G
for /f "tokens=5 delims= " %%a in ("%pingreply%") do ( set pingTime=%%a )       

SET pingTime=%pingTime:time=%
SET pingTime=%pingTime:~1,-1%
SET pingTime=%pingTime:ms=%

IF %Result% GTR %pingTime% set VPN=%~1%
IF %Result% GTR %pingTime% set Result=%pingTime%

ECHO server="%~1" time=%pingTime% 


goto:eof


:ColorText
:: example of syntax
:: call :ColorText 01 "blue"
:: call :ColorText 02 "green"
:: call :ColorText 03 "cyan"
:: call :ColorText 04 "red"
:: call :ColorText 05 "magenta"
:: call :ColorText 06 "yellow"
:: call :ColorText 07 "white"
:: call :ColorText 08 "grey"


<nul set /p "=%DEL%" > "%~2"
findstr /v /a:%1 /R "+" "%~2" nul
del "%~2" > nul
goto :eof

@REM pause