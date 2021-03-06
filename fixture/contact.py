from model.contact import Contact



class ContactHelper:
    def __init__(self, app):
        self.app = app


    def create(self, contact):
        wd = self.app.wd
        # fill contact page
        self.open_contact_page()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        # submit creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page_contact()


    def return_to_home_page_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()


    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith ("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()



    def delete(self):
        wd = self.app.wd
        # fill contact page
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()


    def edit(self, contact):
        wd = self.app.wd
        # fill contact page
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("update").click()
        self.return_to_home_page_contact()


    def count_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        # init group creation
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        contacts = []
        for element in wd.find_elements_by_xpath("//tr[./td]"):
            id = element.find_element_by_name("selected[]").get_attribute("id")
            firstname = element.find_elements_by_tag_name("td")[2].text
            lastname = element.find_elements_by_tag_name("td")[1].text
            contacts.append(Contact(id=id, firstname=firstname, lastname=lastname))
        return contacts

