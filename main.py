import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    path = 'C:\\chromedriver.exe'
    service = Service(path)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def accept_cookies(driver):
    cookie_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Akceptuj wszystkie')]")))
    cookie_button.click()
    time.sleep(2)

def filter_jobs(driver):
    # Filtering by programming language
    python_filter = driver.find_element(By.XPATH, '//label[@data-test="radio-mostPopular-Python-label"]')
    python_filter.click()
    time.sleep(2)

    # Filtering by remote work
    remote_filter = driver.find_element(By.XPATH, '//label[@data-test="checkbox-locationsAndRemoteWork-rw-label"]')
    remote_filter.click()
    time.sleep(2)

    # Filtering by offers for junior
    junior_filter = driver.find_element(By.XPATH,
                                         '//*[@id="root"]/div[4]/div[1]/div[1]/div/div[2]/form/div[5]/div[2]/ul/li[3]/label')
    junior_filter.click()
    time.sleep(2)

def get_job_elements(driver):
    # Find job offer elements
    titles = driver.find_elements(By.XPATH, '//h3[@data-test="offer-title"]')
    companies = driver.find_elements(By.XPATH, '//span[@data-test="company-name"]')
    links = driver.find_elements(By.XPATH, '//a[@data-test="offer-link"]')
    dates = driver.find_elements(By.CSS_SELECTOR, '.JobOfferstyles__FooterText-sc-1rq6ue2-22')
    return titles, companies, links, dates

def create_offers_dict(titles, companies, links, dates):
    # Create dictionary
    offers = []
    for title, company, link, date in zip(titles, companies, links, dates):
        offer = {'offer_title': title.text, 'company_name': company.text, 'link': link.get_attribute('href'),
                 'date': date.text}
        offers.append(offer)
    return offers

def save_to_json(offers):
    # Save to json file
    data = {'offers': offers}
    with open('job_titles.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

def get_job_titles():
    # Set up Chrome driver
    website = 'https://it.pracuj.pl/'
    driver = setup_driver()
    driver.get(website)
    driver.maximize_window()

    accept_cookies(driver)

    filter_jobs(driver)

    titles, companies, links, dates = get_job_elements(driver)

    offers = create_offers_dict(titles, companies, links, dates)
    

    save_to_json(offers)

    # Close chrome browser
    # driver.quit()

    return offers
