# Created by abhignan-rakshith at 10:20 am 11-01-2024 using PyCharm

# # TODO: 1. Create an ISBN-13 barcode
# from barcode import ISBN13
#
# num = '9780140217155'
#
# book_barcode = ISBN13(isbn=num, writer=None)
# book_barcode.save('isbn13_barcode')


# # TODO: 2. Create an EAN-13, GTIN-13 barcode
# from barcode import EAN13
#
# number = '8901234123457'
#
# ean13_barcode = EAN13(number)
#
# ean13_barcode.save('ean13_barcode')


# # TODO: 3. Create a JAN (Japanese Article Numbering) barcode
# from barcode import JAN
# from barcode.writer import ImageWriter  # png support using pillow
#
# number = '450123412310'
#
# japanese_barcode = JAN(number, writer=ImageWriter())
#
# japanese_barcode.save('japanese_barcode')


# TODO: 4. Create a QR code

# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode

# String which represents the QR code
s = "https://www.udemy.com/home/my-courses/learning/"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
url.svg("udemy.svg", scale=8)

# Create and save the png file naming "myqr.png"
url.png('udemy.png', scale=6)
