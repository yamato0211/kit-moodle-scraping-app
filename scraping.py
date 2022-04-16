from selenium import webdriver
from selenium.webdriver.chrome import service as ch
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from key import MOODLE_PASSWORD, MOODLE_USERNAME

moodle_url = "https://ict-i.el.kyutech.ac.jp/login/index.php"
moodle_user = MOODLE_USERNAME
moodle_pass = MOODLE_PASSWORD


def scraping_data():
    elms = []
    options = Options()
    options.add_argument('--headless')
    chrome_service = ch.Service("chromedriver/chromedriver.exe")
    browser = webdriver.Chrome(service=chrome_service, options=options)
    browser.implicitly_wait(7)
    browser.get(moodle_url)
    browser.find_element(by=By.NAME, value="j_username").send_keys(moodle_user)
    browser.find_element(by=By.NAME, value="j_password").send_keys(moodle_pass)
    browser.find_element(by=By.NAME, value="_eventId_proceed").click()
    element_contents = browser.find_elements(
        by=By.CSS_SELECTOR, value="div.w-100.event-name-container.text-truncate.line-height-3 > a")

    for element in element_contents:
        text = element.get_attribute(
            "aria-label").replace('の提出期限が近づいています', '').replace(' 活動', '')
        elms.append(text)
    browser.find_element(by=By.ID, value="action-menu-toggle-1").click()
    browser.find_element(by=By.ID, value="actionmenuaction-6").click()
    browser.quit()
    return elms
