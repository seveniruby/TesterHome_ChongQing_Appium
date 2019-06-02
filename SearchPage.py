
class SearchPage(object):
    def __init__(self, driver):
        self.driver=driver
    def search(self, keyword):
        self.driver.find_element_by_id("search_input_text").send_keys(keyword)
        return self

