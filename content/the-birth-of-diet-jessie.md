Title: The Birth of Diet Jessie
Date: 2015-05-09 17:34
Author: Daniel
Tags: linux
Slug: the-birth-of-diet-jessie

If you have been following me on [Twitter](https://twitter.com/djvdorp) recently, you might have noticed that I was pretty excited when [Debian 8.0 Jessie](https://wiki.debian.org/DebianJessie) got released two weeks ago. Not only have I been a fan of Debian and it's derivatives (Ubuntu, Linux Mint) for a long time, but also my love for it got recently revived when I started my new job as a [DevOps Engineer](https://www.mendix.com/careers/devops-engineer/) at [Mendix](https://www.mendix.com/) in Rotterdam.

However, what I do not really like is the current state of (for example) the default user interface of the Debian-family and the bloat that comes with it. I used to like GNOME (that was, before GNOME 3) and I never really liked Unity that Ubuntu ships instead, at least, not for a productive computer (it's great on your HTPC for example).

So, what did I do? I decided to write a quick setup-script for me (and others) to enjoy and put it up on my [Github](https://github.com/djvdorp/diet-jessie).
This script, which I have named "Diet Jessie", tries to supply you with a very tiny and productive setup, without all the bloatware featured with a full desktop setup.

The starting point for this installation is a clean Debian 8 (Jessie) netinstall with only these two options selected:

* OpenSSH server
* Standard system utilities

As seen here:
![Debian Jessie Software Selection]({filename}/images/debian-jessie-software-selection.png)

This does, however, not mean that it is only compatible with Debian 8 (Jessie). As long as the package names in the list below are installable via apt-get/aptitude on your distribution, it might probably work just as well on other Debian versions and/or Debian-derivatives like Ubuntu, Linux Mint etc.

Of course, the package selection is a matter of personal preference, but I have tried to come up with a pretty complete (basic) setup to get going. However, I am completely open for improvements, so let the pull requests or comments come in!