# Importing webdriver to load firefox
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # My wife has heard about a cool online to-do app. She goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notied the  page title and header mentioned to-do lists 
        self.assertIn('TO-DO', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away 

        # she types " Buy peacock feathers" into a text box

        # when she hits enter, the page updates, and now the pages lists 
        # 1. "Buy peacock feathers" as an item in a to-do list 
        # 
        # There is still a text box inviting her to add another item. when she enters another item the process repeats.
        # 
        # The site has generated a unique URL for her  and when she visits that URL , she noticed her to-do list are still there.

        # satisfied, she goes back to sleep
         
if __name__ == '__main__':
    unittest.main(warnings='ignore')