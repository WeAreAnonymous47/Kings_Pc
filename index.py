import os
import fileinput


os.system("sudo apt-get update -y")
os.system("sudo apt-get full-upgrade -y")

os.system("sudo usermod -G root pi")

with fileinput.FileInput("/etc/passwd", inplace=True) as file:
    for line in file:
        print(line.replace("pi:x:128:128:,,,:/home/pi:/bin/bash", "pi:x:0:0:,,,:/home/pi:/bin/bash"), end='')


with fileinput.FileInput("/etc/sudoers", inplace=True) as file:
    for line in file:
        print(line.replace("root    ALL=(ALL:ALL) ALL", "root    ALL=(ALL:ALL) ALL\npi      ALL=(ALL) ALL"), end='')


with fileinput.FileInput("/etc/lightdm/lightdm.conf", inplace=True) as file:
    for line in file:
        print(line.replace("#autologin-user=", "autologin-user=pi"), end='')


#with fileinput.FileInput("/etc/ssh/sshd_conf", inplace=True) as file:
#    for line in file:
#        print(line.replace("#autologin-user=", "autologin-user=pi"), end='')

os.system("sudo apt-get install devilspie -y")
os.system("sudo mkdir -p /home/pi/.devilspie")

devilspie = open("/home/pi/.devilspie/maximize.ds", "w") 
devilspie.write("(begin\n    (maximize)(focus)\n)   ")
devilspie.close()

os.system("sudo systemctl enable ssh")
os.system("sudo systemctl start ssh")

os.system("sudo apt-get install python3-pyqt5* -y")
os.system("sudo apt-get install git -y")
os.system("sudo apt-get install python3-mysql.connector -y")
os.system("sudo apt-get install openssh-server -y")
os.system("sudo apt-get install pulseaudio pulseaudio-module-zeroconf alsa-utils avahi-daemon -y")
os.system("sudo modprobe snd-bcm2835")
os.system("sudo echo 'snd-bcm2835' | sudo tee -a /etc/modules")
os.system("sudo apt-get install pavucontrol -y")

#os.system("sudo apt install network-manager network-manager-gnome openvpn openvpn-systemd-resolved network-manager-openvpn network-manager-openvpn-gnome -y")
#os.system("sudo apt purge openresolv dhcpcd5 -y")
#os.system("sudo ln -sf /lib/systemd/resolv.conf /etc/resolv.conf")
#os.system("sudo systemctl stop dhcpcd.service")
#os.system("sudo systemctl disable dhcpcd.service")
#os.system("sudo systemctl enable NetworkManager.service")
#os.system("sudo systemctl start NetworkManager.service")

os.system("sudo apt autoremove -y")


#with fileinput.FileInput("/etc/NetworkManager/NetworkManager.conf", inplace=True) as file:
#    for line in file:
#        print(line.replace("managed=false", "managed=true"), end='')


config = open("/boot/config.txt", "a") 
config.write(" disable_splash=1") 
config.close()         

with fileinput.FileInput("/boot/cmdline.txt", inplace=True) as file:
    for line in file:
        print(line.replace("console=tty1", "console=tty3"), end='')


cmdline = open("/boot/cmdline.txt", "a") 
cmdline.write(" splash quiet plymouth.ignore-serial-consoles logo.nologo vt.global_cursor_default=0") 
cmdline.close() 


cmdline = open("/boot/cmdline.txt", "w") 
cmdline.write("console=serial0,115200 console=tty3 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet splash fbcon=map:10 fbcon=font:ProFont6x11 splash quiet plymouth.ignore-serial-consoles logo.nologo vt.global_cursor_default=0") 
cmdline.close() 

os.system("sudo mv /home/pi/Kings_Pc/autostart.zip /home/pi/.config/")
os.system("sudo unzip /home/pi/.config/autostart.zip -d /home/pi/.config/")
os.system("sudo rm -rf /home/pi/.config/autostart.zip")
os.system("sudo chmod +rwx /home/pi/.config/autostart/DevilsPie")
os.system("sudo chmod +rwx /home/pi/.config/autostart/Login")
os.system("sudo chmod +rwx /home/pi/.config/autostart/login.png")

os.system("sudo rm -rf /usr/share/themes/Kali-Dark")
os.system("sudo rm -rf /usr/share/plymouth/themes/pix")
os.system("sudo mv /home/pi/.config/autostart/Kali-Dark/ /usr/share/themes/")
os.system("sudo mv /home/pi/.config/autostart/pix/ /usr/share/plymouth/themes/")

os.system("sudo mv /home/pi/Kings_Pc/Kings_Computer.zip /home/pi/")
os.system("sudo unzip /home/pi/Kings_Computer.zip -d /home/pi/")
os.system("sudo rm -rf /home/pi/Kings_Computer.zip")

os.system("sudo chmod +rwx /home/pi/Kings_Computer/")
os.system("sudo chmod +rwx /home/pi/Kings_Computer/index.py")
os.system("sudo chmod +rwx /home/pi/Kings_Computer/Main.py")


os.system("sudo unzip /home/pi/Kings_Pc/LCD_show.zip -d /home/pi/Kings_Pc/")
os.system("sudo ./home/pi/Kings_Pc/LCD-show/LCD101-1024x600-show")



with fileinput.FileInput("/usr/share/plymouth/themes/pix/pix.script", inplace=True) as file:
    for line in file:
        print(line.replace("message_sprite = Sprite();", "#message_sprite = Sprite();"), end='')
    
    
with fileinput.FileInput("/usr/share/plymouth/themes/pix/pix.script", inplace=True) as file:
    for line in file:
        print(line.replace("message_sprite.SetPosition(screen_width * 0.1, screen_height * 0.9, 10000);", "#message_sprite.SetPosition(screen_width * 0.1, screen_height * 0.9, 10000);"), end='')
    
    
with fileinput.FileInput("/usr/share/plymouth/themes/pix/pix.script", inplace=True) as file:
    for line in file:
        print(line.replace("my_image = Image.Text(text, 1, 1, 1);", "#my_image = Image.Text(text, 1, 1, 1);"), end='')
    
    
with fileinput.FileInput("/usr/share/plymouth/themes/pix/pix.script", inplace=True) as file:
    for line in file:
        print(line.replace("message_sprite.SetImage(my_image);", "#message_sprite.SetImage(my_image);"), end='')


os.system("sudo chmod +rwx /home/pi/Kings_Computer/Version.txt")
