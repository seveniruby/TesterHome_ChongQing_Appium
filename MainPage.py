from SearchPage import SearchPage


class MainPage(object):
    def __init__(self, driver):
        self.driver=driver

    def gotoSearch(self):
        self.driver.find_element_by_id("tv_search").click()
        return SearchPage(self.driver)
    def gotoProfile(self):
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/user_profile_icon")
        el1.click()
