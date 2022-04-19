class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_headline, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param std message_headline: The headline of the message.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'headline': message_headline,
            'body': message_body,
            'sender': sender,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, user_name, N=0):
        """Read inbox from user inbox.

        :param str user_name: The user name.
        :param int N: The number of message the user wants to read.
        :return: The N messages of the user inbox
        """
        user_box = self.boxes[user_name]
        if N == 0 or N > len(user_box):
            N = len(user_box)
        return [message for index, message in enumerate(user_box) if index < N]

    def search_inbox(self, user_name, message_to_search):
        """Read inbox from user inbox.

        :param str user_name: The user name.
        :param str message_to_search: The substring of message.
        :return: The List of all the messages that contains the substring in there body or headline
        """
        user_box = self.boxes[user_name]
        return [message for message in user_box if message_to_search in message['body'] or message_to_search in message['headline']]



