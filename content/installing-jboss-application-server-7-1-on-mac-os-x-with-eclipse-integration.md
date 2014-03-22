Title: Installing JBoss Application Server 7.1 on Mac OS X with Eclipse Integration
Date: 2012-03-11 18:38
Author: Daniel
Tags: development, osx
Slug: installing-jboss-application-server-7-1-on-mac-os-x-with-eclipse-integration

Took me a while to figure out, so here are the steps I followed to get
everything working:

​1. Download and extract the latest JBoss AS 7 version here:

_http://download.jboss.org/jbossas/7.1/jboss-as-7.1.1.Final/jboss-as-7.1.1.Final.tar.gz_

​2. Extracted files go to _/usr/bin_

​3. Download and extract the latest version of Eclipse Indigo for mac 64-bits here:

_http://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/indigo/SR2/eclipse-jee-indigo-SR2-macosx-cocoa-x86\_64.tar.gz_

​4. Extracted files go to /Applications

​5. Install my JBoss Tools:
Go to Help > Install New Software... > Add
In the _Location_, add this url:
_http://download.jboss.org/jbosstools/updates/nightly/trunk/_

Check the upper box to install all JBoss 7 related tools

​6. After that,  follow this tutorial to get the JBoss Application Server in Eclipse for easy management:

_http://hudson.jboss.org/jenkins/job/JBoss-AS7-Docs/lastSuccessfulBuild/artifact/guides/developer-getting-started-guide/target/docbook/publish/en-US/html/gettingstarted.html\#install.eclipse_

​7. start the server in Eclipse. To open the web interface, go to http://localhost:8080

​8. To manage your server, you will need to add an admin user first.
you do this by using the command line and run:
```bash
sh /usr/bin/<Jboss-AS-dir>/bin/add-user.sh
```
the group default is okay (just press enter) and choose your own
username and password (twice) combo. after that, confirm by typing YES.  
now access the management interface here: http://localhost:9990/console
