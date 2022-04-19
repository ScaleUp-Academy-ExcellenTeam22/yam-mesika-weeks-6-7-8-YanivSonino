class RegularFile:
    def __init__(self, file_name, username, moderate):
        """Regular file class. The base class of files.

        :param str file_name: The File name.
        :param str username: The user who wants to create the file.
        :param str moderate: The level of user in the system

        """
        self.file_name = file_name
        self.creator = username
        self.moderate = moderate

    def get_creator(self):
        """Get the creator of the file.

        :return: File creator

        """
        return self.creator

    def get_moderate(self):
        """Get the level of the file moderate creator.

        :return: File moderate level.

        """
        return self.moderate

    def read(self, username, moderate):
        """Read file content.

        :param str username : The user that try to read from the file.
        :param str moderate: The moderate of the user.
        :return: File content
        :raises FileNotFoundError: If the file is not exist
        """
        if username == self.creator or 'm' == moderate:
            try:
                file = open(self.file_name, 'r')
                return file.read()
            except FileNotFoundError:
                print("no such file")
