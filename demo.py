# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import unittest

class TestXueqiu(unittest.TestCase):


    def setUp(self) -> None:
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "chongqing"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_login(self):
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/user_profile_icon")
        el1.click()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_login")
        el2.click()
        el3 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_login_by_phone_or_others")
        el3.click()
        el4 = self.driver.find_element_by_id("com.xueqiu.android:id/register_phone_number")
        el4.send_keys("15600534760")
        el5 = self.driver.find_element_by_id("com.xueqiu.android:id/register_code")
        el5.send_keys("1234")
        el6 = self.driver.find_element_by_id("com.xueqiu.android:id/button_next")
        el6.click()

    def test_search(self):
        self.driver.find_element_by_id("tv_search").click()
        self.driver.find_element_by_id("search_input_text").send_keys("alibaba")
        self.driver.find_element_by_xpath("//*[@text='BABA']").click()
        assert float(self.driver.find_element_by_id("stock_current_price").text)<200

    def test_mi(self):
        self.driver.find_element_by_id("tv_search").click()
        self.driver.find_element_by_id("search_input_text").send_keys("xiaomi")
        self.driver.find_element_by_xpath("//*[@text='01810']/../../..//*[contains(@resource-id, '_btn')]").click()

    def tearDown(self) -> None:
        self.driver.quit()