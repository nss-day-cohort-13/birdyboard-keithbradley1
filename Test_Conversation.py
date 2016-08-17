import unittest
from Conversation import *

#################### new conversaton tests ####################

class TestConversation(unittest.TestCase):

    def test_create_conversation(self):
        conversation = Conversation(1, 2)

        self.assertNotEqual(conversation.id, 0)
        self.assertEqual(conversation.conversation_id, 1)
        self.assertEqual(conversation.chirp_id, 2)


    def test_next_conversation_id_increments(self):
        Conversation.next_conversation_id = 1

        Conversation(1, 2)

        self.assertEqual(Conversation.next_conversation_id, 2)


if __name__ == '__main__':
    unittest.main()