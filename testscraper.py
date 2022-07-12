import unittest
import justry
import json
from justry import Scraper

class TestScraper(unittest.TestCase): #TestCase will allow to access a lot of testing capabilities within this class.
    
    def test_create_json(self):
        dicti = {'a': 1, 'b': 2}
        webscraper = Scraper()
        webscraper.create_json(dicti, 'test.json')

        new_var = json.load(open('test.json'))
        self.assertDictEqual(dicti, new_var)


class TestIntegrationScraper(unittest.TestCase):

    def test_scraping(self):
        webscraper = Scraper()
        webscraper.fetch_community('gaming')
        new_var = json.load(open('gaming.json'))
        self.assertEqual(type(new_var), dict)
        self.assertGreater(len(new_var), 1)
        self.assertSetEqual(set(list(new_var.values())[0].keys()), {'Title', 'Comment', 'ImageSource', 'ID', 'Vote'})
