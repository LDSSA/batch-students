import psutil
import gc

# check if memory usage is over limit
def check_memory_limit(limit: float = 90.):
    return psutil.virtual_memory()[2] > limit

def memory_circuit_breaker(limit: float = 90.):
    # if over limit, garbage collect
    if check_memory_limit(limit):
        gc.collect()

    # if still above limit, stop execution
    if check_memory_limit(limit):
        raise MemoryError("The execution of this cell has reached {limit} %. Stopping Execution.")