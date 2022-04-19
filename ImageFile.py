from BinaryFile import BinaryFile


class ImageFile(BinaryFile):
    """A Image File class, inherit from BinaryFile.

        :param str file_name: The File name.
        :param str username: The user who wants to create the file.
        :param str moderate: The level of user in the system
    """
    def __init__(self, username, file_name, moderate):
        super().__init__(file_name, username, moderate)

    def get_dimensions(self):
        """Get the dimensions of the Image.

        :return: Image dimensions.
        """
        pass
