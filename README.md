# General
Some useful scripts simplifying bureaucracy, especially when living in Munich, Germany.

# termin.py
Small tool to show availability of appointments for Niederlassungserlaubnis mit Blauer Karte EU.

~~Source of the data - https://www22.muenchen.de/termin/index.php?loc=FS&ct=1071898~~

Source of the data - https://www46.muenchen.de/termin/index.php?cts=1080805 (For Niederlassungserlaubnis mit Blauer Karte EU)

Also Add your ""IFTTT API Key"""

```sh
$ python3 termin.py
```

Please note the script **does not perform appointment booking**, it just tells you current status, so you may run it with crone and\or add some custom notifier.

License
MIT
