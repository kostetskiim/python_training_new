from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application():
    def __init__(self):
        self.wd = WebDriver()
        self.session = SessionHelper(self)
        self.wd.implicitly_wait(1)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    def destroy(self):
        wd = self.wd
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return  True
        except:
            return False