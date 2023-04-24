import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

website = 'https://it.pracuj.pl/'
path = 'C:\\chromedriver.exe'

service = Service(path)
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chr_options)
driver.get(website)

driver.maximize_window()

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Akceptuj wszystkie')]"))).click()
time.sleep(2)

python_filter = driver.find_element(By.XPATH, '//label[@data-test="radio-mostPopular-Python-label"]')
python_filter.click()
time.sleep(2)

remote_filter = driver.find_element(By.XPATH, '//label[@data-test="checkbox-locationsAndRemoteWork-rw-label"]')
remote_filter.click()
time.sleep(2)

junior_filter = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div[1]/div/div[2]/form/div[5]/div[2]/ul/li[3]/label')
junior_filter.click()
time.sleep(2)

titles = driver.find_elements(By.XPATH, '//h3[@data-test="offer-title"]')
for title in titles:
    print(title.text)


# driver.quit()



