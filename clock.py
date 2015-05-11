import time

def time_execution(code, codeinput):
    start = time.clock()
    result = code(codeinput)
    run_time = time.clock() - start
    return result, run_time