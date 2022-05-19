import os
from RegularFile import RegularFile


class BinaryFile(RegularFile):
    """A Binary File class, inherit from RegularFile.

    :ivar int size: The size of the file in kb.

    :param str file_name: The File name.
    :param str username: The user who wants to create the file.
    :param str moderate: The level of user in the system
    """
    def __init__(self, file_name, username, moderate):
        super().__init__(file_name, username, moderate)
        try:
            self.size = os.path.getsize(file_name)
        except FileNotFoundError:
            print("no such file")

    def getsize(self):
        """Get the size of the File.

        :return: File size.
        """
        return self.size

