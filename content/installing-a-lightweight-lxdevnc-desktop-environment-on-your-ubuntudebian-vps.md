Title: Installing a lightweight LXDE+VNC desktop environment on your Ubuntu/Debian VPS
Date: 2012-01-04 10:20
Author: Daniel
Tags: internet, linux
Slug: installing-a-lightweight-lxdevnc-desktop-environment-on-your-ubuntudebian-vps

Found some great instructions for putting a lightweight desktop
environment on your (Lowend) VPS or server.  
Uses no more then like 40mb RAM tops, but can be tweaked to only
10-20mb I think.

    //Make sure Debian is the latest and greatest

    apt-get update
    apt-get upgrade
    apt-get dist-upgrade

    //Install X, LXDE, VPN programs

    apt-get install xorg lxde-core tightvncserver

    //Start VNC to create config file

    tightvncserver :1

    //Then stop VNC

    tightvncserver -kill :1  

    //Edit config file to start session with LXDE:

    nano ~/.vnc/xstartup

    //Add this at the bottom of the file:
    lxterminal &
    /usr/bin/lxsession -s LXDE &

    //Restart VNC

    tightvncserver :1

 

 

You then connect using the VNC viewer of your choice on your local
computer. I use the "VNC Free Edition Viewer for Windows Stand-Alone
Viewer" at: http://www.realvnc.com Configure the viewer to access your
VPS at: xxx.xxx.xxx.xxx:5901.

Original credits go to [LongShot @ LET.com][]

  [LongShot @ LET.com]: http://www.lowendtalk.com/profile/227/LongShot
