import os
from DirectorysFile import DirectorysFile
from ImageFile import ImageFile
from TextFile import TextFile
from BinaryFile import BinaryFile


class FileSystemManager:
    """A File system manager class. Allow user to manage their files

    :ivar dict file_manager: User files manager.

    :param list usernames: User list to register in the system.
    """

    def __init__(self, usernames):
        self.file_manager = {user["username"]: [user["password"], user["moderate"], {}] for user in usernames}

    def add_file(self, username, password, file_name):
        """Add a file to the file manager system

        :param str username: The user that want to add the file.
        :param str password: The password of the user.
        :param str file_name: The name of the file the user wants to add.

        :return: If user succeed or failed to add file.
        :raises FileNotFoundError: If user enter file name that is not exist.
        :raises KeyError: If user enter username that is not exist in the system.
        """
        if self.file_manager[username][0] == password:
            user_files = self.file_manager[username][2]
            name, extension = os.path.splitext(file_name)
            if os.path.isdir(file_name):
                user_files.update({file_name: DirectorysFile(file_name, username)})
            else:
                if extension == '.txt' or extension == '.svg':
                    user_files.update({file_name: TextFile(file_name, username, self.file_manager[username][1])})
                elif extension == '.png' or extension == '.jpg':
                    user_files.update({file_name: ImageFile(file_name, username, self.file_manager[username][1])})
                else:
                    user_files.update({file_name: BinaryFile(file_name, username, self.file_manager[username][1])})
            return "Succeed"
        else:
            print("wrong details")
            return "Failed"
