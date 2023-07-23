from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import slack_sdk
import datetime as dt
import os
import io
from PIL import Image
from dotenv import load_dotenv
import pytesseract
import cv2 

def getImageUrls() :
    try :
        url = os.getenv("CRAWLING_URL")

        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")
        
        imageUrlList = []

        bidUrl = soup.find_all("div", attrs = {"class" : "se-component se-image se-l-default"})
        for div in bidUrl:
            imageUrl = div.find("img")["src"].split('?')
            imageUrlList.append(imageUrl[0] + "?type=w773")
        
        return imageUrlList
    except :
        return None

def getTodayMenuImage():
    print()


def slackMessageFormat(list):
    now = dt.datetime.now()
    today = now.strftime("%y년 %m월 %d일")
    title = today + " 오늘의 메뉴는???"

    return [
        {
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": title
			}
		},
        {
            "type": "image",
            "title": {
                "type": "plain_text",
                "text": title,
                "emoji": True
            },
            "image_url": list[0],
			"alt_text": "image1"
        }
    ]

def sendSlackMessage(list) :
    slackToken = os.getenv("TEST_TOKEN")
    channel = os.getenv("TEST_CHANNEL")
    client = slack_sdk.WebClient(token = slackToken)

    text = "test"

    client.chat_postMessage(channel = channel, blocks = slackMessageFormat(list))



if __name__ == "__main__":
    load_dotenv(verbose=True)
    imageUrlList = getImageUrls()
    if (imageUrlList == None):
        print("조졌네이~")
        exit()
    else:
        print("0")
        # print(imageUrlList)

    # sendSlackMessage(imageUrlList)
    print()
    url = imageUrlList[0]
    print(url)
    # response = requests.get(imageUrlList[0])
    # print(io.BytesIO(response.content))

    os.system("mkdir -p image")
    os.system("curl " + url + " > ./image/test.png")
    print()
    img = cv2.imread("./image/test.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # gray = cv2.medianBlur(gray, 3)
    cv2.imwrite('./image/grayImage.png',gray)
    gray_temp = gray[50:200,150:800]
    cv2.imwrite('./image/grayTempImage.png',gray_temp)
    text = pytesseract.image_to_string(gray_temp, lang='Hangul', config = '-l Hangul --oem 3 --psm 6')
    text = text.replace(" ", "")
    print(text)
