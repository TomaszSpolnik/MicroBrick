@echo off
cd /D "%~dp0"
ssh -o StrictHostKeyChecking=no admin@192.168.1.1 /interface bridge port add comment=MikroBrick bridge=bridgeLAN interface=wlan1
ssh admin@192.168.1.1 /interface wireless set wlan1 ssid=MikroTik frequency=2442 mode=ap-bridge disabled=no
ssh admin@192.168.1.1 /interface wireless security-profiles add comment=MikroBrick authentication-types=wpa2-psk mode=dynamic-keys name=WLANClient wpa2-pre-shared-key=[/system routerboard get serial-number]
ssh admin@192.168.1.1 /interface wireless set wlan1 security-profile=WLANClient
exit /B