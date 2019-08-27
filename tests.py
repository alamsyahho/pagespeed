from modules.pagespeed import PageSpeed

p = PageSpeed()

r = p.analyse('https://www.example.com', strategy='desktop')

print(r)