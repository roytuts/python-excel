from xlwt import Workbook, easyxf

tl = easyxf('border: left thick, top thick')
t = easyxf('border: top thick')
tr = easyxf('border: right thick, top thick')
r = easyxf('border: right thick')
br = easyxf('border: right thick, bottom thick')
b = easyxf('border: bottom thick')
bl = easyxf('border: left thick, bottom thick')
l = easyxf('border: left thick')

w = Workbook()

ws = w.add_sheet('Border')
ws.write(1,1,style=tl)
ws.write(1,2,style=t)
ws.write(1,3,style=tr)
ws.write(2,3,style=r)
ws.write(3,3,style=br)
ws.write(3,2,style=b)
ws.write(3,1,style=bl)
ws.write(2,1,style=l)

ws = w.add_sheet('Border and Data')
ws.write(1,1,'Second Row Second Column',style=tl)
ws.write(1,2,'Second Row Third Column',style=t)
ws.write(1,3,'Second Row Fourth Column',style=tr)
ws.write(2,3,'Third Row Fourth Column',style=r)
ws.write(3,3,'Fourth Row Fourth Column',style=br)
ws.write(3,2,'Fourth Row Third Column',style=b)
ws.write(3,1,'Fourth Row Second Column',style=bl)
ws.write(2,1,'Third Row Second Column',style=l)

w.save('borders.xls')
