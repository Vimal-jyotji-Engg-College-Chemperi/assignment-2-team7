import threading
import time
import random


class LamportProcess:

    def __init__(self, pid, total_processes):
        self.pid = pid
        self.total_processes = total_processes
        self.clock = 0
        self.request_queue = []
        self.reply_count = 0
        self.requesting = False

    # Increment logical clock
    def increment_clock(self):
        self.clock += 1

    # Update clock on receiving message
    def update_clock(self, received_time):
        self.clock = max(self.clock, received_time) + 1

    # Send request to all processes
    def request_critical_section(self):
        self.increment_clock()
        self.requesting = True
        timestamp = self.clock
        self.request_queue.append((timestamp, self.pid))
        self.request_queue.sort()

        print(f"Process {self.pid} requesting CS at time {self.clock}")

        for process in processes:
            if process.pid != self.pid:
                process.receive_request(timestamp, self.pid)

    # Receive request from another process
    def receive_request(self, timestamp, sender_pid):
        self.update_clock(timestamp)
        self.request_queue.append((timestamp, sender_pid))
        self.request_queue.sort()

        print(f"Process {self.pid} received request from Process {sender_pid}")

        # Send reply
        for process in processes:
            if process.pid == sender_pid:
                process.receive_reply()

    # Receive reply
    def receive_reply(self):
        self.reply_count += 1

    # Enter critical section
    def enter_critical_section(self):
        while True:
            if (self.requesting and
                self.reply_count == self.total_processes - 1 and
                self.request_queue[0][1] == self.pid):

                print(f"Process {self.pid} ENTERING Critical Section")
                time.sleep(2)  # Simulate database access
                self.release_critical_section()
                break

            time.sleep(0.5)

    # Release critical section
    def release_critical_section(self):
        self.increment_clock()
        print(f"Process {self.pid} RELEASING Critical Section")

        self.request_queue = [req for req in self.request_queue if req[1] != self.pid]
        self.requesting = False
        self.reply_count = 0

        for process in processes:
            if process.pid != self.pid:
                process.remove_request(self.pid)

    # Remove request from queue
    def remove_request(self, pid):
        self.request_queue = [req for req in self.request_queue if req[1] != pid]


# --------- Main Program ---------

def execute_process(process):
    time.sleep(random.randint(1, 5))
    process.request_critical_section()
    process.enter_critical_section()


# Number of processes
n = 3
processes = []

# Create objects
for i in range(n):
    processes.append(LamportProcess(i, n))

# Create threads
threads = []
for process in processes:
    t = threading.Thread(target=execute_process, args=(process,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()