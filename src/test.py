
import datetime as dt
from datetime import timedelta
import os
import sys
from dotenv import load_dotenv

import crawling
import ocr
import slack

def findCorrectLaunchImage(imageUrlList):
    # 오늘 날짜
    now = dt.datetime.today()
    # today = now.strftime("%m월%d일")
    today = now.strftime("07월24일")

    for url in imageUrlList:
        img = ocr.getProcessedImage(url)
        text = ocr.imageToString(img)
        if "점심" in text and today in text:
            return url
    return None


def findCorrectDinnerImage(imageUrlList):
    # 오늘 날짜,내일 날짜 구하기
    today = dt.datetime.today()
    tomorrow = today + timedelta(days=1)
    # today = now.strftime("%m월%d일")
    today = today.strftime("07월24일")
    tomorrow = tomorrow.strftime("%m월%d일")
    urlList = []

    for url in imageUrlList:
        print(url)
        img = ocr.getProcessedImage(url)
        text = ocr.imageToString(img)
        if ("저녁" in text and today in text) or ("점심" in text and tomorrow in text):
            urlList.append(url)
    return urlList

## argv
## 점심 : 0
## 저녁 : 1

if __name__ == "__main__":

    # dotenv에서 url이랑 정보들 가져올 수 있게 함
    load_dotenv(verbose=True)
    
    # 매개변수 확인
    if len(sys.argv) != 2:
        slack.sendSlackErrorMessage("매개변수 문제로 프로그램이 종료되었습니다.")
        print("매개변수 하나 지정해서 넣으소")
        sys.exit()
    menuTimeFlag = sys.argv[1]
    if (menuTimeFlag != '0' and menuTimeFlag != '1')  :
        slack.sendSlackErrorMessage("매개변수 문제로 프로그램이 종료되었습니다.")
        print("매개변수 0, 1 중에 넣으소")
        sys.exit()
    isLaunch = sys.argv[1] == '0'


    # 블로그에서 게시글 내 이미지들의 url을 가져옴
    imageUrlList = crawling.getImageUrls()
    if (imageUrlList == None):
        slack.sendSlackErrorMessage("홈페이지에서 메뉴 이미지를 불러오지 못했습니다.")
        print("조졌네이~")
        sys.exit()
    
    # 마지막 이미지는 건물 소개 이미지라 삭제하였음
    imageUrlList.pop() 

    # 날짜와 점심/저녁이 일치한 이미지 찾기
    # 점심 찾을땐 String, 저녁 찾을 땐 list<String>이 반환됨

    #결과에 따른 슬랙봇 메세지 전송
    
    if isLaunch == True:
        url = findCorrectLaunchImage(imageUrlList)
        if (url == None):
            slack.sendSlackErrorMessage("블로그에 올라온 이미지를 제대로 읽지 못했거나, 이미지가 올라와있지 않습니다.")
            sys.exit()
        slack.sendSlackLaunchMessage(url)
    else:
        urlList = findCorrectDinnerImage(imageUrlList)
        if len(urlList) < 2: 
            slack.sendSlackErrorMessage("블로그에 올라온 이미지를 제대로 읽지 못했거나, 이미지가 올라와있지 않습니다.")
            sys.exit()
        slack.sendSlackDinnerMessage(urlList[0], urlList[1])

