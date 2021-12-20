import unittest
import Lesson7_Task1

class NameTestCase(unittest.TestCase):
    def test_favorite_movie(self):
        full = Lesson7_Task1.favorite_movie('My name')
        full2 = Lesson7_Task1.favorite_movie('MY NAME')
        self.assertEqual(full, 'My name')
        self.assertEqual(full2, 'MY NAME')

unittest.main()