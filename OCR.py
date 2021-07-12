#Importing Dependencies
import easyocr
import cv2
from matplotlib import pyplot as plot
import numpy as np

#Importing Image Path
IMAGE_PATH = 'meme.jpg'
reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext(IMAGE_PATH)
print(result)

#Defining Coordinates
tl = tuple(result[0][0][0])
br = tuple(result[0][0][2])
text = result[0][1]
font = cv2.FONT_HERSHEY_SIMPLEX

#Showing the result, this handles images having multiple lines by itself
image = cv2.imread(IMAGE_PATH)
for i in result:
    tl = tuple([int(val) for val in i [0][0]])
    br = tuple([int(val) for val in i [0][2]])
    text = i[1]
    font = cv2.FONT_HERSHEY_SIMPLEX
    image = cv2.rectangle(image, tl, br, (0,255,0), 5)
    image = cv2.putText(image, text, tl, font, .5, (255,255,255), 2, cv2.LINE_AA)

plot.figure(figsize=(10, 10))
plot.imshow(image)
plot.show()