# General
Some useful scripts simplifying bureaucracy, especially when living in Munich, Germany.

# termin.py
Small tool to show availability of appointments for Niederlassungserlaubnis mit Blauer Karte EU.

~~Source of the data - https://www22.muenchen.de/termin/index.php?loc=FS&ct=1071898~~

Source of the data - https://www46.muenchen.de/termin/index.php?cts=1080805 (For Niederlassungserlaubnis mit Blauer Karte EU)
<<<<<<< HEAD
Also Add your ***IFTTT API Key***

```sh

```
    ifttt_webhook_url = 'https://maker.ifttt.com/trigger/test_event/with/key/{ADD_YOUR_KEY_HERE}'

=======

Also Add your ""IFTTT API Key"""
>>>>>>> d5963743603a5714081dc80affe5a9c92bdac84d

```sh
$ python3 termin.py
```

Please note the script **does not perform appointment booking**, it just tells you current status, so you may run it with crone and\or add some custom notifier.

License
MIT
