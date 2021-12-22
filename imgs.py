from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import urllib.request
from fs.osfs import OSFS


keywords = ['Raccoon','Ferret', 'Chinchilla']

for keyword in keywords:

    driver = webdriver.Chrome(executable_path = 'C:\Python-AI\chromedriver')
    driver.get('https://www.google.com/search?q='+ keyword +'&tbm=isch')

    for i in range(0,5):
        driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')
        try:
            # for clicking show more results button
            driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[2]/div[2]/input').click()
        except Exception as e:
            pass
        time.sleep(2)



    soup = BeautifulSoup(driver.page_source,'html.parser')
    img_tags = soup.find_all("img", class_="rg_i")

    with OSFS('./download/') as myfs:
        if(not myfs.exists(keyword)):
            myfs.makedir(keyword)

    count = 1
    for i in img_tags:
        print(i, end='\r')
        try:
            download_path = 'download/'+ keyword +'/' + 'keyword' + str(count)+ '.jpg'
            urllib.request.urlretrieve(i['src'], download_path)
            print("Number of images download = " + str(count), end='\r')
            count +=1

        except Exception as e:
            pass