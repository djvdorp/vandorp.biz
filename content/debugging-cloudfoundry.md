Title: Debugging Cloud Foundry
Date: 2017-10-31 07:00
Author: Daniel
Tags: debugging, cloud, foundry, cloudfoundry, paas
Slug: debugging-cloudfoundry

At [Mendix](https://www.mendix.com/cloud-native-and-multi-cloud-deployment/) we use [Cloud Foundry](https://www.cloudfoundry.org/) quite extensively. So I get to debug some apps in Cloud Foundry from time to time, and I have been keeping this post as a draft for ages. However, since it could also be useful for other people to have this overview, I will publish it today so that I can refer people to it.

If you are running an ancient Cloud Foundry with DEA (which you really shouldn't do), you can read [this blogpost](https://andypiper.co.uk/2014/02/17/getting-inside-cloud-foundry-for-debug-and-profit/) for how to enter a Warden container. I would advise to use `$ ps -ef | grep warden/depot` to identify your Warden Container instead of the proposed `$ ps -ef | grep warden` as you will get less noise.
You can find the `instances.json` file easily on the Warden runner by using `find /var/vcap -name instances.json`, it will likely be in `/var/vcap/data/dea_next/db/instances.json` though.

For almost everything Cloud Foundry related, you will need the apps GUID, which you can obtain via: `cf app APPNAME --guid` or if you prefer the hard way, `CF_TRACE=true cf app APPNAME | grep summary`. One of the requests should be something like: `GET /v2/apps/937992d7-5fbe-441f-858e-c704291eb127/summary HTTP/1.1`. Your app GUID is `937992d7-5fbe-441f-858e-c704291eb127`.

Once you have the app’s GUID, you can look in the file `/var/vcap/data/dea_next/db/instances.json` in the `runner` VM. This file contains the mapping of app instances to Warden containers. Look for the `application_id` and `instance_index` fields that match the app and instance you care about, then use the `warden_container_path` value in the same JSON hash.

Now, let's go back to the present. If you are running a recent Cloud Foundry you will have Diego with a Garden-runC backend (no, not Garden-Linux). A good start here is to read [this page](https://government-paas-team-manual.readthedocs.io/en/latest/guides/CloudFoundry_debugging/) as it has excellent documentation already. Cloud Foundry also has documentation on this, which is [located here](https://docs.cloudfoundry.org/devguide/deploy-apps/troubleshoot-app-health.html). Again, you will need the app GUID, or you could do: `cf curl /v2/apps/$(cf app APPNAME --guid)/stats | jq 'with_entries(.value = .value.stats.host)'` (requires [jq](https://stedolan.github.io/jq/) installed) or the harder way `CF_TRACE=true cf app APPNAME | grep stats | grep -v GET | jq .\"0\".\"stats\".\"host\"`. You are welcome!
