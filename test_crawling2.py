from selenium import webdriver
import requests
from bs4 import BeautifulSoup

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
            imageUrlList.append(imageUrl)
        
        return imageUrlList
    except AttributeError :
        return None    

getImageUrls()
