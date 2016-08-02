import test
from menu import *

#################### select user tests ####################

class TestSelectUser(unittest.TestCase):
  '''Which user is chriping?'''

  @classmethod
  def setUpClass(self):
    pass

  def test_which_user_is_chirping(self):
    bob = which_user_is_chirping('uuid', 'bob')


if __name__ == '__main__':
    unittest.main()