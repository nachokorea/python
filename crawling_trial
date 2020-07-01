import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

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

for page in [1]:  #1~26
    breed_crawling()
breed_list = [item.replace(' ','-') for item in breed_list]
print(breed_list) #checking point

def pdf_crawling(a):
    driver = webdriver.Chrome('/Users/admin/Downloads/chromedriver_win32/chromedriver.exe')
    breed_url ='https://www.akc.org/dog-breeds/'
    driver.get(breed_url + a)
    try:
        driver.find_element_by_xpath('//*[@id="panel-HEALTH"]/div/p[3]/a').click()
    except:
        print("no_pdf")
        driver.close()

health_dic={}
def health_crawling(b):
    breed_url = "https://www.akc.org/dog-breeds/"
    req = requests.get(breed_url + b)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    health_info = soup.select('#panel-HEALTH > div > p')
    #for info in health_info:
        #health_dic[b] = info

for each_breed in breed_list:
    pdf_crawling(each_breed)
    print(health_crawling(each_breed).get_text())
