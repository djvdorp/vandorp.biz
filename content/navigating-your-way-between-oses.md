Title: Navigating your way between OSes
Date: 2019-01-13 09:00
Author: Daniel
Tags: debian, linux, osx
Slug: navigating-your-way-between-oses

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam convallis massa ac lectus cursus suscipit. Nam condimentum enim in eros placerat pulvinar. Nullam facilisis sodales sapien, rhoncus eleifend sapien malesuada vitae. Pellentesque at nibh at mauris mattis condimentum. Donec fermentum nulla ut est viverra, vitae vehicula turpis placerat. Cras congue dictum lectus viverra eleifend. Maecenas rutrum dictum erat, sit amet pellentesque sem pulvinar id. Fusce eros eros, dignissim at lorem eleifend, semper ultricies nibh. Donec dapibus, felis non aliquam faucibus, dui leo sagittis libero, porta porta magna tortor ac ligula. Integer finibus orci tortor, et tincidunt sapien scelerisque ut. Ut eleifend ut augue sed mollis. Aliquam id molestie enim. Aliquam erat volutpat. Ut et elementum dolor. Duis sit amet nunc malesuada, feugiat eros vitae, mattis diam. Nam aliquam turpis id magna blandit viverra non ut ante.

| Debian apt-get | Debian apt | Arch Linux pacman | NixOS nix-env | Alpine Linux apk |
|----------------|------------|-------------------|---------------|------------------|
| `apt-get update` | `apt update` | `pacman -Syy` | `nix-channel --update` | `apk update` |
| `apt-get upgrade` | `apt upgrade` | `pacman -Syu` | `nix-env -u` | `apk upgrade` |
| `apt-get dist-upgrade` | `apt full-upgrade` | `pacman -Syu` | `nix-env -u` | `apk upgrade` |
| `apt-get install package_name` | `apt install package_name` | `pacman -Syu package_name` | `nix-env -i package_name` | `apk add --no-cache package_name` |
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
