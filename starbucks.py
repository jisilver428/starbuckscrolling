from selenium import webdriver
import bs4
import time
import pandas as pd

def star(result):
    driver=webdriver.Chrome('C:/Users/jieun/AppData/Local/Programs/Python/Python37/WebDriver/chromedriver.exe')
    driver.get('https://www.istarbucks.co.kr/store/store_map.do')
    time.sleep(5)
    
    loca=driver.find_element_by_class_name('loca_search')
    loca.click()
    time.sleep(5)

    loca=driver.find_element_by_class_name('sido_arae_box')
    li=loca.find_elements_by_tag_name('li')
    li[0].click()
    time.sleep(5)
    

    gugun=driver.find_element_by_class_name('gugun_arae_box')
    guli=gugun.find_element_by_tag_name('li')
    guli.click()
    time.sleep(5)

    source=driver.page_source
    bs=bs4.BeautifulSoup(source,'html.parser')
    entire=bs.find('ul',class_='quickSearchResultBoxSidoGugun')
    li_list=entire.find_all('li')

    for infor in li_list:
        print(infor.find('strong').text+infor.find('p',attrs={'class':'result_details'}).text)
        store_name=infor.find('strong').text
        store_address=infor.find('p').text
        result.append([store_name]+[store_address])

    time.sleep(5)
    loca=driver.find_element_by_class_name('loca_search')
    loca.click()
    time.sleep(5)

    loca=driver.find_element_by_class_name('sido_arae_box')
    li=loca.find_elements_by_tag_name('li')
    li[1].click()
    time.sleep(5)
    

    gugun=driver.find_element_by_class_name('gugun_arae_box')
    guli=gugun.find_element_by_tag_name('li')
    guli.click()
    time.sleep(5)

    source=driver.page_source
    bs=bs4.BeautifulSoup(source,'html.parser')
    entire=bs.find('ul',class_='quickSearchResultBoxSidoGugun')
    li_list=entire.find_all('li')

    for infor in li_list:
        print(infor.find('strong').text+infor.find('p').text)
        store_name=infor.find('strong').text
        store_address=infor.find('p').text
        result.append([store_name]+[store_address])



    return

def cs_star():
    result=[]
    print('start!')
    star(result)
    
    star_table=pd.DataFrame(result, columns=['store_name','store_address'])
    star_table['store_address_fix1']=star_table.store_address.str.split('(').str[0]
    star_table['store_address_fix2']=star_table.store_address_fix1.str.split('02-').str[0]
    star_table['store_address_final']=star_table.store_address_fix2.str.split('031-').str[0]
         
    
    st=star_table.to_csv("./starbucks.csv", encoding="cp949", mode='w', index=True)

if __name__== '__main__':
    cs_star()
