# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "chongqing"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["autoGrantPermissions"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)

el1 = driver.find_element_by_id("com.xueqiu.android:id/user_profile_icon")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/tv_login")
el2.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/tv_login_by_phone_or_others")
el3.click()
el4 = driver.find_element_by_id("com.xueqiu.android:id/register_phone_number")
el4.send_keys("15600534760")
el5 = driver.find_element_by_id("com.xueqiu.android:id/register_code")
el5.send_keys("1234")
el6 = driver.find_element_by_id("com.xueqiu.android:id/button_next")
el6.click()

driver.quit()