import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#먼저 아메리칸 켄넬클럽이라는 미국 홈페이지에서 견종 이름 크롤링 후 리스트 만들기 함
breed_list = []
def breed_crawling():
    url = "https://www.akc.org/dog-breeds/page/" + str(page)
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    dog_breeds = soup.select('a > h3')
    for breed in dog_breeds:
        try:
            breed_list.append(breed.text)
        except UnicodeEncodeError:
            breed.text.replace('é','e')
            breed_list.append(breed.text)

for page in [1,2,3,4,5]:  #1~26페이지까지 있는데, 26까지 숫자로 기입하는 방법밖에 없나?ㅠ
    breed_crawling()
breed_list = [item.replace(' ','-') for item in breed_list] #추후 작업 때 각각 견종 페이지 들어가기 위해서 견종 띄어쓰기를 -로 바꾸는 작업

#견종 페이지 Health 카테고리에서 "Official Breed Club Statement" 클릭 후 pdf을 다운받고 싶음
def pdf_crawling(a):
    driver = webdriver.Chrome('/Users/admin/Downloads/chromedriver_win32/chromedriver.exe')
    breed_url ='https://www.akc.org/dog-breeds/'
    driver.get(breed_url + a)
    try:
        driver.find_element_by_xpath('//*[@id="panel-HEALTH"]/div/p[3]/a').click()
    except:
        print("no_pdf")
        driver.close()

#견종 페이지 Health 카테고리에 적힌 내용을 크롤링해서 {견종:Health 내용} 딕셔너리를 만들고 싶음
health_dic={}
def health_crawling(b):
    breed_url = "https://www.akc.org/dog-breeds/"
    req = requests.get(breed_url + b)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    health_info = soup.select('#panel-HEALTH > div > p')
    #for info in health_info:
        #health_dic[b] = info

#파이썬 실행해보면 원하는 결과값 출력 실패...        
for each_breed in breed_list:
    pdf_crawling(each_breed)
    print(health_crawling(each_breed).get_text())
