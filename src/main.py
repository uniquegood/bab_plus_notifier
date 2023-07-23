from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import slack_sdk
import datetime as dt
import os
from dotenv import load_dotenv

def getImageUrls() :
    try :
        url = "https://blog.naver.com/PostList.naver?blogId=babplus123&from=postList&categoryNo=20"

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

def slackMessageFormat(list):
    now = dt.datetime.now()
    today = now.strftime("%y년 %m월 %d일")
    title = today + " 오늘의 메뉴"

    return [{
        "type": "image",
        "title": {
            "type": "plain_text",
            "text": title,
            "emoji": True
        },
        "image_url": list[0],
        "alt_text": "오늘의 메뉴"
    }]

def sendSlackMessage(list) :
    slackToken = os.getenv("SLACK_TOKEN")
    client = slack_sdk.WebClient(token = slackToken)

    text = "test"

    client.chat_postMessage(channel = os.getenv("SLACK_CHANNEL"), blocks = slackMessageFormat(list))


if __name__ == "__main__":
    load_dotenv(verbose=True)
    imageUrlList = getImageUrls()
    if (imageUrlList == None):
        print("조졌네이~")
        exit()
    else:
        print(imageUrlList)

    sendSlackMessage(imageUrlList)
