import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_job_titles():
    # driver setting
    website = 'https://it.pracuj.pl/'
    path = 'C:\\chromedriver.exe'

    service = Service(path)
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service, options=chr_options)
    driver.get(website)

    driver.maximize_window()

    # accept cookies
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Akceptuj wszystkie')]"))).click()
    time.sleep(1)

    # filtering by programming language
    python_filter = driver.find_element(By.XPATH, '//label[@data-test="radio-mostPopular-Python-label"]')
    python_filter.click()
    time.sleep(1)

    # filtering by remote work
    remote_filter = driver.find_element(By.XPATH, '//label[@data-test="checkbox-locationsAndRemoteWork-rw-label"]')
    remote_filter.click()
    time.sleep(1)

    # filtering by offers for junior
    junior_filter = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div[1]/div/div[2]/form/div[5]/div[2]/ul/li[3]/label')
    junior_filter.click()
    time.sleep(1)

    # saving the data of offers in json file
    titles = driver.find_elements(By.XPATH, '//h3[@data-test="offer-title"]')
    companies = driver.find_elements(By.XPATH, '//span[@data-test="company-name"]')
    links = driver.find_elements(By.XPATH, '//a[@data-test="offer-link"]')
    dates = driver.find_elements(By.CSS_SELECTOR, '.JobOfferstyles__FooterText-sc-1rq6ue2-22')
    offers = []
    

    for title, company, link, date in zip(titles, companies, links, dates):
        offer = {'offer_title': title.text, 'company_name': company.text, 'link': link.get_attribute('href'), 'date': date.text}
        offers.append(offer)

    data = {'offers': offers}

    with open('job_titles.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

    # close chrome browser
    # driver.quit()

    return offers




