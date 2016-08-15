import test
from menu import *

#################### veiw chirps tests ####################

class TestViewChirps(unittest.TestCase):
  '''Chirps are separated into public and private chirps. Only the two users involved in a private chirp can see it in their Private Chirps section.'''

  @classmethod
  def setUpClass(self):
    pass

  def test_if_chirp_is_private(self):
    chirp = is_chirp_private('uuid', 'chirp')

  def test_if_chirp_is_public(self):
    chirp = is_chirp_public('uuid', 'chirp')

  def test_select_main_menu(self):
    selection = select_main_menu()


if __name__ == '__main__':
    unittest.main()