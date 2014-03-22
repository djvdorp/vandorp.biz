Title: How to fix Ubuntu 12.04 LTS bugs
Date: 2012-06-13 13:47
Author: Daniel
Tags: linux
Slug: how-to-fix-ubuntu-12-04-lts-bugs

While installing a new server on my work this week, I found 2 most
irritating (and non-professional) bugs in the LTS release (latest
version) Ubuntu 12.04 (server).

#### **“Signal out of range” when starting grub after server installation**
_Fix:_
Boot from the live cd and open a terminal. Assuming your root is on
`/dev/sda1`, then do this:

```bash
sudo -s
mount -t ext4 /dev/sda1 /mnt
nano /mnt/etc/default/grub
```

When the editor comes up, uncomment ( remove the _#_ ) this line
and save and exit: `#GRUB_TERMINAL=console`

```bash
for f in sys proc dev ; do mount --bind /$f /mnt/$f ; done
chroot /mnt
update-grub
```

After the update-grub, reboot and you should be good.

#### **Alert ! /dev/disk/by-uuid/75800786-8994 does not exist. Drop to a shell**
_Fix:_
Boot from the live cd and open a terminal.Assuming your root is on
`/dev/sda1`, then do this:

```bash
sudo -s
mount -t ext4 /dev/sda1 /mntnano /etc/default/grub
```

add `rootdelay=xx` to this line, save and exit:
`GRUB_CMDLINE_LINUX_DEFAULT="**rootdelay=60**"`

```bash
for f in sys proc dev ; do mount --bind /$f /mnt/$f ; done
chroot /mnt
update-grub
```

After the `update-grub`, run `dpkg --configure -a`,
then reboot and you should be good.

I had both errors and fixed them both at once by combining them before
running update-grub.  
I hope this will help you all!

