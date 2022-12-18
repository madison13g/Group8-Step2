import unittest
from Content.post import *

class TestPost(unittest.TestCase):
    @classmethod
    def setUpClass(Post):
        print('set up Post')
    
    def setUp(self):
        self.t1 = Post(10,'There are four quizzes next week.', 'Amethyst')
        self.t2 = Post(10,'Winter break is coming!', 'Madison')
        
    def test_add_comment(self):
        self.t1.add_comment('Review!!!')
        self.t2.add_comment('Yeaaaaa!')
        self.assertEqual(self.t1.comments, ['Review!!!'])
        self.assertEqual(self.t2.comments, ['Yeaaaaa!'])
        self.assertIsNotNone(self.t1.comments)
        self.assertIsNotNone(self.t2.comments)
    
    def test_add_like(self):
        self.t1.add_like()
        self.t2.add_like(2)
        self.assertEqual(self.t1.like, 1)
        self.assertEqual(self.t2.like, 2)
        self.assertIsNotNone(self.t1.like)
        self.assertIsNotNone(self.t2.like)
        
    def tearDown(self):
        print('Testing finished')
        
    @classmethod
    def tearDownClass(Post):
        print('tear down Post')