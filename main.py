import threading
import time
import random
from lamport import LamportProcess


# Function to execute each process
def execute_process(process):
    time.sleep(random.randint(1, 5))  # Random delay
    process.request_critical_section()
    process.enter_critical_section()


if __name__ == "__main__":

    # Number of processes
    n = 3

    # Create process list
    processes = []

    # Create LamportProcess objects
    for i in range(n):
        processes.append(LamportProcess(i, n))

    # Make processes accessible inside lamport module
    import lamport
    lamport.processes = processes

    # Create threads
    threads = []
    for process in processes:
        t = threading.Thread(target=execute_process, args=(process,))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    print("\nAll processes finished execution.")