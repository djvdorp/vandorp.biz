Title: Ubuntu: root password workaround
Date: 2011-02-21 17:01
Author: Daniel
Tags: login, passwd, password, root, ubuntu, workaround, linux
Slug: ubuntu-root-password-workaround

Mocht je ooit je root password van je Ubuntu installatie vergeten zijn,
maar wel (fysieke) toegang tot de desbetreffende computer hebben, kan je
via deze workaround het wachtwoord van de root-user aanpassen, **zonder
het oude wachtwoord te hoeven weten!**

**  
**

1.  Start de pc op
2.  Als de bootloader (GRUB) laad, druk op ESC, zodat je de lijst met
    kernels te zien krijgt
3.  Druk op E
4.  Kies de optie Kernel
5.  Zet achter het stuk met **ro quiet**het volgende stukje tekst:
    **init=/bin/bash**
6.  Na het starten kom je in een terminal. Type hier in: **passwd**
7.  Wijzig het wachtwoord en reboot de pc
8.  Start normaal op, en login met username: **root**en password wat je
    net ingesteld hebt
9.  Voila! Je bent binnen.

 

PS: Credit gaat naar Olaf voor deze briljante tip!
