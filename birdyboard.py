from Chirps import *
from User import *

class Birdyboard(object):
  '''
  All the logic for interface of users and chirps
  creating a new user, creating a new private chirp, creating a new public chirp, viewing all chirps, selecting an active user.
  Static Properties:
    user_filename - file storing all user data
    new_public_chirps_filename - file storing all new public chirp data
    new_private_chirps_filename - file storing all new private chirp data
    view_chirps_filename - function to view all chirps
    select_active_user - function to select a user
    conversation_filename - file storage for all converstaions
  '''
  user_filename = 'user.dat'
  new_public_chirps_filename = 'public_chirps.dat'
  new_private_chirps_filename = 'private_chirps.dat'
  view_chirps_filename = 'view_chirps.dat'
  select_active_user_filename = 'select_active_user.dat'
  conversation_filename = 'conversation_filename.dat'

  def __init__(self):
    '''
    Initialize Birdyboard, deserialize data files.
    '''

    self.users = deserialize(Birdyboard.user_filename, dict())
    self.new_public_chirps = deserialize(Birdyboard.new_public_chirps_filename, dict())
    self.new_private_chirps = deserialize(Birdyboard.new_private_chirps_filename, dict())
    self.view_chirps = deserialize(Birdyboard.view_chirps_filename, dict())
    self.select_active_user = deserialize(Birdyboard.select_active_user_filename, dict())
    self.conversation = deserialize(Birdyboard.conversation_filename, dict())




























