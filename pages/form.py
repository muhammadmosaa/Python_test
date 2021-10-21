# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys

class submit:
    
    def __init__(self, browser):
        self.browser = browser
    def submit_form(self,browser):
        driver= browser
        first_name = driver.find_element_by_id('first-name')
        first_name.send_keys('mosa')
        
        last_name = driver.find_element_by_id('last-name')
        last_name.send_keys('Zahid')
        
        job_title = driver.find_element_by_id('job-title')
        job_title.send_keys('QA Engineer')
        
        grad_school = driver.find_element_by_id('radio-button-3')
        grad_school.click()
        
        male_sex = driver.find_element_by_id('checkbox-1')
        male_sex.click()
        
        driver.find_element_by_css_selector("option[value='1']").click()
        
        
        date = driver.find_element_by_id('datepicker')
        date.send_keys('01/02/2021')
        date.send_keys(Keys.RETURN)
        
        driver.find_element_by_css_selector(".btn.btn-lg.btn-primary").click()
