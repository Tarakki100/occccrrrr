# command to install easyocr:   pip install easyocr



import easyocr

image = 'SIGNA.jpg'

read = easyocr.Reader(['en'])
result = read.readtext(image,paragraph="False")
print(result)



#command to install pytessract
#pip install pytesseract
#pip install opencv-python


import pytesseract
import cv2

img = cv2.imread('dummy.jpg')
result = pytesseract.image_to_string(img)
print(result)
