from selenium import webdriver
from selenium.webdriver.chrome import service as ch
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import key
import time

moodle_url = "https://ict-i.el.kyutech.ac.jp/login/index.php"
moodle_user = key.MOODLE_USERNAME
moodle_pass = key.MOODLE_PASSWORD


def scraping_data():
    elms = []
    options = Options()
    options.add_argument('--headless')
    chrome_service = ch.Service("chromedriver/chromedriver.exe")
    browser = webdriver.Chrome(service=chrome_service, options=options)
    browser.implicitly_wait(10)
    browser.get(moodle_url)
    time.sleep(1)
    browser.find_element(by=By.NAME, value="j_username").send_keys(moodle_user)
    time.sleep(1)
    browser.find_element(by=By.NAME, value="j_password").send_keys(moodle_pass)
    time.sleep(1)
    browser.find_element(by=By.NAME, value="_eventId_proceed").click()
    element_contents = browser.find_elements(
        by=By.CSS_SELECTOR, value="div.w-100.event-name-container.text-truncate.line-height-3 > a")

    for element in element_contents:
        text = element.get_attribute("aria-label")
        elms.append(text)
    time.sleep(2)
    browser.find_element(by=By.ID, value="action-menu-toggle-1").click()
    time.sleep(2)
    browser.find_element(by=By.ID, value="actionmenuaction-6").click()
    time.sleep(2)
    browser.quit()
    return elms


tasks = scraping_data()
for task in tasks:
    print(task)
