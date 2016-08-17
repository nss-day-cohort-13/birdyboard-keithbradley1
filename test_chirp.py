import unittest
from Chirp import *

#################### new chirp tests ####################

class TestChirp(unittest.TestCase):

    def test_create_chirp(self):
        chirp = Chirp('hi', 'hi there')

        self.assertNotEqual(chirp.id, 0)
        self.assertEqual(chirp.name, 'hi')
        self.assertEqual(chirp.message, 'hi there')


    def test_next_product_id_increments(self):
        Chirp.next_chirp_id = 1

        chirp = Chirp('hi', 'hi there')

        self.assertEqual(Chirp.next_chirp_id, 2)


if __name__ == '__main__':
    unittest.main()