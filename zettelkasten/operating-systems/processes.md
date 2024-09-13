---
id: processes
aliases: []
tags: []
---

# Process Concept

Process is a program in execution and process execution must progress in a sequential fashion.
Program is a **passive** entity stored on disk; process is **active**.

- when program is loaded into memory it becomes a process

Layout of a process in memory:

- the program code
- current activity including **program counter**, processor register
- **stack** containing temporary data
  - function params, return addresses

### Process State

As a process executes, it changes state:

- **New**: Process is created
- **Running**: Instructions are being executed
- **Waiting**: The process is waiting for some event
- **Ready**: The process is waiting to be assigned to a process
- **Terminated**: The process has finsihed execution

==7 State process model== like the previous model but has an additional 2 states.

- **suspended ready**: when main memory is full, it will get moved to a secondary memory. \n
  It will remain in this state until the is enough space
- **suspened blocked/wait**: A blocked process is also move to secondary memory if main memory is full.

### Schedulers

There are 3 types of schedulers:

1. short term scheduler
   - selects which proces should be executed next and allocates CPU
   - invoked frequently so must be fast (milliseconds)
   - all other states that are not in long and medium are handled here
2. long term scheduler
   - this handles and selects which processes should be in the the ready queue
   - invoked infrequently so it's allowed to be slow in execution (seconds, minutes)
   - new and ready state are handled by this scheduler
3. medium term scheduler
   - suspended ready and blocked are handled by this scheduler

### Process Control Block (PCB)

Every process has a unique:

- process state - running, waiting, etc
- program counter - locaiton of instruction
- CPU registers - contents of all process-centric registers
- CPU scheduling information
- Memory management information
- Account information
- I/O status information

**Threads**
A process has a single thread of execution.
We need to store thread details in PCB.

**Proces Scheduling**

Proces Scheduling selects among the available process for the next execution on the CPU core.
**Goal**: maximze CPU usage, quickly switching processes
To maintain scheduling queues of process we have:

- ready queue - set of all process in main memory, ready to execute but is waiting.
- wait queue - set of all processes waiting for an even to compete like I/O.

### Context Switching

### Operations on Process

Parent process creates children process, which forms a **tree** of processes.
Resouce sharing options:

- parent and children share all resouces
- children share subset if parent's resouces
- pare and child share no resouces

Process Creation:
A child process is a duplicate of parent and has a program loaded into it.
In UNIX:

- `fork()` system call creates new processes.
- `exec()` system call is used after `fork()` to replace the process' memory space with a new program.
- parent process calls `wait()` to wait for the child to terminate.
  - to prevent parent from terminating before child process
  - child becomes orphan if parent is terminated before child is terminated, return 1

Parent id stores the child's id, and children's id is equal to 0.
If parent process pid is greater than 0, it goes to wait()
Creation of fork is 2^n
