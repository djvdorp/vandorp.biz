Title: Running VirtualBox in Headless Mode with VNC
Date: 2017-02-02 18:30
Author: Daniel
Tags: linux
Slug: running-virtualbox-in-headless-mode-with-vnc

A [quite annoying bug](https://bugreports.qt.io/browse/QTBUG-57608) while using the VirtualBox 5.1.x release, apparently [caused by Qt5](https://github.com/i3/i3/issues/2497), has forced people that use [Tiling Window Managers](https://en.wikipedia.org/wiki/Tiling_window_manager) [like me](http://i3wm.org/) to look at alternative ways to keep on using VirtualBox until a fix has been released. Luckily, VirtualBox has a [quite excellent Headless Mode](https://www.virtualbox.org/manual/ch07.html) that not a lot of people know about. It is also pretty trivial to start using it:

1. Download and install the [VirtualBox Extension Pack](https://www.virtualbox.org/manual/ch01.html#intro-installing)
2. Enable the Remote Display Server, either via [the GUI](https://www.virtualbox.org/manual/ch03.html#settings-display) (`Display -> Remote Display`) or running `VBoxManage modifyvm "VM name" --vrde on`
3. Start your Virtual Machine (VM) in Headless Mode: `VBoxHeadless --startvm "VM name" --vrde on`
4. Connect to it using [your favorite RDP viewer](https://www.virtualbox.org/manual/ch07.html#rdp-viewers): `xfreerdp +clipboard /w:1920 /h:1080 /v:0.0.0.0:3389`
5. [Read the documentation](https://www.virtualbox.org/manual/ch07.html#vboxheadless) on what else is possible with [VirtualBox Headless Mode](https://www.virtualbox.org/manual/ch07.html#idm3202)
