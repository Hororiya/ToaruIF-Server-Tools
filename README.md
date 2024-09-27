# ToaruIF Server and Tools data

## Hosts

* `https://login.index-if.jp` (partially editable, for the first call, must be mapped by DNS at least)
    * `//Auth/gatein.php`: First step, retrieves game data, if client is outdated, first encryption key step etc.
    * `/Auth/login.php`: Third step, makes the login.
* `https://psg.sqex-bridge.jp` (cannot be edited, must be mapped via DNS at least)
    * `/native/session`: Second step, registers the session and provides the api crypto key
* `https://social.index-if.jp/` (can be edited)
    * `/socialsv/*`: Game data. Every steps are from here.
* `http://cache.index-if.jp/` (can be edited)
    * `ver2/`: New crypto, resources
    * `ver1/`: Old crypto, resources

## Credits

TODO