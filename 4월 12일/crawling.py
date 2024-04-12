from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from bs4 import BeautifulSoup as bs
import requests
def image_save(img_path, save_path, file_name):
    html_data = requests.get(img_path)
    imageFile = open(
        os.path.join(
            save_path, 
            file_name
        ), 
        'wb'
    )
    # 이미지 데이터의 크기 
    chunk_size = 100000000
    for chunk in html_data.iter_content(chunk_size):
        imageFile.write(chunk)
        imageFile.close()
    print('파일 저장 완료')
driver = webdriver.Chrome()
time.sleep(1)
driver.get('https://m.naver.com')
time.sleep(5)
element = driver.find_element(By.ID, 'MM_SEARCH_FAKE')
element.send_keys('구로디지털역 맛집')
search_element = driver.find_element(By.XPATH, 
                                     '//*[@id="sch_w"]/div/form/button')
search_element.click()
time.sleep(3)
map_element = driver.find_element(By.XPATH, 
                                  '//*[@id="place-main-section-root"]/div/div[2]/a')
map_element.click()
time.sleep(3)
list_button = driver.find_element(By.XPATH, 
                                  '//*[@id="_place_portal_root"]/div/a')
list_button.click()
time.sleep(3)
store = driver.find_element(By.CLASS_NAME, 'UEzoS')
store.click()
time.sleep(10)
review_button = driver.find_element(By.XPATH, 
                                    '//*[@id="app-root"]/div/div/div/div[4]/div/div/div/div/a[5]')
review_button.click()
time.sleep(1)
review_add = driver.find_element(By.CLASS_NAME, 'fvwqf')
for i in range(2):
    review_add.click()
    # 5초 대기 
time.sleep(5)
soup = bs(driver.page_source, 'html.parser')
driver.close()
li_list = soup.find_all('li', attrs={
    'class' : 'owAeM'
})

reviews = []
i=1
for li_data in li_list:
    review_data = li_data.find('span', attrs={
    'class' : 'zPfVt'
    }).get_text()
    reviews.append(review_data)
    div_data = li_data.find('div', attrs={
        'class' : 'VAvOk'
    })

    img_list = div_data.find_all('img')
    for img in img_list:
        # print(img['src'])
        file_name = f"review_{i}.png"
        save_path = "./img/"
        image_save(img['src'], save_path, file_name)
        i += 1
import pandas as pd
data = pd.Series(reviews)