# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSmokeTest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_homepage(self):
    self.driver.get("https://qrbriggs-byui.github.io/cse270-course/teton/1.5/index.html")
    self.driver.set_window_size(1294, 1392)
    assert self.driver.find_element(By.LINK_TEXT, "Join Us!").text == "Join Us!"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1 > h4")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2 > h4")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight3 > h4")
    assert len(elements) > 0
  
  def test_adminpage(self):
    self.driver.get("https://qrbriggs-byui.github.io/cse270-course/teton/1.5/index.html")
    self.driver.set_window_size(1294, 1392)
    self.driver.find_element(By.LINK_TEXT, "Admin").click()
    elements = self.driver.find_elements(By.ID, "username")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "username").send_keys("bob")
    self.driver.find_element(By.ID, "password").send_keys("cob")
    self.driver.find_element(By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".errorMessage")
    assert len(elements) > 0
  
  def test_directorypage(self):
    self.driver.get("https://qrbriggs-byui.github.io/cse270-course/teton/1.5/index.html")
    self.driver.set_window_size(1294, 1392)
    self.driver.find_element(By.LINK_TEXT, "Directory").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"
    self.driver.find_element(By.ID, "directory-list").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"
  
  def test_joinpage(self):
    self.driver.get("https://qrbriggs-byui.github.io/cse270-course/teton/1.5/index.html")
    self.driver.set_window_size(1294, 1392)
    self.driver.find_element(By.LINK_TEXT, "Join").click()
    elements = self.driver.find_elements(By.NAME, "fname")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "fname").click()
    self.driver.find_element(By.NAME, "fname").send_keys("asdf")
    self.driver.find_element(By.NAME, "lname").click()
    self.driver.find_element(By.NAME, "lname").send_keys("asdf")
    self.driver.find_element(By.NAME, "bizname").click()
    self.driver.find_element(By.NAME, "bizname").send_keys("asdf")
    self.driver.find_element(By.NAME, "biztitle").click()
    self.driver.find_element(By.NAME, "biztitle").send_keys("asdf")
    self.driver.find_element(By.NAME, "submit").click()
    elements = self.driver.find_elements(By.NAME, "email")
    assert len(elements) > 0
  