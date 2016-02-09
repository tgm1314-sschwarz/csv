from csv_uebung import *
from unittest import TestCase


class TestCSV(TestCase):
    def setUp(self):
        self.csv = CSVTest()
        self.f1 = self.csv.open_file("input1.csv", "rt")
        self.f2 = self.csv.open_file("input2.csv", "rt")

        self.d1 = self.csv.get_dialect(self.f1)
        self.d2 = self.csv.get_dialect(self.f2)

        self.r1 = self.csv.read_file(self.f1, self.d1)
        self.r2 = self.csv.read_file(self.f2, self.d2)

        self.out = self.csv.append_files(self.r1, self.r2)

        self.read_test = ['SPOE', 'FPOE', 'OEVP', 'GRUE', 'NEOS', 'WWW', 'ANDAS', 'GFW', 'SLP', 'WIFF', 'M', 'FREIE']
        self.out_test = [['SPOE', 'FPOE', 'OEVP', 'GRUE', 'NEOS', 'WWW', 'ANDAS', 'GFW', 'SLP', 'WIFF', 'M', 'FREIE'], ['27', '14', '15', '10', '9', '0', '1', '0', '0', '0', '0', '0']]

        pass

    def test_open_file(self):
        self.assertRaises(FileNotFoundError, self.csv.open_file, "wrong.csv", "rt")

    def test_read_file(self):
        reader = self.csv.read_file(self.f1, self.d1)
        for row in reader:
            assert(row == self.read_test)

    def test_append_files(self):
        out = self.csv.append_files(self.f1, self.f2)
        for row in out:
            assert(row == self.out_test)

    def test_write_file(self):
        self.assertRaises(TypeError, self.csv.write_file, "wrongType", "semicolon", self.out)

    def test_close_file(self):
        self.assertRaises(AttributeError, self.csv.close_file, "wrongAttribute")
