# -*- coding: utf-8 -*-
# author: Julien Faux - 2020-03-09

"""
1. OBJECTS

You will find 2 classes within this python3 script:
- Clogger : logging tool used for both debugging and main program's output
    to see debugging informations, set LOG_LEVEL to logging.DEBUG

- Skinner : main class used to solve the excercice.
    it's output can be from logger if Skinner.output is set to 'log'
    otherwise each tab will be printed using print

    no unittest have been produced yet.


2. BEHAVIOR:
    at the end of __init__, self.routine is called
    self.ignition perform input checks
    self.main_loop processes input tab following iterations set in input,
    then, for each cell, neighbors are analyzed and death rule is played.


3. RULES

to respect the synchronicity rule, each cell of "self.buffer_tab" is updated while each cell "self.current_tab" is read

the four live/death conditions have been simplified within the "play_death_rule' method
This both enhances code readability & runtime performance


4. numpy

if numpy's import fails, using pip from unix shell:
$ python3 -m pip install numpy
"""


import numpy as np
import logging
from sys import stdout


TRY1 = [
       [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
       [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
       [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0],
       [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
       [0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
       [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
       [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
       [0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
       [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
       [0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1]
]


class Clogger:
    logger_name = "LOGGER"

    def __init__(self, log_level):
        self.historic = []
        _logger = logging.getLogger(self.logger_name)
        _logger.setLevel(level=log_level)
        formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
        stdout_handler = logging.StreamHandler(stream=stdout)
        stdout_handler.setLevel(level=log_level)
        stdout_handler.setFormatter(fmt=formatter)
        file_handler = logging.FileHandler(filename='today.log', mode='a')
        file_handler.setLevel(level=log_level)
        file_handler.setFormatter(fmt=formatter)
        if len(_logger.handlers) < 1:
            _logger.addHandler(hdlr=stdout_handler)
            _logger.addHandler(hdlr=file_handler)

    def get_logger(self):
        return logging.getLogger(name=self.logger_name)


class Skinner:
    LOG_LEVEL = logging.DEBUG  # DEBUG | INFO
    log = Clogger(LOG_LEVEL).get_logger()
    DATA_TYPE = np.bool_
    CARDINALITIES = [-1, 0, 1]
    DEAD, ALIVE = DATA_TYPE(0), DATA_TYPE(1)
    output = "log"

    def __init__(self, tab, iterations):
        self.input_tab = tab
        self.rows_number, self.columns_number = 0, 0
        self.iterations = iterations
        self.current_tab, self.buffer_tab = [], []
        self.alive_neighbors = 0
        self.routine()

    def set_tab_size(self):
        self.rows_number = len(self.input_tab[0])
        self.columns_number = len(self.input_tab)
        self.log.debug("input tab has %s rows and %s columns" % (self.rows_number, self.columns_number))

    def return_matrix_from_list(self, _list):
        try:
            matrix_candidate = np.array(_list, dtype=self.DATA_TYPE)
            self.log.debug("converted list to a %s %s matrix" % (matrix_candidate.shape, self.DATA_TYPE.__name__))
            return matrix_candidate
        except Exception as e:
            self.log.error(e)

    def check_iteration_input(self):
        assert type(self.iterations) is int and self.iterations > 0, "need iterations to process data"

    def check_tab_input(self):
        self.log.debug('analyzing input table')
        assert type(self.input_tab) is list, "tab param must be  a list"
        assert len(self.input_tab) > 0, "need more rows in tab"
        assert len(self.input_tab[0]) > 0, "need more columns in tab"
        self.current_tab = self.return_matrix_from_list(self.input_tab)
        self.rows_number, self.columns_number = self.current_tab.shape
        for i in range(self.rows_number):
            for j in range(self.columns_number):
                assert type(self.current_tab[i, j]) is self.DATA_TYPE, "%s is not a %s" % (
                self.current_tab[i, j], self.DATA_TYPE.__name__)

    def ignition(self):
        self.log.debug('ignition started')
        self.check_iteration_input()
        self.check_tab_input()
        self.log.debug("entries are OK")

    def return_neighbors_health(self, curr_row, curr_col):
        n_alive, stop = 0, False
        self.alive_neighbors = n_alive
        while n_alive < 5 and not stop:
            for ii in self.CARDINALITIES:
                for jj in self.CARDINALITIES:
                    if (ii, jj) != (0, 0):
                        if (curr_row + ii in range(0, self.rows_number)) and (
                                curr_col + jj in range(0, self.columns_number)):
                            if self.current_tab[curr_row + ii, curr_col + jj] == self.ALIVE:
                                n_alive += 1
            stop = True
        return n_alive

    def play_death_rule(self, curr_row, curr_col):
        if self.current_tab[curr_row, curr_col] == self.ALIVE:
            if self.alive_neighbors not in [2, 3]:
                self.log.debug("cell (%s, %s) will die !" % (curr_row, curr_col))
                self.buffer_tab[curr_row, curr_col] = self.DEAD # keep synchronicity
        else:
            if self.alive_neighbors == 3:
                self.log.debug("cell (%s, %s) shall live again." % (curr_row, curr_col))
                self.buffer_tab[curr_row, curr_col] = self.ALIVE

    def update_current(self):
        self.current_tab = self.buffer_tab

    def update_buffer(self):
        self.buffer_tab = self.current_tab

    def main_loop(self):
        for i in range(self.rows_number):
            for j in range(self.columns_number):
                self.alive_neighbors = self.return_neighbors_health(curr_row=i, curr_col=j)
                self.play_death_rule(curr_row=i, curr_col=j)

    def main_process(self):
        for iteration in range(1, self.iterations+1):
            self.update_buffer()
            self.main_loop()
            self.update_current()
            self.log.debug("\n----------ITERATION N°%s----------" % iteration)
            self.prettyprint()

    def prettyprint(self):
        MAXy, MAXx = self.current_tab.shape
        stri = "\n\n"
        for j in range(MAXx):
            for k in range(MAXy):
                stri += str(int(self.current_tab[k, j])) + " "
            stri += "\n"
        if self.output == 'log':
            self.log.info(stri)
        else:
            for string in stri.split('\n'):
                print(string)

    def routine(self):
        self.ignition()
        self.main_process()


if __name__ == '__main__':
    S = Skinner(tab=TRY1, iterations=10)
