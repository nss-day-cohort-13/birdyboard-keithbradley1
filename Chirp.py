
class Chirp():
    """
    Contain data for a single line item.
    Static Property:
        next_private_chirp_id   incrementing id for next created private chirp
        next_public_chirp_id   incrementing id for next created public chirp
    """

    next_private_chirp_id = 1
    next_public_chirp_id = 1

    def __init__(self, name, message):
        """
        Store values for new chirp and increment next id
        Arguments:
            name    the name of the chrip
            message   the message of the chirp
        """
        self.name = name
        self.message = message
        self.id = Chirp.next_private_chirp_id
        Chirp.next_private_chirp_id += 1


    def __init__(self, name, user_id, message):
        """
        Store values for new chirp and increment next id
        Arguments:
            name    the name of the chrip
            message   the message of the chirp
        """
        self.name = name
        self.message = message
        self.id = Chirp.next_public_chirp_id
        Chirp.next_public_chirp_id += 1