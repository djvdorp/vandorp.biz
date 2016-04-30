Title: NixOS installation on multi-boot system with GRUB (from Arch installation) using an embedded configuration file
Date: 2016-04-30 16:00
Author: Daniel
Tags: linux
Slug: nixos-installation-on-multi-boot-system-with-grub-from-arch-installation

A while ago, I started playing around with [Arch Linux](https://www.archlinux.org/) on a spare computer. After following the (excellent) [Beginners' guide](https://wiki.archlinux.org/index.php/beginners'_guide) I ended up with a rather nice [LVM on LUKS](https://wiki.archlinux.org/index.php/Dm-crypt/Encrypting_an_entire_system#LVM_on_LUKS) setup. This spare computer has one physical (SSD) disk (`/dev/sda`), which is divided in `/dev/sda1` (which is `/boot`, a bootable GRUB2 partition used and setup with Arch) and `/dev/sda2` which is my `cryptroot` that, when unlocked, is a single large `lvmpool` with the full size of the partition `/dev/sda2`. I have installed Arch on 3 `lvs` (`arch-root` for the root filesystem, `arch-home` for the home folders and `arch-swap` for the swap partition), as seen in the image below:

![NC110 cryptroot lvmpool lvs]({filename}/images/nc110-cryptroot-lvmpool-lvs.jpg)

Since I read lots of great things about [NixOS](https://nixos.org/), I am trying to install NixOS next to my current Arch install, so I created 3 more `lvs` similar to the `arch-{root,home,swap}` `lvs` above, and I followed the [NixOS installation guide](https://nixos.org/nixos/manual/index.html#sec-installation). I want to re-use my existing GRUB2 from Arch which resides on the (bootable) GRUB2 partition `/dev/sda1`. Of course, I am [not the](https://www.reddit.com/r/NixOS/comments/2bvgr4/nixos_dual_boot_grub_setup/) [first one](http://lists.science.uu.nl/pipermail/nix-dev/2015-August/017931.html) trying to achieve something like this or similar to this. However, the GRUB2 [documentation on specifying devices](https://www.gnu.org/software/grub/manual/grub.html#Device-syntax) is rather limited and cumbersome, especially in the more complex cases such as on my [LVM on LUKS](https://wiki.archlinux.org/index.php/Dm-crypt/Encrypting_an_entire_system#LVM_on_LUKS) setup. With the help of the [Unix & Linux StackExchange](http://unix.stackexchange.com/questions/279856/nixos-installation-on-multi-boot-system-with-grub-from-arch-installation) and some [very useful information](https://www.reddit.com/r/linuxquestions/comments/2wm7oq/help_manually_booting_from_grub_console_into/cp0mqlc) from Reddit user [cookie_enthusiast](https://www.reddit.com/user/cookie_enthusiast) on the `/r/linuxquestions` page on Reddit, I managed to get this working. To further spread and share this knowledge, as well as for my own future reference, I will write down my steps taken here, which are largely based on the aforementioned sources.

I installed NixOS by following the [NixOS installation guide](https://nixos.org/nixos/manual/index.html#sec-installation) and modified the `/etc/nixos/configuration.nix` file to look like this:

```
# Use the GRUB 2 boot loader.
boot.loader.grub.enable = true;
boot.loader.grub.version = 2;
# Define on which hard drive you want to install Grub.
boot.loader.grub.device = "nodev";
boot.initrd.luks.devices = [ { name = "cryptroot"; device = "/dev/sda2"; preLVM = true; } ];
```

I also added `nixpkgs.config.allowUnfree = true;` to allow unfree packages which might be needed for your NixOS system configuration.

It turns out that GRUB2 works well with UUIDs, and not so well with device names. With this knowledge in mind, we need the following 4 UUIDs at hand, before we can (manually) create an extra GRUB menuentry to our NixOS `grub.cfg` `configfile`:

1. The UUID of the LUKS device.
2. The UUID of the LVM Volume Group.
3. The UUID of the LVM Logical Volume.
4. The UUID of the filesystem containing the `grub.cfg` file we want to load via the `configfile` directive in GRUB2.

I will list here how to obtain these four UUIDs:

1. Execute `cryptsetup luksUUID /dev/sda2` and **remove all the dashes (`-`) from the UUID**, `a0cb535a-8468-485f-a220-a5f49e85c9f4` would become `a0cb535a8468485fa220a5f49e85c9f4` in my case.
2. Execute `vgdisplay` and look for the `VG UUID`, `lvmpool` with UUID `5atKN9-PQBi-T9wb-Iyz8-qP4y-HN2E-c5uLOT` in my case.
3. Execute `lvdisplay` and look for the `LV UUID` of the LV Name or LV Path that contains your `grub.cfg` file, `nix-root` or `/dev/lvmpool/nix-root` with UUID `C9zkjF-IHu0-qQkP-KgLf-8rAy-TVPu-HQ7gtj` in my case.
4. Execute `lsblk -p -o +UUID` and look for the UUID of the Device Path that contains your `grub.cfg` file, `/dev/mapper/lvmpool-nix--root` with UUID `cc6a06bb-336f-4e9f-a5f0-fdd43e7f548f` in my case.

This will allow you to create the following extra GRUB menuentry for referencing our NixOS `grub.cfg` `configfile`, which is on my `nix-root` `lv` and because of the `boot.loader.grub.device = "nodev";` in my `/etc/nixos/configuration.nix` there is no GRUB installed for my NixOS installation (in Arch, this would go into `/etc/grub.d/40_custom`):

```
menuentry 'NixOS' {
	insmod crypto
	insmod cryptodisk
	insmod luks
	insmod lvm
	cryptomount -u a0cb535a8468485fa220a5f49e85c9f4
	set root='lvmid/5atKN9-PQBi-T9wb-Iyz8-qP4y-HN2E-c5uLOT/C9zkjF-IHu0-qQkP-KgLf-8rAy-TVPu-HQ7gtj'
	search --fs-uuid --set=root cc6a06bb-336f-4e9f-a5f0-fdd43e7f548f
	configfile '/boot/grub/grub.cfg'
}
```

To clarify this even more, this contains some literal values such as `lvmid` which is **not** supposed to be replaced with the name or ID of your LVM. This is not properly documented anywhere, it seems. The same issue applies for when your put the UUID of your LUKS device in the `cryptomount -u` line **with dashes** in it, GRUB will just tell you `Press any key to continue`, which is (obviously) not very helpful. 

The bare template for a manual GRUB menuentry to boot from `crypt -> LVM -> root` with an [LVM on LUKS](https://wiki.archlinux.org/index.php/Dm-crypt/Encrypting_an_entire_system#LVM_on_LUKS) setup would thus be:

```
menuentry 'NixOS' {
	insmod crypto
	insmod cryptodisk
	insmod luks
	insmod lvm
	cryptomount -u <LUKS UUID without dashes>
	set root='lvmid/<LVM Volume Group UUID>/<LVM Logical Volume UUID>'
	search --fs-uuid --set=root <Filesystem UUID>
	configfile '/boot/grub/grub.cfg'
}
```

Again, I would like to owe a big thank you to Reddit user [cookie_enthusiast](https://www.reddit.com/user/cookie_enthusiast) and [Alexander Batischev](http://unix.stackexchange.com/users/167612/alexander-batischev) for helping me out here, as well as all other sources referenced earlier.
