# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 14:45:50 2021

@author: Mosa
"""

from pages import form
from pages import alert
from selenium import webdriver



#main working
driver = webdriver.Chrome('chromedriver')  

driver.get('http://formy-project.herokuapp.com/form')

form_obj = form.submit(driver)
form_obj.submit_form(driver)

alert_obj = alert.alert_check(driver)

msg = alert_obj.submission_Check(driver)


assert msg=="The form was successfully submitted!"


driver.quit()


