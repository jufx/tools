# coding: utf8
# works on python3.6+


import threading
from time import time
from time import sleep


class Executor(threading.Thread):
    def __init__(self, func):
        threading.Thread.__init__(self)
        self.current_milli_time = lambda: int(round(time() * 1000))
        self.func = func
        self.start_time_ms = 0
        self.end_time_ms = 0
        self.output = None

    def run(self):
        self.start_time_ms = self.current_milli_time()
        self.output = self.func.run()
        self.end_time_ms = self.current_milli_time()

    def run_duration_in_ms(self):
        return self.end_time_ms - self.start_time_ms

    def return_runner(self):
        return self.output


class ThreadPool(object):
    def __init__(self):
        self.execution_times = []
        self.runners_number = None
        self.func = None
        self.threads = []

    def populate(self, func, runners_number=None):
        assert runners_number is not None, "No "
        self.runners_number = runners_number
        self.func = func
        self.threads = []
        self.execution_times = []
        for i in range(0, self.runners_number):
            t = Executor(func)
            self.threads.append(t)

    def start(self, tempo=0):
        assert type(tempo) is int
        for thread in self.threads:
            sleep(tempo)
            thread.start()

    def wait(self):
        for thread in self.threads:
            thread.join()

    def get_executions_times(self):
        for thread in self.threads:
            if thread.return_runner() is not None:
                self.execution_times.append({"run_duration_in_ms": thread.run_duration_in_ms(),
                                         "content": thread.return_runner()})
        return self.execution_times


if __name__ == '__main__':
    # for testing purposes
    
    
    class SimpleFunk(object):
        def run():
            print("func")
            
            
    TP = ThreadPool()
    TP.populate(func=SimpleFunk, runners_number=100)
    TP.start()
    TP.wait()
    print(TP.get_executions_times())
