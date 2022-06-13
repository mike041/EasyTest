"""
@version: python 3.6.3
@author: xiaomai
@software: PyCharm
@file: __init__.py
@Site:
@time: 2022.05.26
"""

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from pageobject.page import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find(element, timeout, poll_frequency=0.5):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, timeout, poll_frequency)
    element = wait.until(EC.presence_of_element_located(By.ID, element))
    try:
        driver.find_element(value=element)
    except WebDriverException:
        pass
