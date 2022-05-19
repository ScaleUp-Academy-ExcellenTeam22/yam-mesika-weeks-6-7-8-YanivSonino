class Message:
    """A Message class. Allows post office to store their messages.

        :ivar dict message: Message details.

        :param int message_id: id of a message
        :param str message_headline: The text of the message headline.
        :param str message_body: The text of the message body.
        :param str sender: The sender name
        """
    SEPARATOR_SIZE = 30

    def __init__(self, message_id, message_headline, message_body, sender):
        self.message = {"headline": message_headline,
                        "body": message_body,
                        'sender': sender,
                        'id': message_id}

    def __str__(self):
        message_ID_str = "Message ID: {}".format(self.message['id'])
        message_sender_str = f" | Message From: {self.message['sender']}"
        message_header_str = f"Title: {self.message['headline']}"
        separator = "-"
        return (f"{separator * len(message_sender_str + message_ID_str)}\n"
                + f"{message_ID_str}"
                + f"{message_sender_str}\n"
                + f"{separator * len(message_sender_str + message_ID_str)}\n"
                + f"{message_header_str}\n"
                + f"{separator * len(message_header_str)}\n"
                + f"{self.message['body']}\n"
                )

    def __len__(self):
        return len(self.message["body"])
