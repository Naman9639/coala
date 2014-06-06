__author__ = 'lasse'

from codeclib.fillib import FilterBase

class LocalFilter(FilterBase):
    def __init__(self, settings):
        FilterBase.__init__(settings)

    def run(self, filename, file):
        """
        Checks the given file.

        :param filename: The filename of the file
        :param file: The file contents as string array
        :return: A list of LineResult
        """
        raise NotImplementedError("This function has to be implemented for a runnable filter.")
