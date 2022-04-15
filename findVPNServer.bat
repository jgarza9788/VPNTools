
taskkill /IM openvpn-gui.exe /f
taskkill /IM openvpn.exe /f
taskkill /IM openvpnserv.exe /f

timeout 10

set VPN=us5861
set Result=1000

ECHO OFF
:: https://nordvpn.com/servers/tools/
::INSERT
:: CALL :TestVPN us4097
:: CALL :TestVPN us4571
:: CALL :TestVPN us4568
:: CALL :TestVPN us2892
:: CALL :TestVPN us3867
:: CALL :TestVPN us2967
:: CALL :TestVPN us3870
:: CALL :TestVPN us4543
:: CALL :TestVPN us4565
:: CALL :TestVPN us6754
:: CALL :TestVPN us8631
:: CALL :TestVPN us5577
CALL :TestVPN us5390
CALL :TestVPN us5861
CALL :TestVPN us5114
CALL :TestVPN us5850
CALL :TestVPN us5851
CALL :TestVPN us6757
CALL :TestVPN us6751
CALL :TestVPN us6752
CALL :TestVPN us8564
CALL :TestVPN us9402
CALL :TestVPN us8635
CALL :TestVPN us5729
CALL :TestVPN us8603
CALL :TestVPN us9409


ECHO ON


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
REM ECHO %pingreply%

for /f "tokens=5 delims= " %%a in ("%pingreply%") do ( set pingTime=%%a )       

SET pingTime=%pingTime:time=%
SET pingTime=%pingTime:~1,-1%
SET pingTime=%pingTime:ms=%

IF %Result% GTR %pingTime% set VPN=%~1%
IF %Result% GTR %pingTime% set Result=%pingTime%

ECHO server="%~1" time=%pingTime% 


goto:eof


