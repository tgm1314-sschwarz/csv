import csv


testerror

class CSVTest:
    """
    Class that can be used to read, append and write csv files.
    """

    @staticmethod
    def open_file(name, like):
        """
        Method for opening a csv file
        """
        return open(name, like)

    @staticmethod
    def get_dialect(file):
        """
        Method that sniffs out the dialect of a give csv file
        :param file: file you want to know the dialect off
        """
        d = csv.Sniffer().sniff(file.read(1024))
        file.seek(0)
        return d

    @staticmethod
    def reg_dialect(name, delimiter):
        """
        Method that can be used to register a new dialect for yourself
        :param name: the name of the dialect you want to register
        :param delimiter: the delimiter you want to set for the dialect
        """
        csv.register_dialect(name, delimiter=delimiter)

    @staticmethod
    def read_file(file, dialect):
        """
        Method that can be used to read a csv file
        :param file: the file you want to read
        :param dialect: the dialect that is used in the file
        """
        return csv.reader(file, dialect)

    @staticmethod
    def append_files(reader1, reader2):
        """
        Method that can be used to append two csv files together so it can be put into a third one
        :param reader1: input from the first file
        :param reader2: input from the second file
        """
        out = []

        for row in reader1:
            out.append(row)

        for row in reader2:
            out.append(row)

        return out

    @staticmethod
    def write_file(file, dialect, output):
        """
        Method that can be used for writing a new csv file
        :param file: name of the file you want to write
        :param dialect: the dialect the file you want to write has
        :param output: what the file you want to write contains
        """
        writer = csv.writer(file, dialect=dialect)
        for i in output:
            writer.writerow(i)

    @staticmethod
    def close_file(file):
        """
        Method that is used for closing the csv files once you are finished
        :param file: the file you want to close
        """
        file.close()
