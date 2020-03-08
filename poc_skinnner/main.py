import numpy as np
from logger import Clogger

"""
# HYPOTHESE:
1: état vivant, 0: état mort
"""

LOG_LEVEL = 10  # 0: DEBUG, 10:INFO

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


class Skinner:
    DATA_TYPE = np.bool_
    CARDINALITIES = [-1, 0, 1]
    DEAD, ALIVE = DATA_TYPE(0), DATA_TYPE(1)
    DEBUG = False

    def __init__(self, tab, iterations):
        self.input_tab = tab
        self.rows_number, self.columns_number = 0, 0
        self.iterations = iterations
        self.log = Clogger().get_logger()
        self.log.setLevel(LOG_LEVEL)
        self.current_tab, self.buffer_tab = [], []
        self.alive_neighbors = 0
        self.routine()

    def set_tab_size(self):
        self.rows_number = len(self.input_tab[0])
        self.columns_number = len(self.input_tab)
        self.log.debug("input tab is a %s r x %s c" % (self.rows_number, self.columns_number))

    def return_matrix_from_list(self, _list):
        try:
            matrix_candidate = np.asmatrix(_list, dtype=self.DATA_TYPE)
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
        while n_alive < 4 and not stop:
            for ii in self.CARDINALITIES:
                for jj in self.CARDINALITIES:
                    if (ii, jj) != (0, 0):
                        if (curr_row + ii in range(0, self.rows_number)) and (
                                curr_col + jj in range(0, self.columns_number)):
                            if self.buffer_tab[curr_row+ii, curr_col+jj] == self.ALIVE:
                                n_alive += 1
            stop = True
        return n_alive

    def play_death_rule(self, curr_row, curr_col):
        if self.buffer_tab[curr_row, curr_col] == self.ALIVE:
            if self.alive_neighbors not in [2, 3]:
                self.log.debug("cell (%s, %s) will die !" % (curr_row, curr_col))
                self.buffer_tab[curr_row, curr_col] = self.DEAD
        else:
            if self.alive_neighbors == 3:
                self.log.debug("cell (%s, %s) shall live again." % (curr_row, curr_col))
                self.buffer_tab[curr_row, curr_col] = self.ALIVE

    def main_loop(self):
        self.buffer_tab = self.current_tab
        for i in range(self.rows_number):
            for j in range(self.columns_number):
                self.alive_neighbors = self.return_neighbors_health(curr_row=i, curr_col=j)
                self.play_death_rule(curr_row=i, curr_col=j)
        self.current_tab = self.buffer_tab

    def main_process(self):
        for iteration in range(self.iterations):
            self.main_loop()
            self.buffer_tab = None
            self.prettyprint(self.current_tab, iteration)

    def prettyprint(self, matrix_to_print, iteration):
        self.log.debug("\n---------ITERATION N°%s---------" % iteration)
        MAXy, MAXx = matrix_to_print.shape
        stri = "\n\n"
        for j in range(MAXx):
            for k in range(MAXy):
                stri += str(int(matrix_to_print[k, j])) + " "
            stri += "\n"
        self.log.info(stri)

    def routine(self):
        self.ignition()
        if not self.DEBUG:
            self.main_process()


if __name__ == '__main__':
    S = Skinner(tab=TRY1, iterations=10)
