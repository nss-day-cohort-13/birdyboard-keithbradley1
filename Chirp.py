
class Chirp():
    """
    Contain data for a single line item.
    Static Property:
        next_chirp_id   incrementing id for next created chirp
    """

    next_chirp_id = 1

    def __init__(self, name, message):
        """
        Store values for new chirp and increment next id
        Arguments:
            name    the name of the chrip
            message   the message of the chirp
        """
        self.name = name
        self.message = message
        self.id = Chirp.next_chirp_id
        Chirp.next_chirp_id += 1