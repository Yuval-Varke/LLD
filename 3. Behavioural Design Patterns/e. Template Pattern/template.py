from abc import ABC, abstractmethod


class DataParser(ABC):
    def parse(self):
        self._open()
        self._dataParser()
        self._close()

    def _open(self):
        print("Opening the file")

    def _close(self):
        print("Closing the file")

    @abstractmethod
    def _dataParser(self):
        pass


class CSVParser(DataParser):
    def _dataParser(self):
        print("Parsing CSV File")


csv_parser = CSVParser()
csv_parser.parse()