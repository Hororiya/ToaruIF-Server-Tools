# ToaruIF Server and Tools data

## FAQ

* **What can I do with this code?**

Basically you can operate as private server for ToaruIF, game dead on day 2/12/2024.

* **Which devices are compatible?**

I tested personally with iOS and macOS (installing IPA on apple silicon macbook), but I am pretty sure you can run it on Android.

* **Does it let me use my data from ex-real server?**

No, it can't do that. But you can manipulate server code (or more simply the database) for that. You can even get better stuff compared to ex-real server lmao.

* **Can it run on 7.0.0?**

Yesn't. I have implemented something, but the way that they hardcoded stuff here it won't let you use 100% of the potential game.

## Hosts

* `https://login.index-if.jp` (partially editable, for the first call, must be mapped by DNS at least)
    * `//Auth/gatein.php`: First step, retrieves game data, if client is outdated, first encryption key step etc.
    * `/Auth/login.php`: Third step, makes the login.
* `https://psg.sqex-bridge.jp` (cannot be edited, must be mapped via DNS at least)
    * `/native/session`: Second step, registers the session and provides the api crypto key
* `https://social.index-if.jp/` (can be edited)
    * `/socialsv/*`: Game data. Every steps are from here. (they are converted into `/api/*`)
* `http://cache.index-if.jp/` (can be edited)
    * `ver2/`: New crypto, resources
    * `ver1/`: Old resources endpoint, resources
    * `ver0/`: Old crypto, resources

## Credits

TODO
