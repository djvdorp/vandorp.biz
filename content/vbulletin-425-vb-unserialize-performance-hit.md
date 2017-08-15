Title: vBulletin 4.2.5 vb_unserialize() performance hit
Date: 2017-08-04 07:00
Author: Daniel
Tags: performance, development, internet, php, cpu
Slug: vbulletin-425-vb-unserialize-performance-hit

[Quite a few](https://trends.builtwith.com/cms/vBulletin) of the biggest forums on the internet use vBulletin to build their communities. Their reasons may vary, but one of the reasons why they might want to do so is because the self-hosted version vBulletin 4 came with free forum support for life and ticket support via their Member Ticket System. They also keep on providing (security) updates at quite a steady pace, which is a respectable thing to do if you consider that vBulletin 4 was released 21 December 2009 and the latest stable release (vBulletin 4.2.5) was released on 10th May 2017. vBulletin 4.2.5 is a maintenance and compatibility release (for `PHP7.x` compatibility) as can be read [over here](https://www.vbulletin.com/forum/forum/vbulletin-4/vbulletin-4-questions-problems-and-troubleshooting/4349766-vbulletin-4-2-5), and was much anticipated by many of their customers, as everybody wants a piece of the PHP7 goodness these days, especially when you read blogposts all over the internet that promise you up to a 4x speed improvement when switching over from `PHP5.6.x` to `PHP7.x.x` on your website. WordPress, for example, already supports PHP7 since [late 2015](https://make.wordpress.org/core/2015/09/10/wordpress-and-php7/) so it is great that now also vBulletin joined this club, with a 7.5 years old product I do think that is a respectable move.

So one would go ahead and after thoroughly testing the upgrade from vBulletin 4.2.4 to 4.2.5 on a dev, test and acceptance environment and reviewing the changelog and code changes, one would roll this out to production, likely by means of the [Command Line Upgrade](http://www.vbulletin.com/docs/html/upgrade_cli) if you run vBulletin at a reasonable size. At this point in time you are obviously still running `PHP5.6.x` as you need vBulletin 4.2.5 as the final piece of your puzzle to move over to `PHP7.x.x` in your highly integrated environment, after you have studied [this page](http://php.net/manual/en/migration70.php) about the migration for months. (You actually had quite some months, since `PHP7.0.x` first got released in [late 2015](https://wiki.php.net/todo/php70#timetable) and vBulletin released halfway 2017 as seen above)

You have made backup beforehand, closed down your vBulletin board so that only Administrators can still access it during the upload, and maybe made your site inaccessible to the public audience and only to a limited subset of IP's of your staff maintaining the website. When you run the vBulletin 4.x Publishing Suite and you have disabled the vBulletin CMS and vBulletin Blog products via the AdminCP -> Plugins & Products -> Manage Products screen, you have to re-enable these before upgrading, as otherwise you will hit issues during the upgrade (I learned this the hard way via a forum post that I wanted to link but can't seem to find anymore right now). If you didn't hit this bump in the road, good, then you should have the upgrade completed rather quickly. At this point you might notice that your server seems to become a lot less responsive and the load on your server seems to be increasing. As you are likely running a LAMP or LNMP stack, you first suspect the cause of this to be MySQL, because it is always MySQL, isn't it?
Well, this time it is not. Because even though there seems no explicit mention of in the changelog for vBulletin 4.2.5, there is another big change in this version that you need to know about.

The vBulletin developers decided to do changes in the way that vBulletin handles it's `unserialize()` behavior, very likely because of [the big warning](http://php.net/manual/en/function.unserialize.php) in the PHP Manual and because remote code execution was [possible via unserialize](https://www.notsosecure.com/remote-code-execution-via-php-unserialize/). You can read more about this in great detail [over here](https://paragonie.com/blog/2016/04/securely-implementing-de-serialization-in-php) and I honestly think it is a must-read for every PHP developer on the planet. PHP made some changes in `PHP 5.6.x` and `7.0.x` to reduce the risk of `unserialize()` being exploited but it isn't until `PHP7.1.x` that it can be considered truly safe. So the vBulletin developers read it and built their own `vb_unserialize()` function with a brief PHPDoc one-line description above it, that states: `vBulletin Emulation of Unserialize, to stop abuse of this function`.

So far, so good. You like security, I like security, we all like security. What I don't like, however, is regressions, and especially not performance ones. Because upon inspecting the function signature of this new `vb_unserialize()` fella, you will notice that they never use the PHP `unserialize()` anymore, but instead they have built a sub-optimal performing version of `unserialize()` themselves that seems to have some weird recursion going on that makes `PHP5.6.x` go crazy. And with crazy, I mean performance regression crazy, causing the execution time of `vb_unserialize()` to be (in our case) `2.75 seconds`, versus the `6 milliseconds (!)` that `unserialize()` previously took. That is one way to bring your application server (php-fpm) to it's knees, let me assure you that, as this is amplified for every user hitting your PHP application server, which is quite a lot if you run a forum or website at a big scale. Server loads of over `350` were not uncommon during this time, and made our team lose quite some sleep unfortunately. At this time, New Relic really proved it's value, as it allowed us to break down the time spent within the application server per method. I can post some (redacted) images of this upon request.

I have nothing to complain about the vBulletin Support Staff however, as they help you very well, even after multiple years of buying the license and they gave us some valuable pointers in how to determine the root cause of this performance regression. It turns out that it is possible (yet not officially supported) to run the vBulletin 4.2.4 codebase on a vBulletin 4.2.5 database. It does not work flawlessly, as you will get some vBulletin Database Errors from time to time, mostly due to the fact that there are some database migrations between 4.2.4 and 4.2.5, but you can find and read them yourself in the vBulletin codebase. However, it is better to have a site that is up again (as in, with a running application server) with some occassional database errors, compared to not having a website running anymore at all.

The function signature of `vb_unserialize()` contains a `boolean $usephp` that is set to `false` by the vBulletin developers. If you change this to `true` again, you will have a very minor code change that will make all these problems go away while running `PHP5.6.x` and vBulletin 4.2.5 when you are affected by this performance regression. It might not be needed anymore once you have switched over to `PHP7.1.x` later on, but it is rather easy to revert in the future. I mean, we all use Git or another great version control tool for all our projects, including websites, right? Make sure to document why this change was done, maybe link to this blogpost if you found it useful, because at the time of writing the vBulletin Support Staff mentioned that they have not seen complaints from other users on lower performance of vBulletin 4.2.5 on `PHP5.6.x`. Although development on vBulletin 4.x is more or less officially over, aside from security patches, it may be worth making public for users having the issue. So that is what I did here.

Be aware vBulletin 4.2.5 may not run under `PHP7.2.x`. It was developed and tested for `7.1.x` as the highest PHP version. The last developer working on the project did not believe it would run correctly on `PHP7.2.x` or above. If you want to use `PHP7.2.x` or beyond, you would need to upgrade to vBulletin 5.x, whatever the latest version at the time. At least running `PHP7.2.x` with vBulletin 4.2.5 is not (officially) supported. Be aware vBulletin 5 is very different than vBulletin 4. No styling or add-ons will work after the upgrade, you will be left with a default style. Do your research before upgrading, some customers get surprised and frustrated when they find out things like forum passwords don't exist or calendar events don't get carried over. As always, investigate and test before you decide to upgrade major version.