from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
#import unittest

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    # helper method, refactoring to remove repeated code accessing
    # the rows

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)


    def test_can_start_a_list_for_one_user(self):
        # Jacob visits the site
        self.browser.get(self.live_server_url)

        # he sees that it's a fancy new to-do list
        # according to the page title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He decides to give it a whirl
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # and enters in his first to do item
        # "Everything"
        inputbox.send_keys('Do Everything')

        # He presses enter and it appears in a list below
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Do Everything')

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Do Everything', [row.text for row in rows])

        # The text entry remains, and he sees he can add more items to the todo List
        # He adds his next item "And then Some"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('And then some')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on his lists
        self.wait_for_row_in_list_table('1: Do Everything')
        self.wait_for_row_in_list_table('2: And then some')


    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Jacob starts a new to-do lists
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Do Everything')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Do Everything')


        # But when he wakes up tomorrow, will the list still be there?
        # He notices that there's a unique url and that
        jacob_list_url = self.browser.current_url
        self.assertRegex(jacob_list_url, '/lists/.+')

        # Now a new user, Francis, comes along to the site

        ## We use a new browser session to make sure that no information
        ## of Jacob's is coming through from cookies, etc.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits the home page. There is no sign of Jacob's
        # list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Do Everything', page_text)
        self.assertNotIn('And then some', page_text)

        # Francis starts a new list by entering a new item. He
        # is less interesting that Edith...
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, jacob_list_url)

        # Again, there is no trace of Jacob's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Do Everything', page_text)
        self.assertIn('And then some', page_text)

        # there's helper text which explains that his list will persist

        # They both refresh the browser to test
        # All is good, and they've got a lot of work to do tomorrow

        self.fail('Finish the test!')
