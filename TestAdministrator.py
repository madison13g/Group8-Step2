import unittest
from Person.administrator import *

class TestAdmin(unittest.TestCase):
    @classmethod
    def setUpClass(Admin):
        print('set up Admin')
    
    def setUp(self):
        self.t1 = Admin('amanatullah', 'TA533', 'A13')
        self.t2 = Admin('Dan', 'password3', 'A1')
        
    def test_displayUser(self):
        self.assertEqual(self.t1.displayUser(), 'Username: amanatullah Admin code: A13')
        self.assertEqual(self.t2.displayUser(), 'Username: Dan Admin code: A1')
        self.assertIsNotNone(self.t1.displayUser)
        self.assertIsNotNone(self.t2.displayUser)
    
    def test_displayCount(self):
        self.assertEqual(self.t1.displayCount(), 'There are 17 users')
        self.assertEqual(self.t2.displayCount(), 'There are 17 users')
        self.assertIsNotNone(self.t1.displayCount)
        self.assertIsNotNone(self.t2.displayCount)
        
    def tearDown(self):
        print('Testing finished')
        
    @classmethod
    def tearDownClass(Post):
        print('tear down Admin')