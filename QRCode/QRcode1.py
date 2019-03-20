import pyqrcode
print('Enter Patients URL')
url=input()
qr=pyqrcode.create(url)
qr.png('link.png',scale=7)
  
