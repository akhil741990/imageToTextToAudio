'''
Created on 30-Aug-2020

@author: akhil
'''
import cv2
import pytesseract
import numpy as np


img = cv2.imread('/home/akhil/Downloads/sapiens.jpeg')
#Alternatively: can be skipped if you have a Blackwhite image
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gray, img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
gray = cv2.bitwise_not(img_bin)

kernel = np.ones((2, 1), np.uint8)
img = cv2.erode(gray, kernel, iterations=1)
cv2.imwrite("/home/akhil/Downloads/sapiens-grey.jpg", img)
img = cv2.dilate(img, kernel, iterations=1)
cv2.imwrite("/home/akhil/Downloads/sapiens-grey-dilate.jpg", img)
out_below = pytesseract.image_to_string(img)
print("OUTPUT:", out_below)



from gtts import gTTS 

import os 
  
# The text that you want to convert to audio 
mytext = 'Hello world'
  
# Language in which you want to convert 
language = 'en'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=out_below, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("welcome.mp3") 
  
# Playing the converted file 
os.system("mpg321 welcome.mp3") 
