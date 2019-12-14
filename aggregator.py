# coding: utf8
# works on python3.6+


from glob import iglob
from os import getcwd


class Aggregator(object):
    def __init__(self, path_to_files, pattern):
        self.pattern=pattern
        self.path_to_files = path_to_files if path_to_files else getcwd()
        self.matching_list = []
        self.aggregate()

    def aggregate(self):
        for f in iglob(self.path_to_files + self.pattern, recursive=True):
            self.matching_list.append(f)
