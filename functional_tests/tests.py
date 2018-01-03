from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#import unittest


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    # helper method, refactoring to remove repeated code accessing
    # the rows
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
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
        time.sleep(1)
        self.check_for_row_in_list_table('1: Do Everything')

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Do Everything', [row.text for row in rows])

        # The text entry remains, and he sees he can add more items to the todo List
        # He adds his next item "And then Some"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('And then some')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        #self.assertIn(
        #    '2: And then some',
        #    [row.text for row in rows]
        #)

        # The page updates again, and now shows both items on his lists
        self.check_for_row_in_list_table('1: Do Everything')
        self.check_for_row_in_list_table('2: And then some')

        # But when he wakes up tomorrow, will the list still be there?

        # He notices that there's a unique url and that
        # there's helper text which explains that his list will persist

        # He refreshes the browser to test
        # All is good, and he's got a lot of work to do tomorrow

        self.fail('Finish the test!')


#browser.quit()
