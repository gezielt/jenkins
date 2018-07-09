import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("D:\oldpc\workpc\d\pythonlabs/chromedriver.exe")

    def test_search_in_python_org(self):
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get("https://portal.iba.by/web/guest/home?p_p_id=com_liferay_login_web_portlet_LoginPortlet&p_p_lifecycle=0&p_p_state=maximized&saveLastPath=false")
        element = driver.find_element_by_id("_com_liferay_login_web_portlet_LoginPortlet_login")
        element.send_keys("uyuruts")
        element = driver.find_element_by_id("_com_liferay_login_web_portlet_LoginPortlet_password")
        element.send_keys("6490375Ira")
        element.submit()
        element = driver.find_element_by_xpath("//i[@class='fa fa-caret-down']").click()
        element = driver.find_element_by_xpath("//a[@href='https://portal.iba.by/web/guest/poisk-sotrudnikov']").click()
        element = driver.find_element_by_xpath("//input[@placeholder='NAME *']")
        element.send_keys("Yuruts")
        element = driver.find_element_by_xpath("//input[@placeholder='DEPARTMENT']")
        element.send_keys("")
        element = driver.find_element_by_xpath("//button[@class='btn btn-primary btn-lg']").click()
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
