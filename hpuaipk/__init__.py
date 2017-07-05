"""
Simple Hanyang PUA to Unicode IPK Converter

"""

import fire
from .table import table

__version__ = '0.0.1'


class Converter(object):
    """A simple converter class."""

    def __init__(self, encoding="utf8"):
        self._encoding = encoding

    def print(self, file_path):

        try:
            _file = open(file_path, "r", encoding=self._encoding)

        except FileNotFoundError:
            return "File not found: " + str(file_path)

        line = _file.readline()

        while line:
            yield "".join(table[char] if char in table else char
                          for char in line)
            line = _file.readline()

    def save(self, file_path, save_path):

        try:
            _file = open(file_path, "r", encoding=self._encoding)

        except FileNotFoundError:
            return "File not found: " + str(file_path)

        with open(save_path, "w", encoding=self._encoding) as _save:

            line = _file.readline()

            while line:
                _save.write("".join(table[char] if char in table else char
                                    for char in line))
                line = _file.readline()


def main():
    fire.Fire(Converter)