import test
from menu import *

#################### new user tests ####################

class TestNewUser(unittest.TestCase):
  '''test for new user creation'''

  @classmethod
  def setUpClass(self):
    pass

  def test_new_user_account(self):
    bob = new_user('uuid', 'bob')
  def test_enter_full_name(self):
    bob = enter_full_name('uuid', 'bob')
  def test_enter_screen_name(self):
    bob = enter_screen_name('uuid', 'bob')


if __name__ == '__main__':
    unittest.main()