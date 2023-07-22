import requests
from bs4 import BeautifulSoup

# 크롤링할 페이지의 URL
url = "https://blog.naver.com/babplus123"

# 이미지 URL을 담을 리스트
image_urls = []

try:
    # HTTP GET 요청을 보냅니다.
    response = requests.get(url)
    response.raise_for_status()  # 에러 체크

    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    # 모든 이미지 태그를 찾아서 반복합니다.
    print(111)
    # print(soup)
    print(soup.find_all('img'))
    for img_tag in soup.find_all('img'):

        print(img_tag)

        # # 이미지 태그의 src 속성을 가져와서 리스트에 추가합니다.
        # img_url = img_tag.get('src')
        # if img_url:
        #     image_urls.append(img_url)

    # 추출한 이미지 URL 리스트 출력
    print(222)
    print(image_urls)

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"An error occurred: {err}")
