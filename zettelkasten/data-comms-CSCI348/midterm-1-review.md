# Midterm Data Communications Review

## Chapter 1: Introduction

### Question 1

What's propagation delay? how do you compute it for a given link?

Propagation delay is the time it takes for a signal to travel from one end of a link to the other. It is computed by multiplying the length of the link by the propagation speed of the medium. ^propagation-delay

Formulate the equation for propagation delay.

$$
\text{Propagation delay} = \frac{\text{Length of the link}}{\text{Propagation speed of the medium}}
$$
^propagation-delay-formula

Propagation speed depends on the medium.

- For copper wire, the speed of propagation is 2.3 x 10^8 m/s.
- For optical fiber, the speed of propagation is about 2/3 the speed of light, which is 3 x 10^8 m/s.

Example:

A link has a length of 1000 meters and a propagation speed of 2.3 x 10^8 m/s. What's the propagation delay?

$$
\text{Propagation delay} = \frac{1000}{2.3 \times 10^8} = 4.3478 \times 10^{-6} \text{ seconds} = 4.3478 \text{ microseconds}
$$

### Question 2

If I am seding 1 bit to a host in the moon, which of the following is the dominat factor: [[midterm-1-review#^transmission-delay|transmission delay]] or [[midterm-1-review#^propagation-delay|propagation delay]]?

Transmission delay is the time it takes to push all the bits of a message into the link. For 1 bit, this is extremely small, regardless of the transmission speed of the medium. 
^transmission-delay

$$
\text{Transmission delay} = \frac{\text{Length of the message (size of data)}}{\text{Transmission speed of the medium (bandwidth)}}
$$
^transmission-delay-formula

For a 1-bit message, with a slow bandwidth of 1 Mbps, the transmission delay is 1 bit / 1 Mbps = 0.000001 seconds or 1 microsecond.

Distance from the moon to the earth is 384,400 km.

$$
\text{Propagation delay} = \frac{384,400 \times 10^3}{3 \times 10^8} = 1.2813 \text{ seconds}
$$

The propagation delay (1.2813 seconds) is much greater than the transmission delay (1 microsecond).

**So, the dominant factor is the propagation delay.**

- Distance: enormous distance to the moon.
- Single bit: trasmitting 1 bit is very fast.
- Speed Limit: propagation speed is limited by the speed of light, which is 3 x 10^8 m/s, and constant.

### Question 3

If I am sending 1Mbits to a host in the same room, which of the following is the dominant factor: [[midterm-1-review#^transmission-delay|transmission delay]] or [[midterm-1-review#^propagation-delay|propagation delay]]? Justify your answer.

[[midterm-1-review#^transmission-delay-formula|transmission delay formula]]
[[midterm-1-review#^propagation-delay-formula|propagation delay formula]]

1Mbits = 1,000,000 bits.

Suppose we have a 1Gbps link (1000 Mbps).

$$
\text{Transmission delay} = \frac{1 \times 10^6}{1 \times 10^9} = 0.001 \text{ seconds}
$$

Assume the distance between two hosts is 10 meter.

$$
\text{Propagation delay} = \frac{10}{2 \times 10^8} = 5 \times 10^{-8} \text{ seconds} \approx 0.05 \text{ microseconds}
$$

The transmission delay is much greater than the propagation delay.

**So, the dominant factor is the transmission delay.**

### Question 4

I have a datacenter where two servers exchange huge amounts of data (in the order of petabytes).  I need to reduce the time it takes for the data to go from one server to the other. A friend of mine suggests  that  I  reduce  the  cable  size  connecting  the  two  servers  by  half,  and  another  friend suggests that I increase the bandwidth of the cable two folds. Which suggestion should I follow?  Justify your answer.

1. Halving the cable size by half

Halving the cable size will reduce the propagation delay by **50%**. However in a datacenter the distance between servers is not that large, so the propagation delay reduction is not that significant.

Halving the propagation has not affects on [[midterm-1-review#^transmission-delay-formula|transmission delay]].

2. Doubling the bandwidth

Doubling the bandwidth will reduce the transmission delay by **50%**. For large data center, this can be a significant reduction in the time it takes for the data to go from one server to the other.

Example:

- initial bandwidth: 1 Gbps (1 x 10^9 bits/second)
- data size: 1 Petabyte (8 x 10^15 bits)

Initial transmission delay: 1 Gbps

$$
\text{Initial transmission delay} = \frac{8 \times 10^{15}}{1 \times 10^9} = 8 \times 10^6 \text{ seconds} \approx 92.6 \text{ days}
$$

New transmission delay: 2 Gbps

$$
\text{New transmission delay} = \frac{8 \times 10^{15}}{2 \times 10^9} = 4 \times 10^6 \text{ seconds} \approx 46.3 \text{ days}
$$

**So, doubling the bandwidth will reduce the transmission delay by 50%.**

### Question 5

NASA establishes a lunar base and needs to establish a data link between the control station in Houston and the lunar base. They only need to send a packet of 1000 bytes every hour that contains some information about the things to be done. They can set up a low bandwidth 1Kbps link for $1000 or a high bandwidth 1Gbps link for $1,000,000. Which one should they choose and why? Justify your answer.

Trying to find the balance between the cost and the time it takes for the data to go from one server to the other.

1. Low bandwidth 1Kbps link

    - Cost: $1000
    - Bandwidth: 1 Kbps (1 x 10^3 bits/second)
    - Data size: 1000 bytes = 8 x 10^3 bits
    - Transmission Rate: 1 Kbps (1 x 10^3 bits/second)

    $$
    \text{Transmission delay} = \frac{8 \times 10^3}{1 \times 10^3} = 8 \text{ seconds}
    $$

    - Frequency of transmission: sending 1 packet every hour, allow use time to send the packet. 8 seconds is not a big deal.

    - Troublesome if data size is larger.

2. High bandwidth 1Gbps link

    - Cost: $1,000,000
    - Bandwidth: 1 Gbps (1 x 10^9 bits/second)
    - Transmission Rate: 1 Gbps (1 x 10^9 bits/second)

    $$
    \text{Transmission delay} = \frac{8 \times 10^3}{1 \times 10^9} = 8 \times 10^{-6} \text{ seconds} = 8 \text{ microseconds}
    $$

    - more future proof if the data size is larger.

**1 Kbps link is cheaper and more cost effective.**

### Question 6

How many layers does the OSI protocol stack have? List them from top to bottom.

The OSI protocol stack has 7 layers:

1. Application Layer - Provides network services to the end-user.
2. Presentation Layer - translate data between the application layer and the network format
3. Session Layer - manages sessions between applications
4. Transport Layer - responsible for end-to-end error recovery and flow control
5. Network Layer - handles data routing between networks
6. Data Link Layer - provides node-to-node data transfer and error correction
7. Physical Layer - transmits raw bits over a physical medium

### Question 7

How many layers does the TCP/IP protocol stack have? List them from top to bottom.

The TCP/IP protocol stack has 4 layers:

1. Application Layer - combines function of Application, Presentation, and Session layers in the OSI model.
2. Transport Layer - resposible for end-to-end error recovery and flow control. (TCP and UDP)
3. Internet Layer - handles routing packets between networks (IP)
4. Link Layer - deals with physical transmission medium and the hardware that connects devices to each other. (Ethernet, WiFi, etc.)

### Question 8

In a circuit-switched network can unused resources belonging to a call be used by other calls to increase network utilization? Why or why not?  

Curcuit-switched is the connections that is established between two hosts before the data transmission, the data is then transmitted on a dedicated path. Noone else can use the path for connection.

**Unused resources belonging to a call cannot be used by other calls to increase network utilization.**

- It has a dedicated allocation once the circuit is established, and the entire bandwidth is dedicated to the two hosts, regardless of whether data is being transmitted or not.
- The capacity of the circuit remains constant.


### Question 9

List 1 advantage and 1 disadvantage of making the packet size small in a packet-switched network

Advantage:
- reduced transmission time: smaller packet size means less time to transmit.
- Faster Processing: routers and switches can process smaller packets more quickly.

Disadvantage:
- Increased overhead: each packet needs to carry its own header information, proportion of header data to payload data is higher, reducing the efficiency.
- Less efficient use of bandwidth: smaller packet size means less data is transmitted per packet, which can lead to less efficient use of bandwidth.


### Question 10

List 1 advantage and 1 disadvantage of making the packet size big in a packet-switched network.

Advantage:
- more efficient for bulk data transfer: they can send more data per packet, reducing the overhead of sending multiple small packets.

Disadvantage:
- higher latency: larger packets take longer to transmit, which can lead to longer delays.

### Question 11

In a virtual-circuit switched network, can packets belonging to the same connection, i.e., communicating pairs, follow different paths in the network and arrive out-of-order at the destination? Justify your answer.

Virtual-circuit is a dedicated path between two hosts. Once the path is established, all packets belonging to the same connection should follow the same path. Physical resources are not exclusively dedicated to the connection.

**No, packets belonging to the same connection should follow the same path in a virtual-circuit switched network.**

### Question 12

True/False. In a [[datagram-network]], each packet carries the destination address in the packet header. Justify your answer.

True. In a [[datagram-network]], each packet carries the destination address in the packet header. This is because the destination address is used to determine the next hop in the network.

### Question 13

What's the main motivation for packet switching? Briefly explain.

Packet switching allows multiple connections to share the same resources, and it is more efficient than circuit switching.

Packets can also be routed differently based on network conditions, and if a packet is lost, only the lost packet needs to be retransmitted.

### Question 14

True/False. If a node needs to communicate only with nodes on the same link, i.e., with another neighbor, Physical Layer and Link Layer are enough. In other words, no network layer is necessary. Justify your answer.

True, if a node only needs to communicate with nodes on the same link, physical layer and link layer are enough.

The network layer is not necessary. Network layer is only needed if the node needs to communicate with nodes on different networks.

### Question 15

How "wide" is a bit on a 1 Gbps link? 

A width of a bit means how far the signal can travel before the next bit arrives (the physical distance the bit occupies the medium).

Rate at which bits are transmitted is 1 Gbps, which is 1 x 10^9 bits per second.

Assuming we are using fiber-optic cable, which has a propagation speed of 2/3 the speed of light, i.e., 2 x 10^8 m/s.

$$
\text{Distance} = \text{Propagation speed} \times \text{Time}
$$

$$
\text{Distance} = \frac{2 \times 10^8 \text{ m/s}}{1 \times 10^9 \text{ s}} = 0.2 \text{ meters} = 20 \text{ cm}
$$

So, a bit on a 1 Gbps link is 0.2 meters wide or 20 cm wide.

### Question 16

Suppose you are developing a standard for a new type of network. You need to decide whether your network will use virtual-circuits or datagram forwarding. What are the pros and cons of using virtual-circuits?

Pros:
- Connection-oriented: ensures that data is delivered reliably and in order.
- Efficient Resource Allocation: dedicated resources for each connection, efficient for applications that require consistent data rates.

Cons:
- Inefficient Resource Utilization if network is idle or underutilized.
- If the path on the virtual-circuit is broken, the entire connection is broken.

### Question 17

Briefly describe how Time Division Multiplexing (TDM) works.

Divides the available bandwidth into time slots, and each connection is assigned a time slot. 

![[circuit-switching-TDM.png]]

### Question 18

Briefly describe how Frequency Division Multiplexing (FDM) works.

Divides the available bandwidth into frequency bands, and each connection is assigned a frequency band.

![[circuit-switching-FDM.png]]

### Question 19

Briefly explain what’s meant by the “service interface” of a protocol? What’s the service interface of the Internet Protocol (IP)? 

Service interface is the set of protocols from lower layers that a layer makes available to the layer above it.

In the case of IP, it exports a connectionless, unreliable, "best effort" datagram to the transport layer protocol.

### Question 20

Briefly explain what’s meant by the “peer interface” of a protocol? 

Peer interface is a set of rules that defines how two layers interact with each other.

Peer interface is the communication interface with its counterpart (peer) on another machine.

This interface defines the form and meaning of messages exchanged between protocol peers to implement the service interface.

### Question 21

How and why do packets get lost during transmission? Briefly explain.

1. Packet loss during transmission
2. Packet loss due to congestion
3. Packet loss due to errors
4. Packet loss due to network overload
5. Packet lost due to hardware failure
6. Packet lost due to TTL expiration

### Question 22

Consider sending a file F=M*L bits over a path of N links. Each link transmits at R bits/sec. The network is lightly loaded so that there are no queuing delays. When packet switching is used, the M*L bits are broken up into M packets, each packet L bits. Also assume that the propagation delay is negligible. 

File size: F = M*L bits
Number of links: N
Transmission rate: R bits/sec
Setup time: ts
Header size: h bits

a.  Suppose that the network is circuit-switched. Further suppose that the transmission rate of the circuit between the source and the destination is R bps. Assuming ts set-up time and h bits of header appended to the entire file, how long does it take to send the file? 

Circuit-switch requires a set up time (Ts) so we add that to the file size + header divided by the transmission rate. This will result in how long it takes to send the file.

$$
total size = F + h = M*L + h
$$

$$
transmission time = \frac{F}{R} = \frac{M*L+h}{R}
$$

$$
total time = transmission time + setup time = \frac{M*L+h}{R} + ts
$$

b.  Suppose the network is a packet-switched virtual circuit network such as X.25. Denote the virtual-circuit set-up time by ts. Suppose the sending layers add a total of h bits of header to each packet. How long does it take to send the file from the source to the destination? 

Virtual circuit networks still need to determine a path so we use Ts as the time it takes to set- up. We then are using packet-switching so the file gets split into several packets M that all get a headers H. We find the time it takes for the packets with headers to send as M x (L + H) / R and put everything together to get the equation above.

$$
packet size = L + h
$$

$$
total size = M * (L + h)
$$

$$
transmission time = \frac{M * (L + h)}{R}
$$

$$
total time = transmission time + setup time = \frac{M * (L + h)}{R} + ts
$$

c.  Suppose the network is a packet-switched datagram network such as the Internet. Now suppose that each packet has 2*h bits of header. How long does it take to send the file?

Datagram network doesn’t require time to set up a fixed circuit to follow since it constantly changes routes, so Ts is not used here. Since it is packet-switched we have to include the header to all packets so M packets with (L + 2H) size and bitrate of R. The result is the equation above.

$$
packet size = L + 2h
$$

$$
total size = M * (L + 2h)
$$

$$
transmission time = \frac{M * (L + 2h)}{R}
$$

$$
total time = \frac{M * (L + 2h)}{R}
$$

### Question 23

Suppose two nodes A and B are connected via a point-to-point link. The length of the link is 10000km and its bandwidth is 1Kbps. Assume the speed of signal on the wire is 3x10^5 km/sec. 

Given:
- Length of the link: 10000 km
- Bandwidth: 1 Kbps
- Speed of signal: 3 x 10^5 km/s

a.  Calculate the minimum RTT for the link. 

$$ Propagation Delay = \frac{Distance}{Speed} = \frac{10000 \text{ km}}{3 \times 10^5 \text{ km/s}} = 0.0333 \text{ seconds} $$

$$
RTT = 2 \times Propagation Delay = 2 \times 0.0333 \text{ seconds} = 0.0666 \text{ seconds}
$$

b.  How long does it take to transmit 1000 bytes from A to B.

Convert 1000 bytes to bits:

$$
1000 \text{ bytes} = 1000 \times 8 = 8000 \text{ bits}
$$

$$
Transmission Time = \frac{File Size}{Bandwidth} = \frac{8000 \text{ bits}}{1000 \text{ bits/sec}} = 8 \text{ seconds}
$$

### Question 24

Suppose a 100 Mbps point-to-point link is being set up between the earth and a new lunar colony. The distance from the moon to the earth is approximately 390,000 km, and data travels over the link at the speed of light, i.e., 3x10^5 km/sec. 

Given:
- Distance: 390,000 km
- Speed: 3 x 10^5 km/s
- Bandwidth: 100 Mbps (100,000,000 bits/s)

a.  Calculate the minimum RTT for the link. 

$$
Propagation Delay = \frac{Distance}{Speed} = \frac{390,000 \text{ km}}{3 \times 10^5 \text{ km/s}} = 1.3 \text{ seconds}
$$

$$
RTT = 2 \times Propagation Delay = 2 \times 1.3 \text{ seconds} = 2.6 \text{ seconds}
$$

b.  A camera on the lunar base takes pictures of the earth and saves them in digital format to disk.  Suppose Mission Control on earth wishes to download the most current image, which is 25MB.  What is the minimum amount of time that will elapse between when the request for the data goes out and the transfer is finished? 

Convert 25MB to bits:

$$
25 \text{ MB} = 25 \times 10^6 \text{ bytes} = 25 \times 10^6 \times 8 = 200 \times 10^6 \text{ bits}
$$

$$
Transmission Time = \frac{File Size}{Bandwidth} = \frac{200 \times 10^6 \text{ bits}}{100 \times 10^6 \text{ bits/s}} = 2 \text{ seconds}
$$

$$
Total Time = RTT + Transmission Time = 2.6 \text{ seconds} + 2 \text{ seconds} = 4.6 \text{ seconds}
$$


### Question 25

Consider  two  hosts  A  and  B  connected  by  a  single  link  of  rate  R bps.  Suppose  that  the  two  hosts  are separated by M meters and suppose the propagation speed along the link is s m/sec. Host A is to send a packet of size L bits to host B. 

a.  Express propagation delay tprop in terms of M and s. 

M = distance between A and B
s = propagation speed

$$
t_{prop} = \frac{M}{s}
$$

b.  Determine the transmission time of the packet ttrans in terms of L and R.

R = transmission rate in bits per second
L = size of the packet in bits

$$
t_{trans} = \frac{L}{R}
$$

c.  Ignoring processing and queueing delays, how long does it take for the last bit of the packet to arrive at B? 

$$
t_{total} = t_{prop} + t_{trans} = \frac{M}{s} + \frac{L}{R}
$$

d.  Suppose host A begins to transmit the packet at time t=0. At time t = ttrans where is the last bit of the packet?  

Transmission time is the time it takes for the packet to be placed on the wire. So from 0 to Ttrans its being placed on the wire. By the end of it the entire packet is finally on the wire.  Propagation would be the time it takes to go across the wire to B.At time t = ttrans, the last bit of the packet is at the destination.

e.  Suppose tprop is greater than ttrans. At time t = ttrans where is the first bit of the packet? 

$$
Distance traveled by first bit = s \times t_{trans} = s \times \frac{L}{R}
$$

f.  Suppose s=2.5*105 km/s, L=100 bits, and R=28 Kbps. Find the distance m so that tprop equals ttrans. 

Given:
- s = 2.5 x 10^5 km/s = 2.5 x 10^8 m/s (converting to meters per second)
- L = 100 bits
- R = 28 Kbps = 28,000 bits/s

we want
$$
t_{prop} = t_{trans}
$$

$$
\frac{M}{s} = \frac{L}{R}
$$

$$
M = \frac{L \times s}{R} = \frac{100 \text{ bits} \times 2.5 \times 10^8 \text{ m/s}}{28,000 \text{ bits/s}} = 892.86 \text{ meters}
$$

### Question 26

Suppose two hosts A and B are separated by 10,000 kilometers and are connected by a direct link of R=1 Mbps. Suppose the propagation speed over the link is 2.5*10^8 m/sec. 

Given:
- Distance A and B: 10,000 km = 10,000,000 meters
- Bandwidth (R): 1 Mbps = 1,000,000 bits/s
- Propagation speed (s): 2.5 x 10^8 m/s

a.  Calculate the “bandwidth-delay” product R*tprop. 

1. Calculate the propagation delay:
$$
t_{prop} = \frac{M}{s} = \frac{10,000,000 \text{ meters}}{2.5 \times 10^8 \text{ m/s}} = 0.04 \text{ seconds}
$$

2. Calculate the bandwidth-delay product:
$$
R \times t_{prop} = 1,000,000 \text{ bits/s} \times 0.04 \text{ seconds} = 40,000 \text{ bits}
$$

b.  Provide an interpretation of the bandwidth-delay product. 

Bandwidth delay product is the max amount of data that can be in the process of being sent at any given time. 40,000 bits means that at any given time that amount of bits can be in the link.

c.  Consider sending a file of 400,000 bits from host A to host B. Suppose the file is sent continuously as one big message. How long does it take for the last bit of the message to arrive at B. 

1. Calculate the transmission time:
$$
t_{trans} = \frac{File Size}{R} = \frac{400,000 \text{ bits}}{1,000,000 \text{ bits/s}} = 0.4 \text{ seconds}
$$

2. Calculate the total time:
$$
total time = t_{prop} + t_{trans} = 0.04 \text{ seconds} + 0.4 \text{ seconds} = 0.44 \text{ seconds}
$$

### Question 27
Consider the packet switched network shown below. The bandwidth of the link between the source and router R1 is 1 Mbps and the length of the link is 1000 kms. The bandwidth of the link between router R1 and the destination is 100Kbps and the length of the link is 10000 kms. Assume that the speed of light is 2*10^5 km/sec. 

![[questions 7.png]]

Given:
- Link 1 (Source to R1): 
  - Bandwidth: 1 Mbps = 1,000,000 bits/s
  - Length: 1000 km
- Link 2 (R1 to Destination):
  - Bandwidth: 100 Kbps = 100,000 bits/s
  - Length: 10,000 km
- Speed of light: 2 x 10^5 km/s

a.  What's the RTT? 

1. Calculate the propagation delay for Link 1:

$$
t_{prop1} = \frac{1000 \text{ km}}{2 \times 10^5 \text{ km/s}} = 0.005 \text{ seconds}
$$

2. Calculate the propagation delay for Link 2:

$$
t_{prop2} = \frac{10,000 \text{ km}}{2 \times 10^5 \text{ km/s}} = 0.05 \text{ seconds}
$$

3. Total One-Way Propagation Delay:

$$
t_{prop} = t_{prop1} + t_{prop2} = 0.005 \text{ seconds} + 0.05 \text{ seconds} = 0.055 \text{ seconds}
$$

4. Round Trip Time (RTT):

$$
RTT = 2 \times t_{prop} = 2 \times 0.055 \text{ seconds} = 0.11 \text{ seconds}
$$


b.  Assume that the source sends 1000 packets each of length 1000 bytes to the destination. How long does it take for the transmission to complete?

1. Packet size:

$$
Packet Size = 1000 \text{ bytes} = 1000 \times 8 = 8000 \text{ bits}
$$

2. Transmission time for one packet on Link 1:

$$
t_{trans} = \frac{Packet Size}{Bandwidth} = \frac{8000 \text{ bits}}{1,000,000 \text{ bits/s}} = 0.008 \text{ seconds}
$$

3. Transmission time for one packet on Link 2:

$$
t_{trans} = \frac{Packet Size}{Bandwidth} = \frac{8000 \text{ bits}}{100,000 \text{ bits/s}} = 0.08 \text{ seconds}
$$

4. Total transmission time for 1000 packets:
- Since the bottleneck is link 2, we consider  its transmission time.

$$
Total Transmission Time = 1000 \times t_{trans2} = 1000 \times 0.08 \text{ seconds} = 80 \text{ seconds}
$$

5. Total Time for Transmission to Complete:

$$
Total Time = Total Transmission Time + t_{prop} = 80 \text{ seconds} + 0.055 \text{ seconds} = 80.055 \text{ seconds}
$$

## Chapter 2: Link Layer and Physical Layer

### Question 1

What's encapsulation as it applies to protocols. Briefly explain.

Encapsulation is the process of wrapping the data with the necessary information. For example, placing the header for each packet is encapsulation like adding destination and source MAC addresses.

### Question 2

Briefly explain the "framing" problem in the link layer and how PPP solves it.

Framing is the process of dividing data streams into frames for transmission.

The problem with framing is that we need to know where each frame starts and ends to properly read the data.

PPP solution:
- Flag sequence to indicate the start and end of the frame (01111110 or 0x7E)
- Escape character (0x7D) is used to escape the flag sequence when it appears in the data field.
- CRC for error detection

### Question 3

In an Ethernet, why does doubling the bit rate (if everything else remains the same) require halving the maximum cable length?

- Doubling the bit rate requires faster signal transitions, which is more likey to degrade over distance. Shorter cable length allows for less signal degradation.
- Ethernet uses CSMA/CD, which requires a station detect collisions with a specific time. Higher bit rate shrink this time window, which is why we need to halve the cable length to keep the same collision detection time.

### Question 4

In a token ring, a station must wait for the token to come around to it before sending. Why is it  not  possible  for  the station  to sense  the ring  and then  start transmitting if there is no traffic?

Token ring network, ensures that only one station can transmit at a time. This helps avoid collisions and ensure fair access to the network for all stations.

It is not possible since without the token, the station will not be able to transmit. This prevents collisions because if they all think no one is transmitting but they want to go there is no type of authority to decide and they will end up colliding. The token is what allows them to transmit and without it they cant.

### Question 5

Smarty Smart thinks that having a minimum frame size is wasteful for Ethernet.  He proposes that the minimum frame size be reduced to 15 bytes, 14 bytes for the header and 1 byte for the payload. Explain why this may not be a good idea.

![[ethernet-header.png]]

Not only does this waste resources since you are just sending 1 byte worth of data for every 14 bytes of headers which will result in slow speeds, but it also hinders collision detection because it needs to be long enough to reach the other station.

### Question 6

In a broadcast channel, the link bandwidth is wasted due to multiple hosts trying to send at once and canceling each other’s communication. A simple model of this problem is that time is divided into discrete slots. If a network has n hosts, and the probability of any single host trying to use a slot is p, what fraction of slots are wasted due to collisions?

![[slotted-aloha.png]]

about 63% because 37% is successful

### Question 7

Explain the following terms: MTU, byte stuffing, bit stuffing:

MTU: Maximum Transmission Unit, the maximum size of a packet in a network.

Byte stuffing: A method used in serial communications to ensure that special characters are not misinterpreted as control characters. It involves inserting an extra byte (typically 0x7D) when a special character is detected.

![[byte-stuffing.png]]

Bit stuffing: A method used in serial communications to ensure that special characters are not misinterpreted as control characters. It involves inserting a bit (typically 0) when a special character is detected (five 1s consecutive)

![[bit-stuffing.png]]

### Question 8

Consider 4 hosts, A, B, C and D attached together using an Ethernet hub into a star topology. Assume that A is sending some data to B. Is it possible for C to send some data to D at the same time? Justify your answer.

No, because the hub will broadcast the signal to all the other hosts. So C and D will receive the signal at the same time.

Hubs do not have the capability to detect collisions.

### Question 9

What's the "type" or "protocolNo" field in a Link Layer (LL) header used for? Do all LLs have to have a "type" field in their headers? If a protocol does NOT have this field, what is the implication?

The "type" or "protocolNo" field in a Link Layer (LL) header is used to indicate the type of protocol being used. It is essentially a code that tells the receiving device what type of data is being sent.

Not all LLs have to have a "type" field in their headers. For example, in a point-to-point link, there is no need for a "type" field since the data is directly sent to the destination.

If a protocol does NOT have this field, the implication it must rely on other methods to identify the payload protocol. 

### Question 10

Consider a link layer that does NOT add error detection/correction bits to the end of its frames? What are the implications of this design?

This implies that the receiving device has to rely on other means of error detection, this could lead to data corruption and loss and increased retransmission of data.

### Question 11

Why is it important for protocols configured on top Ethernet to have a length in their header indicating how long the message is?

To help ensure accurate data delimitation and prevent issues with data being misinterpreted or lost, error detection (CRC) can be used.

### Question 13

What's a MAC address. What is it used for?

A MAC address is a unique identifier assigned to a network interface controller (NIC), it is used to identify the device on the network.

### Question 14

Briefly describe how Ethernet's Carrier Sense Multiple Access/Collison Detection (CSMA/CD) work? What's the advantage of CSMA/CD over CSMA?

CSMA/CD is a network protocol used in Ethernet networks to manage data transmission. It works by having the stations sense the channel for any ongoing transmissions. If the channel is busy, the station will wait for a random amount of time and then check again. If the channel is free, the station will transmit its data. If a collision is detected, the station will wait for a random amount of time and then check again. This process is repeated until the data is successfully transmitted. It will minimize the time wasted on unsuccesful transmissions.

In CSMA listens for a free channel before transmitting, it does not handle collisions.

CSMA/CD detects collisions and stops the transmission.

### Question 15

Briefly describe how channel partitioning MAC algorithms work. Also describe their advantages and disadvantages.

1. Time Division Multiple Access (TDMA):
- channel is divided into time slots, each slot is assigned to a station.
- pro: each station has a dedicated time slot, no collisions.
- con: wasted bandwidth if stations are not active at the same time.
![[channel-partitioning-mac-protocols-tdma.png]]

2. Frequency Division Multiple Access (FDMA):
- channel is divided into frequency bands, each band is assigned to a station.
- pro: simultaneous transmission, no collisions.
- con: limited to fixed stations, no dynamic allocation.
![[channel-partitioning-mac-protocols-fdma.png]]

### Question 16

Briefly explain the difference between serial and parallel communication. Which is preferred in long distance communication?

![[parallel-vs-serial-digital-communication.png]]

Serial communication is preferred in long distance communication because it is more reliable and suitable for long distances.

Parallel communication is preferred in short distance communication because it is faster and more efficient.

### Question 17

Briefly  explain  the  difference  between  synchronous  and  asynchronous 
communication. Which is preferred in long distance communication and why?

![[synchronous-communication.png]]
![[asynchronous-communication.png]]

Asynchronous communication is preferred in long distance communication because it is simpler and more reliable.

### Question 18

Give a list of the 3 types of cables used in communication networks. Which cables do high speed Ethernet use?

1. Twisted Pair (unshielded: commonly used in Ethernet)
2. Coaxial (shielded: used in older TV cables)
3. Fiber Optic (used in long distance communication)

High speed Ethernet uses twisted pair and fiber optic cables.

### Question 19

Briefly explain the difference between modulation and encoding.

Modulation is the process of changing a carrier's signal (amplitude, frequency, phase) to encode data (digital or analog).

Encoding converts data into an analog or digital signal.

### Question 20

Suppose you want to transmit the following 10-bit message "0100101100". 

a.  Suppose you want to protect the message from errors using the CRC polynomial x4 + x3 + x. Use polynomial long division to determine the message that would be transmitted. 
b.  Suppose you want to protect the message from errors using two-dimensional odd parity. Assume that the message is divided into 5-bit chunks for parity computation purposes. Determine the message that would be transmitted.

![[question 2-2.jpg]]

### Question 21
Suppose you want to transmit the following 12-bit message "110010011111". 

a.  Suppose you want to protect the message from errors using a checksum by dividing the message into  4-bit  chunks  and  performing  1s  complement  addition.  Show  the  EDC  bits  that  will  be transmitted. Show your work. 

![[question 3a.jpg]]

b.  Suppose you want to protect the message from errors using one-dimensional even parity. Assume that the message is divided into 4-bit chunks for parity computation purposes. Determine the message that would be transmitted. Show the parity bits for each chunk.

![[question 3b.jpg]]

### Question 22

Suppose  you  want  to  transmit  the  following  4-byte  message  “0xfb  0x7e  0x7d  0xff”  with  0xfb  being transmitted first. 

a.  Assume that the link layer uses byte-counting for framing and has a one-byte length field in the header. Show the bytes transmitted on the wire as hexadecimal numbers. 

On the wire: 0x04 0xfb 0x7e 0x7d 0xff

b.  Assume that the link layer uses byte-stuffing, using 0x7e as the frame delimiter and 0x7d as the escape character. Show the bytes transmitted on the wire. 

message: 0xfb 0x7e 0x7d 0xff
add delimiter: **0x7e** 0xfb 0x7e 0x7d 0xff **0x7e**
add escape character: 0x7e 0xfb **0x7d** 0x7e **0x7d** 0x7d 0xff 0x7e
Final: **0x7e** 0xfb **0x7d** 0x7e **0x7d** 0x7e 0xff **0x7e**

c.  Assume that the link layer uses bit-stuffing, stuffing an extra 0 bit after 5 consecutive 1 bits. Show the bits transmitted on the wire clearly marking the stuffed bits. Recall that a link that uses bit-stuffing still uses 0x7e as the frame delimiter.

0xfb = 1111 1011 = 11111 **0** 011
0x7e = 0111 1110 = 011111 **0** 10
0x7d = 0111 1101 = 011111 **0** 01
0xff = 1111 1111 = 11111 **0** 111
Combine: 11111**0**011011111**0**10 011111**0**0111111**0**111
Then add the delimiters to the front and back:
**0111 1110** 11111**0**011011111**0**10 011111**0**0111111**0**111 **0111 1110**


### Question 23

Consider a broadcast link L1 containing hosts A and B. Further consider another link L2 containing nodes C and D. Answer the following questions: 

a.  Assume L1 and L2 are attached together with a hub. Does host A now need to compete with hosts C and D to gain control of the link? Why or why not? What's your answer if L1 and L2 are attached by a bridge?  

Hub: Yes, host A will need to compete with hosts C and D to gain control of the link because all host share the same collision domain managed by the hub.

Bridge: No, host A will not need to compete with hosts C and D to gain control of the link because they have different collision domains.

b.  Assume L1 and L2 are attached together with a bridge. Assume A sends a packet to B immediately after the links are attached. Does the bridge forward the packet to link L2? Why or why not? 

No, the bridge does not foward the packet to link L2 because both **A** and **B** are on **L1**. Bridge efficiently routes the frame within the correct collision domain based on MAC addresses table.

c.  Assume L1 and L2 are attached together with a bridge. Assume A sends a packet to B immediately after the links are attached. Further assume that B immediately replies back to A. Does the bridge forward the packet to link L2? Why or why not?

No, same as above.

### Question 24

Some network applications are a better match for an Ethernet, some are a better match for an FDDI (token ring) network. Which network would be better match for a remote terminal application (e.g., Telnet) and which would be better for a file transfer application (e.g., FTP)? Give a general explanation for what it is about each of these applications that suggest that one type of network is better match than the other?

Remote terminal application (e.g., Telnet): requires real-time, low latency for interactive use. Ethernet is more suitable for this type of application because it has a lower latency and higher bandwidth.

Ethernet:
- star topology
- CSMA/CD (lower latency)
- ranges from 10 Mbps to 100 Gbps
Advantages: cost-effective, easy to install and configure, widely used.

File transfer application (e.g., FTP): requires high bandwidth and reliability. FDDI is more suitable for this type of application because it has a higher bandwidth and reliability.

FDDI:
- ring topology
- Token Ring
- 100 Mbps (higher bandwidth)
Advantages: high reliability, longer transmission distance, better resistance to electromagnetic interference.

### Question 25

![[ll-pl-questions-9.png]]

a. A sends packet to B
- Bridge will forward packet to link 1 and link 2
- Forwarding table after:
- A: Link 1
- B: Link 2

b. C sends packet to B
- Bridge will forward packet link 3 to link 2
- Forwarding table after:
- A: Link 1
- B: Link 2
- C: Link 3

c. A sends packet to D
- Bridge will forward packet from link 1 to link 3
- Forwarding table after (unchanged):
- A: Link 1
- B: Link 2
- C: Link 3

d. B sends packet to D
- Bridge will forward packet to link 1 and link 3 (D not in table)
- Forwarding table after:
- A: Link 1
- B: Link 2
- C: Link 3
- D: Link 4

e. C sends packet to D
- Bridge is not used (same network)
- Forwarding table after (unchanged):
- A: Link 1
- B: Link 2
- C: Link 3
- D: Link 4


### Question 26
![[question-10.png]]
![[spanning-tree.jpg]]
![[spanning-tree-table.jpg]]


### Question 27

Determine the maximum length of an Ethernet cable in kilometers with CSMA/CD for transmitting data at a rate of 500 Mbps with frame size of 10.000 bits. Assume that the signal speed in the cable is 2x105 km/sec. Show your work.

Given:
- Data rate: 500 Mbps
- Frame size: 10,000 bits
- Signal speed: 2x10^5 km/sec

To find the maximum cable length, we need to determine the maximum transmission time for a frame to travel from one end to the other and back. This is given by:

$$
t_{trans} = \frac{Frame Size}{Data Rate} = \frac{10,000 bits}{500 \times 10^6 bits/sec} = 0.02 milliseconds
$$

Calculate the maximum Round-Trip Time (RTT):
RTT <= t_trans

$$
t_{prop} = \frac{RTT}{2} = \frac{0.02 ms}{2} = 0.01 ms
$$

Calculate maximum length of cable:

$$
Length = t_{prop} \times Signal Speed = 0.01 ms \times 2x10^5 km/sec = 2 km
$$

### Question 28

A link layer protocol with CSMA/CD in the MAC layer is running at 1 Gbps over a 1km cable. The signal speed in the cable is 2x105 km/sec. What should be the minimum frame size for the link layer? Show your work

Given:
- Data rate: 1 Gbps
- Cable length: 1 km
- Signal speed: 2x10^5 km/sec

Calculate RTT:

$$
RTT = 2 \times \frac{Distance}{Signal Speed} = 2 \times \frac{1 km}{2x10^5 km/sec} = 0.01 ms
$$

Calculate minimum frame size:
Transmission time of the frame must be less than the RTT:

$$
t_{trans} <= RTT
$$

Set t_{trans} = RTT:

$$
\frac{Frame Size}{1 \times 10^9 bits/sec} = 10 \times 10^{-6} sec
$$

Solve for frame size:

$$
Frame Size = 10 \times 10^{-6} sec \times 1 \times 10^9 bits/sec = 10,000 bits
$$

