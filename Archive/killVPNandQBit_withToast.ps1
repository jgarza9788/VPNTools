
taskkill /IM openvpn-gui.exe /f
taskkill /IM openvpn.exe /f
taskkill /IM openvpnserv.exe /f
taskkill /IM qbittorrent.exe /f

[void] [System.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms")

$objNotifyIcon = New-Object System.Windows.Forms.NotifyIcon
while($True)
{
$objNotifyIcon.Icon = [System.Drawing.SystemIcons]::Information
$objNotifyIcon.BalloonTipIcon = "Info" 
$objNotifyIcon.BalloonTipTitle = "killed VPN and Qbit" 
$objNotifyIcon.BalloonTipText = "killed VPN and Qbit"
$objNotifyIcon.Visible = $True 
$objNotifyIcon.ShowBalloonTip(10000)
Start-Sleep 500
}