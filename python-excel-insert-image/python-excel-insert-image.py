from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()

img1 = Image('1.jpg')
img2 = Image('2.jpg')

ws = wb.active

#ws.add_image(img1)
#ws.add_image(img2)

#ws.add_image(img1, 'B2')
#ws.add_image(img2, 'B14')

ws.add_image(img1, 'A2')
ws.add_image(img2, 'G2')

wb.save('excel-image.xlsx')
