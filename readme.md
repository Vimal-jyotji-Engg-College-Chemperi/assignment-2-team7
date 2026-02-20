**Lamport’s Algorithm for Distributed Databases**

**Overview**

This is a modular implementation of Lamport’s Distributed Mutual Exclusion Algorithm, designed to simulate controlled access to shared resources in distributed database systems.
The algorithm ensures that only one process can access the critical section at any given time, maintaining data consistency across distributed nodes.
This implementation is built using Python and follows an Object-Oriented Programming (OOP) approach.

**Algorithm Description**

Lamport’s algorithm is a permission-based mutual exclusion algorithm introduced by Leslie Lamport in 1978.

It uses:

- Logical Clocks to order events

Timestamped REQUEST messages

REPLY messages for permission

Release notifications

Sorted request queues

Unlike token-based algorithms, Lamport’s algorithm requires permission from all other processes before entering the critical section.

Key Features

Fully Distributed (No central coordinator)

Fair access using timestamp ordering

Deadlock-free

Starvation-free

Deterministic ordering of requests

Object-Oriented implementation

Project Structure

lamport-assignment/
├── lamport.py     # Contains LamportProcess class
├── main.py        # Executes and simulates processes
└── README.md      # Project documentation

Files Description

1️⃣ lamport.py – Core Algorithm Module

Contains the main class:

LamportProcess

Responsible for:

Maintaining logical clock

Managing request queue

Sending and receiving requests

Handling replies

Entering and exiting critical section

2️⃣ main.py – Execution File

Creates multiple process objects

Simulates distributed nodes using threads

Starts request-execute-release cycle

Displays system behavior

**Installation & Setup**
Prerequisites

Python 3.7 or higher

No external libraries required

Installation

Download or clone the project folder.

Navigate to the directory:

cd lamport-assignment
Usage

Run the simulation:

python main.py

The program will simulate multiple distributed processes requesting access to a shared resource.

How the Algorithm Works
1️⃣ Initialization

Create N processes

Each process maintains:

Logical clock

Request queue

Reply counter

2️⃣ Requesting Critical Section

When a process wants to enter:

Increment logical clock

Broadcast REQUEST(timestamp, process_id) to all other processes

Add its request to local queue

Wait for replies from all processes

3️⃣ Receiving a Request

Upon receiving a REQUEST:

Update logical clock:

clock = max(local_clock, received_timestamp) + 1

Add request to queue

Send REPLY back

4️⃣ Entering Critical Section

A process enters the critical section only if:

It has received replies from all other processes

Its request has the smallest timestamp in the queue

5️⃣ Releasing Critical Section

After execution:

Increment logical clock

Remove request from queue

Broadcast RELEASE message

Other processes remove its request

Example Execution Flow

Assume 3 processes: P0, P1, P2

P1 requests access (timestamp = 1)

P0 and P2 send replies

P1 enters critical section

After completion, P1 releases

Next process with smallest timestamp enters

Only one process is in the critical section at any time.

Message Complexity

For N processes:

REQUEST messages: N − 1

REPLY messages: N − 1

RELEASE messages: N − 1

Total messages per critical section entry:

3(N − 1)

This is higher than token-based algorithms.

API Reference
Class: LamportProcess
Constructor
LamportProcess(pid: int, total_processes: int)

Parameters:

pid → Process ID

total_processes → Total number of processes in the system

Methods
request_critical_section()

Sends request to all processes and waits for permission.

receive_request(timestamp, sender_pid)

Handles incoming request and sends reply.

enter_critical_section()

Enters critical section if conditions are satisfied.

release_critical_section()

Releases resource and notifies all processes.

System Properties
Mutual Exclusion

Only one process accesses shared data at a time.

Fairness

Requests are served in timestamp order.

Deadlock-Free

No circular waiting occurs.

Starvation-Free

Every request eventually gets executed.

Applications in Distributed Databases

Distributed transaction management

Write-lock synchronization

Multi-node database consistency

Distributed file access control

Advantages
Fully distributed approach
Clear event ordering using logical clocks
Simple and understandable implementation
No single point of failure

Limitations
High message overhead
Requires reliable communication
Not scalable for very large systems
Failure of one node may block others

Future Improvements
Add fault tolerance
Add crash recovery mechanism
Simulate network delays
Add visualization of request ordering
Add performance analysis metrics

Conclusion

This demonstrates a complete implementation of Lamport’s Distributed Mutual Exclusion Algorithm for distributed database systems.
The simulation ensures safe and fair access to shared resources using logical clocks and timestamp-based ordering, making it suitable for understanding distributed synchronization mechanisms.




