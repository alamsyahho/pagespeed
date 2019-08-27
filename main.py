from modules.pagespeed import PageSpeed
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-u', '--url', action='store', dest='url', help='Url', required=True)
parser.add_argument('-s', '--strategy', action='store', dest='strategy', choices=['desktop', 'mobile'], default='desktop', help='Choice: desktop/mobile')

args = parser.parse_args()

if __name__ == "__main__":
    ps = PageSpeed()
    pageSpeed = ps.analyse(args.url, strategy=args.strategy)

    print(pageSpeed)