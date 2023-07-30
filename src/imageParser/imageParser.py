import os
from dotenv import load_dotenv
import pytesseract
import cv2 
import datetime as dt


def getCropedImage(url):
    today = dt.datetime.today()
    today = today.strftime("%m월%d일%H시%M분%S초%f")

    initFileName = "./image/init" + today + ".png"
    cropFileName = "./image/crop" + today + ".png"
    
    print(initFileName)
    os.system("mkdir -p image")
    os.system("curl " + url + " > " + initFileName)
    img = cv2.imread(initFileName)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # gray = cv2.medianBlur(gray, 5)
    # cv2.imwrite('./image/grayImage.png',gray)
    
    cropGray = gray[80:190,180:800]
    cv2.imwrite(cropFileName,cropGray)
    os.system("rm -rf ./image")
    return cropGray


def imageToString(image):
    text = pytesseract.image_to_string(image, lang='Hangul', config = '-l Hangul --oem 3 --psm 6')
    text = text.replace(" ", "")
    return text
    

def findImages(imageUrlList):
    urlDictionary = {}

    for url in imageUrlList:
        cropedImage = getCropedImage(url)
        text = imageToString(cropedImage)
        text = text.strip()
        urlDictionary[text] = url
        
    return urlDictionary