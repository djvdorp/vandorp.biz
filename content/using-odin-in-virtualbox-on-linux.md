Title: Using ODIN in VirtualBox on Linux
Date: 2017-02-02 19:00
Author: Daniel
Tags: linux
Slug: using-odin-in-virtualbox-on-linux

A while ago I wrote that [2017 is The Year of the Linux Desktop](https://www.vandorp.biz/2017/01/2017-the-year-of-the-linux-desktop/), but there is one thing that has always bothered me and that is that I need to fallback to my Windows machine to flash a new ROM on my lovely Samsung (Android) phone. Of course there is [Heimdall](http://glassechidna.com.au/heimdall/), but I never got it to work, and especially not for ROMs consisting of multiple separate files. So I decided to give running ODIN in VirtualBox a shot, and while I did not get everything working yet, [these steps](https://www.reddit.com/r/linux/comments/19kaic/using_odin_in_virtualbox_windows_guest_in_linux/) got me pretty far already:

1. Download and install the [VirtualBox Extension Pack](https://www.virtualbox.org/manual/ch01.html#intro-installing)
2. In the Windows VM in VirtualBox, go to `Settings -> USB` and enable `Enable USB 2.0 (EHCI) Controller`
3. Blacklist the `cdc_acm` driver in your Linux host machine: `sudo modprobe -r cdc_acm` and add `blacklist cdc_acm` to your `/etc/modprobe.d/blacklist.conf`
4. On your Linux host machine, add your user to the `vboxusers` group: `usermod -G vboxusers -a username`
5. Inside the Windows VM, install [Samsung Smart Switch PC (previously KIES)](http://www.samsung.com/us/smart-switch/) for the drivers, or install just the drivers [from here](http://samsungusbdriver.com/)
6. Put the phone in Download Mode, plug in the USB Cable, forward the USB Port to the Windows VM (in VirtualBox, with a running Windows VM, in the menu go to `Devices -> USB` and tick your phone)
7. [Download](http://odindownload.com/) and extract ODIN, and when the phone is connected in download mode, it should work.
