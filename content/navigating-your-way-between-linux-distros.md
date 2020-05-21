Title: Navigating your way between Linux distro's
Date: 2020-05-21 15:00
Author: Daniel
Tags: debian, linux
Slug: navigating-your-way-between-linux-distros

Assuming you are running Linux, you probably have a favorite or most-familiar Linux distribution; I suspect your first one. In my case, this would be the Debian distro and it's [derivatives](https://www.debian.org/derivatives/), such as Ubuntu or the Ubuntu derivatives such as Linux Mint or Pop!_OS. In an ideal world, you would probably want to exclusively use your personal preference for every computer that you have to touch or work with. However, in reality this is often not possible, for example if your employer insists on running something else, or you are using a CPU architecture for which your distro isn't the ideal choice (that would be hard for Debian, considering it aims to be the universal operating system). Either way, sometimes you have to use other distro's as well, let's say when experimenting, learning or playing with containers, and you might feel lost without some of these commands. My personal cheatsheet might help you here, and it definitely helps me:



| Debian apt-get | Debian apt | Arch Linux pacman | NixOS nix-env | Alpine Linux apk |
|----------------|------------|-------------------|---------------|------------------|
| `apt-get update` | `apt update` | `pacman -Sy` | `nix-channel --update` | `apk update` |
| `apt-get upgrade` | `apt upgrade` | `pacman -Su` | `nix-env -u` | `apk upgrade` |
| `apt-get dist-upgrade` | `apt full-upgrade` | `pacman -Su` | `nix-env -u` | `apk upgrade` |
| `apt-get install package_name` | `apt install package_name` | `pacman -S package_name` | `nix-env -i package_name` | `apk add --no-cache package_name` |
| `apt-get remove package_name` | `apt remove package_name` | `pacman -R package_name` | `nix-env -e package_name` | `apk del package_name` |
| `apt-get purge package_name` | `apt remove --purge package_name` | `pacman -Rn package_name`| `nix-env -e package_name` | `apk del package_name` |



Useful sources:

* https://debian-handbook.info/browse/stable/sect.apt-get.html
* https://wiki.manjaro.org/index.php?title=Pacman_Overview
* https://wiki.manjaro.org/index.php?title=Pacman_Tips
* https://wiki.archlinux.org/index.php/pacman
* https://wiki.archlinux.org/index.php/Pacman/Tips_and_tricks
* https://wiki.archlinux.org/index.php/AUR_helpers
* https://nixos.wiki/wiki/Nix_to_Debian_phrasebook
* https://nixos.wiki/wiki/Cheatsheet
* https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management
