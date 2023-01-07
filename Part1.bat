@echo off
cd /D "%~dp0"
ssh -o StrictHostKeyChecking=no admin@192.168.88.1 /interface bridge port remove numbers=0,1,2,4
ssh admin@192.168.88.1 /interface bridge add comment=MikroBrick name=bridgeLAN
ssh admin@192.168.88.1 /interface bridge port add comment=MikroBrick bridge=bridgeLAN interface=ether2
ssh admin@192.168.88.1 /interface bridge port add comment=MikroBrick bridge=bridgeLAN interface=ether3
ssh admin@192.168.88.1 /interface bridge port add comment=MikroBrick bridge=bridgeLAN interface=ether4
ssh admin@192.168.88.1 /ip dhcp-server network add comment=MikroBrick address=192.168.1.0/24 gateway=192.168.1.1
ssh admin@192.168.88.1 /ip pool add comment=MikroBrick name=dhcp_pool1 ranges=192.168.1.2-192.168.1.254
ssh admin@192.168.88.1 /ip dhcp-server add address-pool=dhcp_pool1 disabled=no interface=bridgeLAN name=dhcpLAN
ssh admin@192.168.88.1 /ip address add comment=MikroBrick address=192.168.1.1/24 interface=bridgeLAN network=192.168.1.0
ssh admin@192.168.88.1 /ip firewall nat add comment=MikroBrick action=masquerade chain=srcnat out-interface=ether1
ssh admin@192.168.88.1 /interface list member add comment=MikroBrick interface=bridgeLAN list=LAN
exit /B