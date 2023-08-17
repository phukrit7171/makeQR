import qrcode
qrcode.make(input('Your url : ')).save(input('Your file name : ')+'.png')