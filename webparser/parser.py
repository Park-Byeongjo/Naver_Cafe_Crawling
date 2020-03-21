from selenium import webdriver
from parsed_data.modules.cafe_crawl import parse_cafe
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webparser.settings")
django.setup()
from parsed_data.models import CafeData

if __name__ == '__main__':
    p_list = '컴퓨터'
    c_time = '00:00'
    # Download chromedriver location setting
    driver = webdriver.Chrome('/Users/byeun/Downloads/chromedriver')
    driver.implicitly_wait(3) # Delay for web loading
    try:
        data = parse_cafe(driver, p_list, c_time)
        for t in data:
            CafeData(title=t.title, link=t.link, time=t.time).save()
    # the end of work
    finally:
        driver.quit()
