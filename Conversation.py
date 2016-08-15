class Conversation(object):
    """
    Contain data for a single Conversation.
    Static Property:
        next_conversation_id   incrementing id for next created conversation
    """

    next_conversation_id = 1

    def __init__(self, conversation_id, chirp_id):
        """
        Store values for new conversation and increment next id
        Arguments:
            conversation_id    the conversation item belongs to
            chirp_id  the chirp pertaining to the line item
        """

        self.id = Conversation.next_conversation_id
        self.conversation_id = conversation_id
        self.chirp_id = chirp_id
        Conversation.next_conversation_id += 1