import pyqrcode
import png

link  = "https://github.com/Sephens"
qr_code = pyqrcode.create(link)
qr_code.png("steve.png", scale = 5)
qr_code.show()