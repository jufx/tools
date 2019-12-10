# coding: utf8
# works on python3.6+
from fuzzywuzzy import fuzz


class SimpleMatcher():
    def __init__(self, one, two):
        self.value = fuzz.ratio(one, two)


if __name__ == '__main__':
    # for testing purposes
    print(SimpleMatcher('aaa', 'abbaa').value)
