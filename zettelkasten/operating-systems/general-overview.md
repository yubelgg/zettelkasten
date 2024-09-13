---
id: general-overview
aliases: []
tags: []
---

# General Overview

## System Calls

OS provides the services, and system calls are usually written in a high level language (C,C++).

- It will have a unique number associated with it.

## System call parameter passing

Will often need a parameter, usually the simplest way is through the registers.

- if size is larger than register, not a good idea

We can also store it in a block and just pass the address as the parameter.
Also can use a stack (LIFO) by the operating systems.

## Types of system calls

1. process control
   - create, terminate, load, execute
2. File management
   - create, delete, read, write
3. Device management
   - request release, read, write device
4. Information maintenance
   - get/set time, system data
5. communications
   - send/receive messages, shared memory
6. protection
   - control access to resources
