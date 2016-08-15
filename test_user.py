import unittest
from User import *

#################### new user tests ####################

class TestUser(unittest.TestCase):

    def test_create_user(self):
        user = User('Jim Jones',
                        'drink_koolaid')

        self.assertNotEqual(user.id, 0)
        self.assertEqual(user.name, 'Jim Jones')
        self.assertEqual(user.screen_name, 'drink_koolaid')

    def test_next_user_id_increments(self):
        User.next_user = 1

        User('Jim Jones',
                 'drink_koolaid')

        User('Joan Jett',
                 'bad_reputation')

        self.assertEqual(User.next_user_id, 4)



if __name__ == '__main__':
    unittest.main()