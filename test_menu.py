import test
from menu import *

#################### menu tests ####################

class TestMenu(unittest.TestCase):
  '''test for menu options'''

  @classmethod
  def setUpClass(self):
    pass

  def test_new_user_account(self):
    bob = new_user('uuid', 'bob')

  def test_select_user(self):
    bob = select_user('uuid', 'bob')

  def test_view_chirps(self):
    chirp = view_chirps('uuid', 'chirp')

  def test_public_chirp(self):
    chirp = public_chirps('uuid', 'public_chirp')

  def test_private_chirp(self):
    chirp = private_chirps('uuid', 'private_chirp')

  def test_exit(self):
    exit = exit_menu('uuid', 'bob')


if __name__ == '__main__':
    unittest.main()