import unittest
from Person.user import *

class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(User):
        print('set up User')
    
    def setUp(self):
        self.t1 = User('madison13g', 'password1')
        self.t2 = User('amethyst1016', 'password2')
        
    def test_displayUser(self):
        self.assertEqual(self.t1.displayUser(), 'Username: madison13g')
        self.assertEqual(self.t2.displayUser(), 'Username: amethyst1016')
        self.assertIsNotNone(self.t1.displayUser)
        self.assertIsNotNone(self.t2.displayUser)
        
    def test_password(self):
        self.t1.password = 'password123'
        self.t2.password = 'password123'
        self.assertEqual(self.t1.password, 'password123')
        self.assertEqual(self.t2.password, 'password123')
        self.assertIsNotNone(self.t1.password)
        self.assertIsNotNone(self.t2.password)
        
    def tearDown(self):
        print('Testing finished')
        
    @classmethod
    def tearDownClass(Post):
        print('tear down User')