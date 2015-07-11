Title: Online.nl ADSL 2+ settings/configuration 
Date: 2015-07-11 14:28
Author: Daniel
Tags: internet
Slug: online-nl-adsl-2-plus-settings-configuration

For my home internet connection, I am a customer of [Online.nl](http://online.nl) for their very affordable *Supersnel Internet 30 Mb/s* package.
With this subscription, you will also receive their default modem, the *Huawei HG655d home gateway* which gets all it's settings pushed via the provider.
However, after not even 2 years of service, my *Huawei HG655d* died last week, out of the blue, with no warning sign whatsoever.

One of my very friendly colleagues was so kind to borrow me a spare ADSL/VDSL modem, the *FRITZ!Box 7360*.
So I asked my provider for the settings for their ADSL connection, which they were not able to provide, all they could do is send me over a new default modem within 3-5 working days (I was already offline for 3 days at that time).

I was very upset with their customer service and decided to go on the hard way, and figure out the Online.nl ADSL 2+ settings/configuration myself, which I will post here for my own future reference, as well as for other customers who might once just experience the same kind of issues with this provider's hardware:

```
Subscription: Online.nl Supersnel Internet 30 Mb/s
ADSL type: ADSL 2+ (ITU G.992.5) Annex A (analog phone line)

Account Information required: no (no username/password needed)

VLAN Settings: none (no VLAN ID needed)

DSL ATM Settings:
  VPI: 8
  VCI: 35
  Encapsulation: Bridged (Routed Bridge Encapsulation)
    Obtain the IP address automatically (DHCP)
    DHCP host name: (blank)

DNS (v4) servers:
Use other DNSv4 servers:
  Preferred DNSv4 server: 8.8.8.8 (Google DNS)
  Alternative DNSv4 server: 8.8.4.4 (Google DNS)
```

**Note 1:** I don't use the providers DNS servers (194.134.5.55 and 194.134.5.5) on purpose, since I have more faith in Google's DNS.

**Note 2:** I haven't been able to setup my home phone (VOIP) since my default modem wasn't accessible anymore at all, and you need to find the SIP settings there [as described here in Dutch](http://online.gebruikers.eu/forum/viewthread.php?thread_id=4714&highlight=firebug&pid=41199#post_41199).
