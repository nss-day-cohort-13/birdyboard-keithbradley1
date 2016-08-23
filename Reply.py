class Reply(object):
    """
    Creates new reply, storing to the conversation data file.
    Static Property:
        next_reply_id   incrementing id for next created reply.
    """


    next_reply_id = 1

    def __init__(self, user_id):
        """
        Store values for new reply and increment next id.
        Arguments:
            user_id       the user associated with the reply
        """

        self.id = Reply.next_reply_id
        self.user_id = user_id
        Reply.next_reply_id += 1