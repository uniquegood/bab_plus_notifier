import os
from dotenv import load_dotenv
import pytesseract
import cv2 

def getProcessedImage(url):
    os.system("mkdir -p image")
    os.system("curl " + url + " > ./image/test.png")
    img = cv2.imread("./image/test.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # gray = cv2.medianBlur(gray, 5)
    cv2.imwrite('./image/grayImage.png',gray)
    cropGray = gray[80:190,180:770]
    cv2.imwrite('./image/grayCropImage.png',cropGray)
    os.system("rm -rf ./image")
    return cropGray

def imageToString(image):
    text = pytesseract.image_to_string(image, lang='Hangul', config = '-l Hangul --oem 3 --psm 6')
    text = text.replace(" ", "")
    return text
    
