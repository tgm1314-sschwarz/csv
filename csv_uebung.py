import csv


"""Programm welches zwei csv dateien mit unterschiedlichen dialekt einliesst und
als csv mit einem ; dilekt speichert."""
__author__ = "Schwarz Stephan"
__version__ = "1.0"


class csv_uebung():

    @staticmethod
    def open_file(name, like):
        return open(name, like)

    @staticmethod
    def get_dialect(file):
        d = csv.Sniffer().sniff(file.read(1024))
        file.seek(0)
        return d

    @staticmethod
    def reg_dialect(name, delimiter):
        csv.register_dialect(name, delimiter=delimiter)

    @staticmethod
    def read_file(file, dialect):
        return csv.reader(file, dialect)

    @staticmethod
    def append_files(reader1, reader2):
        out = []

        for row in reader1:
            out.append(row)

        for row in reader2:
            out.append(row)

        return out

    @staticmethod
    def write_file(file, dialect, output):
        writer = csv.writer(file, dialect=dialect)
        for i in output:
            writer.writerow(i)

    @staticmethod
    def close_file(file):
        file.close()

if __name__ == '__main__':
    csv_uebung()
