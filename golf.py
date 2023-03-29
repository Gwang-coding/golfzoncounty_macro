from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import schedule
import time
import datetime
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
driver = webdriver.Chrome(
    "/Users/jk/Desktop/chromedriver", options=chrome_options)

chrome_options.add_experimental_option("detach", True)
wait = WebDriverWait(driver, 5)


def click():
    driver.refresh()
    driver.implicitly_wait(5)

    driver.find_element(By.CLASS_NAME, "swiper-button-next").click()
    driver.find_element(By.CLASS_NAME, "swiper-button-next").click()

    wait.until(EC.presence_of_element_located((By.ID, 20230423)))
    driver.find_element(By.ID, 20230423).click()

    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#choice-c > ul > li:nth-child(3) > div > label > div')))
    driver.find_element(
        By.XPATH, "//dt[text()[contains(.,'08:')]]").click()


def test():
    now = datetime.datetime.now()
    print(now)


def sta():
    log()
    schedule.every(1).seconds.do(test)
    schedule.every().day.at("09:00").do(click)

    while True:
        schedule.run_pending()
        time.sleep(1)


def log():
    id = driver.find_element(By.CSS_SELECTOR, "#loginID")
    id.click()
    id.send_keys("id")

    pw = driver.find_element(By.CSS_SELECTOR, "#loginPW")
    pw.click()
    pw.send_keys("pw")

    login = driver.find_element(By.CLASS_NAME, "btn-type.mb10")
    login.click()


driver.get("http://www.golfzoncounty.com/reserve/main?gc_no=222&area_code=2")
sta()
