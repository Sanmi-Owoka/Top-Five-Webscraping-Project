from unittest import TestCase
from web_scrape import WebScrape
from web_processing import WebProcess
from web_word_counter import WordCounter



class TestTask(TestCase):
    def setUp(self):
        self.web_scrape = WebScrape()
        self.web_process = WebProcess()
        self.count = WordCounter()

    def test_web_scrape(self):
        result =  self.web_scrape.scrape("https://www.python.org")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertNotIsInstance(result, dict)
        self.assertNotIsInstance(result, list)
        self.assertTrue(result)
        self.assertGreater(len(result), 1)

    def test_web_processing(self):
        result = self.web_process.text_process("python software is a 1 2 3 4 class")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertNotIsInstance(result, dict)
        self.assertNotIsInstance(result, dict)
        self.assertTrue(result)
        self.assertEqual(result, ["Python" , "Software", "Class"])

    def test_web_counter(self):
        result = self.count.word_counter(["python", "software", "train", "sound", "music", "punch", "dance"])
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertNotIsInstance(result, list)
        self.assertNotIsInstance(result, str)
        self.assertEqual(len(result), 7)
        self.assertEqual(result, {"python": 1, "software": 1, "train" : 1, "sound" : 1, "music" : 1, "punch" : 1, "dance" : 1})
        self.assertEqual(sum(list(result.values())), 7)
        self.assertEqual(list(result.keys()), ["python", "software", "train", "sound", "music", "punch", "dance"])

    def tearDown(self):
        self.web_scrape = None
        self.web_process = None
        self.count = None
    
       








