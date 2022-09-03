import pyqrcode
url = pyqrcode.create('https://github.com/Sephens')

url.svg('uca-url.svg', scale=3)
url.eps('uca-url.eps', scale=2)
print(url.terminal(quiet_zone=1))