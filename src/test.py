
import datetime as dt
import os
import sys
from dotenv import load_dotenv

import crawling
import ocr
import slack

## argv
## 점심 : 0
## 저녁 : 1

if __name__ == "__main__":
    # 매개변수 확인
    if len(sys.argv) != 2:
        print("매개변수 하나 지정해서 넣으소")
        sys.exit()
    menuTimeFlag = sys.argv[1]
    if (menuTimeFlag != '0' and menuTimeFlag != '1')  :
        print("매개변수 0, 1 중에 넣으소")
        sys.exit()
    isLaunch = sys.argv[1] == '0'

    # dotenv에서 url이랑 정보들 가져올 수 있게 함
    load_dotenv(verbose=True)

    # 블로그에서 게시글 내 이미지들의 url을 가져옴
    imageUrlList = crawling.getImageUrls()
    if (imageUrlList == None):
        slack.sendSlackErrorMessage("홈페이지에서 메뉴 이미지를 불러오지 못했습니다.")
        print("조졌네이~")
        sys.exit()
    
    # 마지막 이미지는 건물 소개 이미지라 삭제하였음
    imageUrlList.pop() 


    now = dt.datetime.now()
    # today = now.strftime("%m월%d일")
    today = now.strftime("07월24일")

    for url in imageUrlList:
        print(url)
        img = ocr.getProcessedImage(url)
        text = ocr.imageToString(img)
        print()
        print(today)
        print(text)
        print()

        if (isLaunch == True):
            if "점심" in text and today in text:
                slack.sendSlackMessage(url)
                sys.exit()
        else:
            if "저녁" in text and today in text:
                slack.sendSlackMessage(url)
                sys.exit()

    slack.sendSlackErrorMessage("블로그에 올라온 이미지를 제대로 읽지 못했거나, 이미지가 올라와있지 않습니다.")



