Title: Installing JBoss Application Server 7.1 on Mac OS X with Eclipse Integration
Date: 2012-03-11 18:38
Author: Daniel
Tags: development, osx
Slug: installing-jboss-application-server-7-1-on-mac-os-x-with-eclipse-integration

Took me a while to figure out, so here are the steps I followed to get
everything working:

​1) download and extract the latest JBoss AS 7 version here:  

http://download.jboss.org/jbossas/7.1/jboss-as-7.1.1.Final/jboss-as-7.1.1.Final.tar.gz

​2) extracted files go to /usr/bin

​3) download and extract the latest version of Eclipse Indigo for mac
64-bits here:  

http://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/indigo/SR2/eclipse-jee-indigo-SR2-macosx-cocoa-x86\_64.tar.gz

​4) extracted files go to /Applications

​5) **Install my JBoss Tools:**  
Go to Help\>Install New Software..-\>Add  
In the "Location", add this url:  
**http://download.jboss.org/jbosstools/updates/nightly/trunk/**  
Check the upper box to install all JBoss 7 related tools

​6) after that,  follow this tutorial to get the JBoss Application
Server in Eclipse for easy management:  

http://hudson.jboss.org/jenkins/job/JBoss-AS7-Docs/lastSuccessfulBuild/artifact/guides/developer-getting-started-guide/target/docbook/publish/en-US/html/gettingstarted.html\#install.eclipse

​7) start the server in Eclipse. To open the web interface, go to
http://localhost:8080

​8) To manage your server, you will need to add an admin user first.  
you do this by using the command line and run:  
sh /usr/bin/\<Jboss-AS-dir\>/bin/add-user.sh  
the group default is okay (just press enter) and choose your own
username and password (twice) combo. after that, confirm by typing YES.  
now access the management interface here:  
http://localhost:9990/console
