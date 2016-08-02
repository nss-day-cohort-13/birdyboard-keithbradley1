import test
from menu import *

#################### new chirp tests ####################

class TestNewChirp(unittest.TestCase):
  '''Users can chirp publicly or they can start a private chirp with another user.
'''

  @classmethod
  def setUpClass(self):
    pass

  def test_is new_chirp_public(self):
    bob = is_new_chirp_public('uuid', 'chirp')
  def test_is_new_chirp_private(self):
    chirp = is_new_chirp_private('uuid', 'chirp')
  def test_select_menu(self):
    menu = did_user_select_menu()
  def test_did_user_enter_text(self):
    text = did_user_enter_text('uuid', 'chirp')


if __name__ == '__main__':
    unittest.main()