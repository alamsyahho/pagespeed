# Google PageSpeed Insights for Python

[![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg)]()

`pagespeed` offers a convenient interface for the Google PageSpeed Insights API.
It is written in Python and provides an easy way to query a site's page speed.

## Quickstart
Execute the script:

```
$ python3.7 main.py -u https://www.example.com -s desktop
100

$ python3.7 main.py -u https://www.example.com -s mobile
100

```

## Note
This is for Version 5 of the Google PageSpeed Insights API. Written and tested on python 3.7. This script is modified from the original version in order to easily integrate it as part of jenkins pipeline