from easy_io import *
from Chirp import *
from User import *
from Conversation import *

class Birdyboard(object):
  '''
  All the logic for interface of users and chirps
  creating a new user, creating a new private chirp, creating a new public chirp, viewing all chirps, selecting an active user.
  Static Properties:
    user_filename - file storing all user data
    select_active_user - method to select a user
    new_chirps_filename - file storing all new public chirp data
    create_a_reply - method that creates a reply stores active chirps and replies in a converation dictionary
    view_chirps_filename - method to view all chirps
    conversation_filename - file storage for all converstaions
    exit_birdyboard - method to exit birdyboard
  '''
  user_filename = 'user.dat'
  chirps_filename = 'chirps.dat'
  conversation_filename = 'conversation_filename.dat'

  def __init__(self):
    '''
    Initialize Birdyboard, deserialize data files.
    '''

    self.users = deserialize(Birdyboard.user_filename, dict())
    self.chirps = deserialize(Birdyboard.chirps_filename, dict())

    User.next_user_id = len(self.users) + 1
    Chirp.next_chirp_id = len(self.chirps) + 1

    self.active_user_id = 0
    self.active_chirp_id = 0



  def create_new_user(self, name, screen_name):
    """
    Add a new user to the user dictionary
    Arguments:
        name        new user's name
        screen_name     new user's screen name
    """

    new_user = User(name, screen_name)
    self.users[new_user.id] = new_user
    serialize(self.users, Birdyboard.user_filename)
    return new_user


  def create_new_chirp(self, message):
    """
    Add a new chrip to the chirp dictionary
    Arguments:
        chirp_title        new chirps's title
        message     new chirps's message
        user_id     new chirps's user_id
    """

    new_chirp = Chirp(message, user_id)
    self.chirps[new_chirp.id] = new_chirp
    serialize(self.chirps, Birdyboard.chirp_filename)

  def select_active_user(self, user_id):
      """
      Set active user and active order if exists for user
      Arguments:
          user_id   the id of the active user
      """

      self.active_user_id = user_id

  def print_all_chrips(chirp_id, user_id):
    '''
    show all chirps
    Arguments:
      chirp_id
      user_id
    '''
    print_all_chrips = Chirp

























