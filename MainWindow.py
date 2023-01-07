import subprocess
import tkinter as tk  # import tk for mainframe
from tkinter import filedialog
from tkinter.simpledialog import askstring  # import simpledialog with askstring
from PyQt6 import QtWidgets, uic  # import PyQT6 widgets
import sys  # import sys for QT widget UI
import os  # import os for path related code

root = tk.Tk()  # tkinter for user prompt
current_dir = os.getcwd()  # assign path
ip_address = "192.168.1.1"  # variable
ssid = "MikroTik "  # variable
wpa2 = "[/system routerboard get serial-number]"  # variable
mt_def_ip = "192.168.88.1"  # variable
ssh_dir = filedialog.askdirectory(parent=root, initialdir=current_dir,  # assign user home dir to a variable
                                  title='Please select Windows User\'s directory (C:\\Users\\User)')


class Ui(QtWidgets.QMainWindow):  # class for GUI

    with open("Part1.bat", 'r') as file:  # open .bat file with read permissions
        content = file.readlines()  # read contents of the .bat file
        keyword = "gateway="  # set keyword to look for
        for line in content:  # listing for function
            if keyword in line:  # if statement
                raw_line = line  # assign line to a variable
                i = raw_line.find(keyword)  # get line index
                pre_trim = raw_line[i:i + len(keyword) + len(line)]  # trim line from the beginning
                sec_trim = pre_trim[len(keyword):]  # trim line from the end
                last_used_ip = sec_trim[:-2]  # trim line from the end

    defIP = ip_address[:-1]  # assign trimmed value to the variable

    with open("Part3.bat", 'r') as file:  # open .bat file with read permissions
        content = file.readlines()  # read contents of the .bat file
        keyword = "set wlan1 ssid="  # set keyword to look for
        keyword2 = " frequency=2442 mode=ap-bridge disabled=no"  # set keyword to look for
        for line in content:  # listing for function
            if keyword in line:  # if statement
                raw_line = line  # assign line to a variable
                i = raw_line.find(keyword)  # get line index
                pre_trim = raw_line[i:i + len(keyword) + len(line)]  # trim line from the beginning
                sec_trim = pre_trim[len(keyword):]  # trim line from the end
                last_used_ssid = sec_trim[:-len(keyword2)]  # trim line from the end
    defSSID = ssid  # assign trimmed value to the variable

    with open("Part3.bat", 'r') as file:  # open .bat file with read permissions
        content = file.readlines()  # read contents of the .bat file
        keyword = "wpa2-pre-shared-key="  # set keyword to look for
        for line in content:  # listing for function
            if keyword in line:  # if statement
                raw_line = line  # assign line to a variable
                i = raw_line.find(keyword)  # get line index
                pre_trim = raw_line[i:i + len(keyword) + len(line)]  # trim line from the beginning
                sec_trim = pre_trim[len(keyword):]  # trim line from the end
                last_used_wpa = sec_trim[:-1]  # trim line from the end
    defWPA = wpa2  # assign trimmed value to the variable

    file = open("Part1.bat", 'r')  # open .bat file with read permissions
    replacement = ""  # empty string for replacement purposes
    for line in file:  # listing for function
        changes = line.replace(last_used_ip, defIP)  # assign the replacement line to a variable
        replacement = replacement + changes  # merge string to replace with an empty string
    file.close()  # close opened .bat file
    fout = open("Part1.bat", 'w')  # open .bat file with write permissions
    fout.write(replacement)  # write string with replacement
    fout.close()  # close opened .bat file

    file = open("Part2.bat", 'r')  # open .bat file with read permissions
    replacement = ""  # empty string for replacement purposes
    for line in file:  # listing for function
        changes = line.replace(last_used_ip, defIP)  # assign a replacement line to a variable
        replacement = replacement + changes  # merge string to replace with an empty string
    file.close()  # close opened .bat file
    fout = open("Part2.bat", 'w')  # open .bat file with write permissions
    fout.write(replacement)  # write string with replacement
    fout.close()  # close opened .bat file

    file = open("Part3.bat", 'r')  # open .bat file with read permissions
    replacement = ""  # empty string for replacement purposes
    for line in file:  # listing for function
        changes = line.replace(last_used_ip, defIP)  # assign a replacement line to a variable
        replacement = replacement + changes  # merge string to replace with an empty string
    file.close()  # close opened .bat file
    fout = open("Part3.bat", 'w')  # open .bat file with write permissions
    fout.write(replacement)  # write string with replacement
    fout.close()  # close opened .bat file

    file = open("Part3.bat", 'r')  # open .bat file with read permissions
    replacement = ""  # empty string for replacement purposes
    for line in file:  # listing for function
        changes = line.replace(last_used_ssid, defSSID)  # assign a replacement line to a variable
        replacement = replacement + changes  # merge string to replace with an empty string
    file.close()  # close opened .bat file
    fout = open("Part3.bat", 'w')  # open .bat file with write permissions
    fout.write(replacement)  # write string with replacement
    fout.close()  # close opened .bat file

    file = open("Part3.bat", 'r')  # open .bat file with read permissions
    replacement = ""  # empty string for replacement purposes
    for line in file:  # listing for function
        changes = line.replace(last_used_wpa, defWPA)  # assign a replacement line to a variable
        replacement = replacement + changes  # merge string to replace with an empty string
    file.close()  # close opened .bat file
    fout = open("Part3.bat", 'w')  # open .bat file with write permissions
    fout.write(replacement)  # write string with replacement
    fout.close()  # close opened .bat file

    ssh_dir = os.path.join(ssh_dir, './' + '.ssh' + './' + "known_hosts")

    with open(ssh_dir, 'r') as file:  # open .ssh file with read permissions
        content = file.readlines()  # read contents of the .ssh file
        for line in content:  # listing for function
            if mt_def_ip in line:  # if statement
                raw_line = line  # assign lign to a variable
                file = open(ssh_dir, 'r')  # open decoded config file with read permissions
                replacement = ""  # empty sting for replacement purposes
                for line in file:  # listing for function
                    changes = line.replace(raw_line, "\n")  # assign a replacement line to a variable
                    replacement = replacement + changes  # merge string to replace with an empty string
                file.close()  # close opened config file
                fout = open(ssh_dir, 'w')  # open decoded config file with write permissions
                fout.write(replacement)  # write string with replacement
                fout.close()  # close opened config file

    def __init__(self):  # initialise GUI function
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('MicroBrickGui.ui', self)  # Load the .ui file

        self.button = self.findChild(QtWidgets.QPushButton, 'ipButton')  # find button by name in GUI
        self.button.clicked.connect(self.change_ip)  # assign action to a button

        self.button = self.findChild(QtWidgets.QPushButton, 'Step3ConfButton')  # find button by name in GUI
        self.button.clicked.connect(self.step3_config)  # assign action to a button

        self.button = self.findChild(QtWidgets.QPushButton, 'Step5ConfButton')  # find button by name in GUI
        self.button.clicked.connect(self.step5_config)  # assign action to a button

        self.button = self.findChild(QtWidgets.QPushButton, 'ssidButton')  # find button by name in GUI
        self.button.clicked.connect(self.change_ssid)  # assign action to a button

        self.button = self.findChild(QtWidgets.QPushButton, 'wpa2Button')  # find button by name in GUI
        self.button.clicked.connect(self.change_wpa2)  # assign action to a button

        self.button = self.findChild(QtWidgets.QPushButton, 'Step6Button')  # find button by name in GUI
        self.button.clicked.connect(self.step6_config)  # assign action to a button

        self.ip = self.findChild(QtWidgets.QTextBrowser, 'ipView')  # Find the text browser
        self.ip.setHtml(ip_address)  # Show the content of variable in html form

        self.ssid = self.findChild(QtWidgets.QTextBrowser, 'ssidView')  # Find the text browser
        self.ssid.setHtml(ssid)  # Show the content of variable in html form

        self.wpa2 = self.findChild(QtWidgets.QTextBrowser, 'wpa2View')  # Find the text browser
        self.wpa2.setHtml(wpa2)  # Show the content of variable in html form

        self.show()  # show GUI

    def change_ip(self):  # Function to change the ip in .bat
        global ip_address  # assign global variable
        ip_address = askstring("New IPAddress", "default: 192.168.1.1")  # get new IP address from user
        raw_ip = ip_address[:-1]  # assign trimmed value to the variable
        file = open("Part1.bat", 'r')  # open .bat file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("192.168.1.", raw_ip)  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened .bat file
        fout = open("Part1.bat", 'w')  # open .bat file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened .bat file

        file = open("Part2.bat", 'r')  # open .bat file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("192.168.1.", raw_ip)  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened .bat file
        fout = open("Part2.bat", 'w')  # open .bat file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened .bat file

        file = open("Part3.bat", 'r')  # open .bat file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("192.168.1.", raw_ip)  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened .bat file
        fout = open("Part3.bat", 'w')  # open .bat file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened .bat file
        self.ip.setHtml(ip_address)  # Show the content of variable in html form

    def step3_config(self):  # Function to begin the reconfiguration
        subprocess.run(os.path.join(current_dir, './' + 'Part1.bat'))  # Execute .bat with commands
        return

    def step5_config(self):  # Function to end the reconfiguration
        subprocess.run(os.path.join(current_dir, './' + 'Part2.bat'))  # Execute .bat with commands
        return

    def step6_config(self):  # Function to add optional config
        subprocess.run(os.path.join(current_dir, './' + 'Part3.bat'))  # Execute .bat with commands
        return

    def change_ssid(self):  # Function to change ssid from default value
        global ssid  # assign global variable
        ssid = askstring("New SSID", "default: MikroTik")
        file = open("Part3.bat", 'r')  # open .bat file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("MikroTik", ssid)  # assign a replacement line to a variable
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened config file
        fout = open("Part3.bat", 'w')  # open .bat file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened .bat file
        self.ssid.setHtml(ssid)  # Show the content of variable in html form

    def change_wpa2(self):  # Function to change wpa2 from default value
        global wpa2  # assign global variable
        wpa2 = askstring("New wpa2", "default: S/N")
        file = open("Part3.bat", 'r')  # open .bat file with read permissions
        replacement = ""  # empty string for replacement purposes
        for line in file:  # listing for function
            changes = line.replace("[/system routerboard get serial-number]", wpa2)  # assign a repl. line to a var
            replacement = replacement + changes  # merge string to replace with an empty string
        file.close()  # close opened .bat file
        fout = open("Part3.bat", 'w')  # open .bat file with write permissions
        fout.write(replacement)  # write string with replacement
        fout.close()  # close opened .bat file
        self.wpa2.setHtml(wpa2)  # Show the content of variable in html form


app = QtWidgets.QApplication(sys.argv)  # defines widget as app
window = Ui()  # defines window
app.exec()  # loops app
