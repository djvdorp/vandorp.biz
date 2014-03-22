Title: Install JBoss AS 7 on a Debian 6 VPS
Date: 2012-03-15 19:02
Author: Daniel
Tags: internet, linux
Slug: install-jboss-as-7-on-a-debian-6-vps

I followed the following steps, all instructions as root ofcourse:

First install the JDK package for Linux:
```bash
wget http://download.oracle.com/otn-pub/java/jdk/7/jdk-7-linux-x64.tar.gz
mkdir /usr/lib/jvm/  
tar zxvf jdk-7-linux-x64.tar.gz -C /usr/lib/jvm/
```

set it as default:
```bash
update-alternatives --install /usr/bin/java java
/usr/lib/jvm/jdk1.7.0/bin/java 1065  
update-alternatives --install /usr/bin/javac javac
/usr/lib/jvm/jdk1.7.0/bin/javac 1065
```

check if it is at the top of the priority:  
```bash
update-alternatives --config java
```
check this output to ensure everything is alright:
```bash
java -version
javac -version
```
   
Then install JBoss 7 AS:
```bash
wget http://download.jboss.org/jbossas/7.1/jboss-as-7.1.1.Final/jboss-as-7.1.1.Final.tar.gz
tar zxvf jboss-as-7.1.1.Final.tar.gz -C /usr/local/
cd /usr/local/
mv jboss-as-7.1.1.Final/ jboss-7.1.1
addgroup jboss
useradd -g jboss jboss  
chown -R jboss:jboss /usr/local/jboss-7.1.1/
```

edit this config to make it accessable from the outside world:
```bash
nano jboss-7.1.1/standalone/configuration/standalone.xml
```

change the "interfaces" part to:

```xml
<interfaces>
    <interface name="management">
        <any-address/>
    </interface>
    <interface name="public">
        <any-address/>
    </interface>
</interfaces>
```

make Jboss available as a service:  
```bash
touch /etc/init.d/jboss
chmod 755 /etc/init.d/jboss  
nano /etc/init.d/jboss
```

put this in it:
```bash
#!/bin/sh
### BEGIN INIT INFO
# Provides: jboss
# Required-Start: $local_fs $remote_fs $network $syslog
# Required-Stop: $local_fs $remote_fs $network $syslog
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: Management of JBoss AS v7.x
### END INIT INFO

#Defining JBOSS_HOME
JBOSS_HOME=/usr/local/jboss-7.1.1

case “$1″ in
start)
echo “Starting JBoss AS7…”
sudo -u jboss sh ${JBOSS_HOME}/bin/standalone.sh &
;;
stop)
echo “Stopping JBoss AS7…”
sudo -u jboss sh ${JBOSS_HOME}/bin/jboss-admin.sh –connect command=:shutdown
;;
log)
echo “Showing server.log…”
tail -1000f ${JBOSS_HOME}/standalone/log/server.log
;;
*)
echo “Usage: /etc/init.d/jboss {start|stop|log}”
exit 1
;; esac
exit 0
```
 
now you can use:
```bash
service jboss start | stop | log
```

then add some iptables rules to access it at port 80:
```bash
iptables -t nat -A PREROUTING -p tcp -m tcp --dport 80 -j REDIRECT --to-ports 8080
iptables -t nat -A PREROUTING -p udp -m udp --dport 80 -j REDIRECT --to-ports 8080
```

save the rules:

```bash
iptables-save > /etc/firewall.conf
```
make them autoload at reboot:
```bash
nano /etc/network/interfaces
```
find this line: _auto lo_
put this on a new line below it: _iface lo inet loopback_

```bash
pre-up iptables-restore < /etc/firewall.conf
```

then save and exit. reboot and see if everything works!
