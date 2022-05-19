from RegularFile import RegularFile


class DirectorysFile:
    """Directory File class. To allow user store their files.
    :ivar dict directory: The directory.
    :ivar str username: The user name.
    :ivar str directory_name: The directory name.

    :param str directory_name: The directory name.
    :param str username: The user who wants to create the file.
    """

    def __init__(self, directory_name, username):
        self.directory_file = {}
        self.directory_name = directory_name
        self.username = username

    def add_to_directory(self, file_name, file):
        """ Add file to directory
        :param File file: The file.
        :param str file_name: The file name
        """
        self.directory_file.update({file_name: file})
