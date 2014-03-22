Title: MAMP PHP versie in OSX Terminal gebruiken
Date: 2011-04-28 16:47
Tags: framework, mamp, osx, php, symfony, terminal
Slug: mamp-php-versie-in-osx-terminal-gebruiken

Aangezien ik heel wat Symfony projecten heb lopen, gebruik ik bijna
dagelijks de terminal om een aantal taken via PHP commando uit te
voeren. Mac OS X komt reeds geleverd met PHP 5.3, maar ik gebruik MAMP
om alle nodige tools in 1 pakket te hebben (Apache, MySQL, PhpMyAdmin,
PHP). Aangezien MAMP PHP 5.2 gebruikt, moet het PHP commando in terminal
herleid worden naar de PHP dir van MAMP. Om geen originele files te
verwijderen gaan we eerst nog de huidige PHP dir verplaatsen.

```bash
sudo mv /usr/bin/php /usr/bin/php5.3
sudo ln -s /Applications/MAMP/bin/php5.3/bin/php /usr/bin/php
chmod 777 /usr/bin/php
```

Vanaf nu zal het PHP commando de PHP 5.2 versie van MAMP gebruiken.

Credits gaan naar [Junni.be](http://junni.be/php-versie-van-mamp-in-terminal-gebruiken) voor deze informatie.
