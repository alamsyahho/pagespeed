from lib.google_pagespeed import GooglePagespeed
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-u', '--url', action='store', dest='url', help='Url', required=True)
parser.add_argument('-s', '--strategy', action='store', dest='strategy', choices=['desktop', 'mobile'], default='desktop', help='Choice: desktop/mobile')

args = parser.parse_args()

if __name__ == "__main__":
    ps = GooglePagespeed()
    pageSpeed = ps.analyse(args.url, strategy=args.strategy)

    print(pageSpeed)