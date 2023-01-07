@echo off
cd /D "%~dp0"
ssh -o StrictHostKeyChecking=no admin@192.168.1.1 /interface bridge port remove numbers=0
ssh admin@192.168.1.1 /interface bridge port add comment=MikroBrick bridge=bridgeLAN interface=ether5
ssh admin@192.168.1.1 /ip address remove [find comment="defconf"]
ssh admin@192.168.1.1 /ip dhcp-server network remove [find comment="defconf"]
ssh admin@192.168.1.1 /ip dhcp-server remove defconf
ssh admin@192.168.1.1 /interface list member remove [find comment="defconf"]
ssh admin@192.168.1.1 /interface list member add comment=MikroBrick interface=ether1 list=WAN
ssh admin@192.168.1.1 /interface bridge remove [find comment="defconf"]
exit /B