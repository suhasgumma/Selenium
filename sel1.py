import unittest
import time

from selenium import webdriver

class TestCase1(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/Users/suhasgumma/Desktop/Selenium/chromedriver 3')
        # time.sleep(10)
        self.addCleanup(self.browser.close)
    

    def testPageTitle(self):
        
        self.browser.get('http://www.google.com')

        self.assertIn('Google', self.browser.title)
    

class TestCase2(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/Users/suhasgumma/Desktop/Selenium/chromedriver 3')
        self.addCleanup(self.browser.close)
    
    def testPageTitle(self):
        self.browser.get('http://www.google.com')

        self.assertTrue('Po' in self.browser.title)
    
    

if __name__ == '__main__':
    unittest.main()