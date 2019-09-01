from lib.google_pagespeed import GooglePagespeed

p = GooglePagespeed()

r = p.analyse('https://www.google.com', strategy='desktop')

print(r)