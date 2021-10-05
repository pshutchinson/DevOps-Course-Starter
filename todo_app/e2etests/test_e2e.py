import os
import pytest

from threading import Thread
from todo_app import app
from todo_app.services import mongo
from dotenv import find_dotenv, load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope='module')
def driver():
    opts = webdriver.ChromeOptions()
    opts.add_argument('--headless')
    opts.add_argument('--no-sandbox')
    opts.add_argument('--disable-dev-shm-usage')
 
    with webdriver.Chrome('/usr/bin/chromedriver', options=opts) as driver:
        yield driver

@pytest.fixture(scope="module")
def app_with_temp_board():
    
    file_path = find_dotenv('.env')

    load_dotenv(file_path, override=True)
    
    # construct the new application
    application = app.create_app()

    with application.app_context():
        create_board('Test')
        os.environ['MONGO_DB'] = 'Test'

    # start the app in its own thread.
    thread = Thread(target=lambda:

    application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    
    yield application
    
    # Tear Down
    thread.join(1)

def create_board(name):
    mongo.create_board(name)

def test_task_journey(driver, app_with_temp_board):
    try:
        driver.get('http://localhost:5000/')
        
        elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "title")))
        
        assert driver.title == 'To-Do App'

        elem.send_keys("A Test Item")
        elem = driver.find_element_by_name("submit")
        elem.send_keys(Keys.RETURN)

        elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Start")))
        elem.send_keys(Keys.RETURN)

        elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Complete")))
        elem.send_keys(Keys.RETURN)
    
        elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Reset")))
    finally:
        driver.close()