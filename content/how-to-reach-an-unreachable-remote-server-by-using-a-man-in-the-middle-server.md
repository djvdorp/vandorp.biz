Title: How to reach an unreachable remote server by using a man-in-the-middle server
Date: 2014-02-06 19:15
Author: Daniel
Tags: internet, linux, osx
Slug: how-to-reach-an-unreachable-remote-server-by-using-a-man-in-the-middle-server

Yesterday, I needed to solve a pretty interesting problem. I had to move
a few TB's of data from server A to server B in different countries and
datacenters. Server A had a pretty decent connection, Server B had an
awesome fast connection, but the connection between each other was
unbelievably slow due to network routing issues within the route or one
of the datacenters.

As the TB's of data mentioned above needed to be moved before a deadline
in the near future, and I already contacted the hosts from both
datacenters and they couldn't help me out, I had to solve it myself.

With some Googling and thinking through some options, I came with the
idea of using a man-in-the-middle server (Server C).

Server A's connection to Server C was fast. Server B's connection to
Server C was fast as well. The routing between Server A and Server B was
just bugged!

As Server C was only used to pass data through, I used a simple
dedicated server box with (pretty much) unmetered traffic from
[Kimsufi/OVH](http://www.isgenoeg.nl).

The solution I used is based on [this](http://superuser.com/questions/170758/how-to-ssh-to-an-unreachable-remote-machine-by-tunneling-through-a-server-that-e) StackOverflow post. I have used
it for SSH access, SCP transfers and Rsync synchronization.

  

Ony one ssh tunnel is needed from Server A (to Server C).

First make sure Server C is properly configured for this:  
Edit Server C's _/etc/ssh/sshd_config_:

```
AllowTcpForwarding yes
GatewayPorts yes
```

After that, do a restart of the ssh/sshd service.

From Server A:

```bash
ssh -N -R 0.0.0.0:8022:localhost:22 serverCUser@serverC
```

Now you can just connect from Server B onto Server A with:

```bash
ssh -p 8022 serverAUser@serverC
```

Additionally you may want to define some stuff in _~/.ssh/config_:

```
Host gate.serverA
HostName serverC
Port 8022
HostKeyAlias serverA
```

This allows you to do the more coherent:
```bash
ssh serverAUser@gate.serverA
```
and at the same time not be bothered with server fingerprint
mismatches.
