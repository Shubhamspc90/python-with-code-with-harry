'''
i am going to create QR code by using python library like qrcode
'''
import qrcode

url=input("Enter your Url:  ")
fileName=input("Entre the file name, you want to save with:  ")
if not(fileName .endswith(".png")):
    fileName=fileName+".png"
    
img=qrcode.make(url)
img.save(fileName)

print("program end succesfully.")