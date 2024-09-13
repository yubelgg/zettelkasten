---
id: intro-data-comms
aliases: []
tags: []
---

# Introduction to data communcations

Transmitting mesage from one node to another:

- message to one reciever (unicast)
- message to multiple reciever (multicast)
- message to everyone (broadcast)

### Circuit Sharing

FDM shares by frequency
TDM shares by time

## Packet Switching

Divides the message into smaller chuncks called **packets**.
It will need resources to store the packets in a queue, waiting for outpit link.

- store and forward: packages move one hop at a time

  - must recieve whole package before packet can be forwarded
  - put into a queue and waits for the output link
  - done at each router: **per hop**

Will resend package that is lost, which is why we divide it into smaller package.
**Packet switching allows more users to use the network**

### Package Switching Issue

1. What should be the packet size?
   - Fixed-size or variable size?
   - how big?
2. Should we establish an end to end path through the network for the package to flow?
   - yes: Virtual Circuit Networks (X.25, Frame-Relay, ATM, MPLS)
   - no: Datagram networks (the internet)

Assuming we have a 1 Mbps bandwidth

- with a 5\*10^6 (5 Mbps) message with 3 hops to destination node
- it will take 15 seconds to reach the destination

Assuming we have same bandwidth and smaller package size

- will have faster transmition
- small packages have **bit error**

Why not too small:

- Each package carries some **headers** (balancing headers size and package size)
- 100 byte package with a 20 byte header leads to a 20% bandwidth waste
- 1000 byte package with a 20 byte headers leads to a 2% bandwidth waste

ATM has a 5 byte header and 48 byte package size
