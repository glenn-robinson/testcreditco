import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestTestCreditCo():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testCreditCo(self):
    self.driver.get("https://taxcreditco.com/")
    self.driver.set_window_size(1600, 1000)
    self.driver.find_element(By.LINK_TEXT, "Contact").click()
    self.driver.find_element(By.ID, "firstname-3a877d85-0e59-43b4-9079-9eb8b5306c04").click()
    self.driver.find_element(By.ID, "firstname-3a877d85-0e59-43b4-9079-9eb8b5306c04").send_keys("test")
    self.driver.find_element(By.ID, "jobtitle-3a877d85-0e59-43b4-9079-9eb8b5306c04").click()
    self.driver.find_element(By.ID, "jobtitle-3a877d85-0e59-43b4-9079-9eb8b5306c04").send_keys("test")
    self.driver.find_element(By.ID, "email-3a877d85-0e59-43b4-9079-9eb8b5306c04").click()
    self.driver.find_element(By.ID, "email-3a877d85-0e59-43b4-9079-9eb8b5306c04").send_keys("test@test.com")
    self.driver.find_element(By.ID, "phone-3a877d85-0e59-43b4-9079-9eb8b5306c04").send_keys("555-666-7777")
    self.driver.find_element(By.ID, "company-3a877d85-0e59-43b4-9079-9eb8b5306c04").click()
    self.driver.find_element(By.ID, "company-3a877d85-0e59-43b4-9079-9eb8b5306c04").send_keys("Test")
    self.driver.find_element(By.ID, "state-3a877d85-0e59-43b4-9079-9eb8b5306c04").click()
    self.driver.find_element(By.ID, "state-3a877d85-0e59-43b4-9079-9eb8b5306c04").send_keys("CA")
    self.driver.find_element(By.ID, "message-3a877d85-0e59-43b4-9079-9eb8b5306c04").click()
    self.driver.find_element(By.ID, "message-3a877d85-0e59-43b4-9079-9eb8b5306c04").send_keys("This is a test. Please ignore")
    self.driver.find_element(By.CSS_SELECTOR, ".hs-button").click()
  
