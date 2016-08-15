class User:
    """
    Creates a new user with the users information and increments the static
    variable to change the customer's id
    """
    next_user_id = 1

    def __init__(self, name, screen_name):
        """
        __init__ function passes in varibles to store the information on the class
        """
        self.name = name
        self.screen_name = screen_name
        self.id = User.next_user_id
        User.next_user_id += 1