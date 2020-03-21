from selenium import webdriver
from bs4 import BeautifulSoup
import time

# crawling data format
class article_data:
    def __init__(self, title, link, time):
        # title is article
        # link is article link
        # time is article time
        self.title = title
        self.link = link
        self.time = time

# cafe-menu search and page change
def parse_cafe(driver, query, data_time):
    # query is cafe-menu / data_time is the time chosen
    # url access
    driver.get("https://cafe.naver.com/joonggonara")
    time.sleep(1)# wait for page loading
    # find cafe-menu and click
    driver.find_element_by_partial_link_text(query).click()
    time.sleep(1)
    driver.switch_to.frame('cafe_main')

    data = []  # data storage

    t = True
    while t:
        # page crawl
        t = page_cafe(driver, data, data_time)
        if t != '다음':
            t = False

    return data

# change pages until find the data_time want
def page_cafe(driver, data, data_time):
    # data is storing data for article / data_time is time chosen
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # hf is page navigation crawl
    hf = soup.select('div.prev-next > a')
    count = 15  # count is maximum number of article
    for t in hf:
        if count < 14:
            return count
        elif t.text == '다음' :
            driver.find_element_by_link_text(t.text).click()
            return t.text
        elif t.text == '이전':
            continue
        else:
            driver.find_element_by_link_text(t.text).click()
            count = crawling_page(driver, data, data_time)

# page title and link and time crawling
def crawling_page(driver, data, data_time):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # article html format crawl
    article = soup.select('div:nth-child(6) > table > tbody > tr > td > div > div > a.article')
    # article time html format crawl
    article_time = soup.select('div:nth-child(6) > table > tbody > tr > td.td_date')
    count = 0
    for t in article:
        ti = time_check(article_time[count], data_time)
        if ti is True:
            break
        else:
            data.append(article_data(t.text.strip(), t.get('href'), article_time[count].text))
            count += 1

    return count

# check until data_time
def time_check(cafe_time, data_time):
    if cafe_time.text.find(':') == -1 or cafe_time.text < data_time:
        t = True
    else :
        t = False
    return t