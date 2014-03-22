Title: Handige UNIX commandos
Date: 2011-05-23 10:11
Author: Daniel
Tags: commands, handy, lamp, lnmp, server, unix, vps, linux
Slug: handige-unix-commandos

Bij het configureren van een Linux server (LAMP/LNMP stack op mijn VPS)
zoek je vaak een paar commandos voor bepaalde taken. Hier zal ik een
paar handige opsommen die ik vaak gebruik:

**Tar.gz een directory (output file komt in de directory waarin je op
dat moment zit):**
```bash
tar -zcvf <name>.tar.gz /home/your/directory
```

**Un-tar.gz een archief:**
```bash
tar -zxvf <name>.tar.gz
```

**Download een file via de command line:**
```bash
wget <url>
```

**Chmod alle .sh files naar 700:**
```bash
chmod 700 *.sh
```

**Alle packages updaten:**
```bash
apt-get update && apt-get upgrade
```
