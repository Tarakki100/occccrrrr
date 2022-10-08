#Approach 1: using easyocr

# command to install easyocr:   
#pip install easyocr



import easyocr

image = 'SIGNA.jpg'     #read image

read = easyocr.Reader(['en'])      #take only english language content
result = read.readtext(image,paragraph="False")            #read the text present in english language
print(result)   #print the text 


#Approach 2: using pytesseract

#command to install pytessract and opencv python
#pip install pytesseract
#pip install opencv-python


import pytesseract
import cv2

img = cv2.imread('dummy.jpg')    #read image
result = pytesseract.image_to_string(img)    #capture the text
print(result)     #print the text
