import unittest
from Content.topic import *

class TestTopic(unittest.TestCase):
    @classmethod
    def setUpClass(Topic):
        print('set up Topic')
        
    def setUp(self):
        self.t1 = Topic('Quizzes','Amethyst')
        self.t2 = Topic('Winter break','Madison')
        
    def test_tag(self):
        self.t1.tag = 'MDS'
        self.t2.tag = 'MDS'
        self.assertEqual(self.t1.tag, 'MDS')
        self.assertEqual(self.t2.tag, 'MDS')
        self.assertIsNotNone(self.t1.tag)
        self.assertIsNotNone(self.t2.tag)
    
    def test_show(self):
        self.assertIsNotNone(self.t1.show())
        self.assertIsNotNone(self.t2.show())
        self.assertEqual(self.t1.show(), f'Topic id: 11 Topic name: Quizzes')
        self.assertEqual(self.t2.show(), f'Topic id: 12 Topic name: Winter break')
        
    def tearDown(self):
        print('Testing finished')
        
    @classmethod
    def tearDownClass(Topic):
        print('tear down Topic')
