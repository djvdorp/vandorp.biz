Title: Ruby Gems errors oplossen (updaten en cleanen)
Date: 2011-04-28 16:54
Author: Daniel
Tags: cleanup, gems, osx, rails, ruby
Slug: ruby-gems-errors-oplossen-updaten-en-cleanen

Begin, voor het updaten van je Gems, altijd met éénmaal **sudo gem
update --system**. Dit is om je ruby-gems package (de basis) te updaten.

Normaal gesproken kan je je losse gems het beste updaten, door meerdere
malen **sudo gem update**gevolgd door een **sudo gem cleanup** te runnen
(thanks, Olaf!). Echter, soms geeft dit problemen, zoals deze hieronder:

 

<div>

> <div>
>
> ...  
>  Attempting to uninstall rails-2.3.5  
>  Unable to uninstall rails-2.3.5:  
>  Gem::InstallError: cannot uninstall, check \`gem list -d rails\`  
>  ...
>
> </div>
>
> <div>
>
> <!--more-->
>
> </div>

</div>

Following the instructions I then ran **gem list -d rails** noting the
install path for newer gems was now /Library/Ruby/Gems/1.8 whereas the
older gems that cleanup was failing on were in
/System/Library/Frameworks/Ruby.framework/Versions/1.8/usr/lib/ruby/gems/1.8.
So the solution was to run cleanup once while overriding GEM\_HOME as
follows:


    sudo sh -c 'GEM_HOME=/System/Library/Frameworks/Ruby.framework/Versions/1.8/usr/lib/ruby/gems/1.8 gem cleanup'

<div>

Credits gaan naar [Gabrito.com][] voor deze informatie.

</div>

  [Gabrito.com]: http://gabrito.com/post/mac-os-x-gem-cleanup-failing
    "Gabrito.com"
