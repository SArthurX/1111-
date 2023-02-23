from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains
import time
import re

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

h = input("請輸入1111網址：")

driver = webdriver.Chrome(options=options, executable_path=r'C:/Users/NTUST/Desktop/chromedriver')
driver.get(f'{h}')

pages = driver.find_element_by_xpath("/html/body/div[2]/div/div[4]/article/div[2]/div[3]/div/div[1]/span[2]")
p = int(pages.text)
actions = ActionChains(driver)

for page in range(4,4+p*2,+2):
    
    titles = driver.find_elements_by_class_name("mobiContent")
    nextpages = driver.find_elements_by_class_name("pageJumper")
    
    for title in titles:
        print (title.text)
        
    if page <= p*2:
        if nextpages[0].text == nextpages[3].text:
            actions.click(nextpages[0])
            actions.perform()
        else:
            actions.click(nextpages[2])
            actions.perform()
    else:
        startpage = nextpages[0]
        actions.click(startpage)
        actions.perform()

x = input("範圍：")
def pf(p):
    print("地區：",areas.text)
    print("科目：",titles[1+(i-1)*5].text)
    print("需求對象：",titles[2+(i-1)*5].text)
    print("時資：",titles[3+(i-1)*5].text)
    print("\n")

for page in range(4,4+p*2,+2):
    
    titles = driver.find_elements_by_class_name("mobiContent")
    nextpages = driver.find_elements_by_class_name("pageJumper")
    if page <= p*2:
        for i in range(1,11):
            areas = driver.find_element_by_xpath(f'/html/body/div[2]/div/div[4]/article/div[2]/ul[2]/li[{i}]/div[2]/div/ul/li[1]/span[2]/a')
            if x in areas.text:
                regex = r'[^\d]+'
                match = re.findall(regex, titles[0+(i-1)*5].text)
                if match[0] == match [-1]:
                    print(match[0])
                else:
                    print(match[0],match[1])
                pf(p)
    else:
        work = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/article/div[2]/div[3]/div/div[1]/span[1]')
        w = int(work.text)
        if w%10 == 0:
            for i in range(1,11):
                areas = driver.find_element_by_xpath(f'/html/body/div[2]/div/div[4]/article/div[2]/ul[2]/li[{i}]/div[2]/div/ul/li[1]/span[2]/a')
                if x in areas.text:
                    regex = r'[^\d]+'
                    match = re.findall(regex, titles[0+(i-1)*5].text)
                    if match[0] == match [-1]:
                        print(match[0])
                    else:
                        print(match[0],match[1])
                    pf(p)
        else:
            for i in range(1,w%10+1):
                areas = driver.find_element_by_xpath(f'/html/body/div[2]/div/div[4]/article/div[2]/ul[2]/li[{i}]/div[2]/div/ul/li[1]/span[2]/a')
                if x in areas.text:
                    regex = r'[^\d]+'
                    match = re.findall(regex, titles[0+(i-1)*5].text)
                    if match[0] == match [-1]:
                        print(match[0])
                    else:
                        print(match[0],match[1])
                    pf(p)
    if page <= p*2:
        if nextpages[0].text == nextpages[3].text:
            actions.click(nextpages[0])
            actions.perform()
        else:
            actions.click(nextpages[2])
            actions.perform()
    else:
        break
driver.quit()