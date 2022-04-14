class Message:
    """A Message class. Allows post office to store their messages.

        :ivar dict message: Message details.

        :param int message_id: id of a message
        :param str message_headline: The text of the message headline.
        :param str message_body: The text of the message body.
        :param str sender: The sender name
        """

    def __init__(self, message_id, message_headline, message_body, sender):
        self.message = {"headline": message_headline,
                        "body": message_body,
                        'sender': sender,
                        'id': message_id}

    def __str__(self):
        return "Message From: {}, Message ID: {}, Headline: {}, Message: {}".format(self.message["sender"], self.message["id"], self.message["headline"], self.message["body"])

    def __len__(self):
        return len(self.message["body"])
