# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class alert_check:
    def __init__(self, browser):
        self.browser = browser
    def submission_Check(self,browser):
        alert = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert"))
        )
        return alert.text