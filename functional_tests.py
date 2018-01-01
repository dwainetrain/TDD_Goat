from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Jacob visits the site
        self.browser.get('http://localhost:8000')

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
        input.send_keys('Do Everything')

        # He presses enter and it appears in a list below
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Do Everything' for row in rows)
        )

        # The text entry remains, and he sees he can add more items to the todo List
        # He adds his next item "And then Some"

        # But when he wakes up tomorrow, will the list still be there?

        # He notices that there's a unique url and that
        # there's helper text which explains that his list will persist

        # He refreshes the browser to test
        # All is good, and he's got a lot of work to do tomorrow

        self.fail('Finish the test!')
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')







browser.quit()
