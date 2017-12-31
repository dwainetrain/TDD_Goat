from selenium import webdriver
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
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')



# He decides to give it a whirl and enters in his first to do item
# "Everything"

# He presses enter and it appears in a list below

# The text entry remains, and he sees he can add more items to the todo List
# He adds his next item "And then Some"

# But when he wakes up tomorrow, will the list still be there?

# He notices that there's a unique url and that
# there's helper text which explains that his list will persist

# He refreshes the browser to test
# All is good, and he's got a lot of work to do tomorrow

browser.quit()
