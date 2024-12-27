---
id: midterm-2
aliases: []
tags: []
---

# Review

> [!question] why is it not possible to build a global network such as the internet using just [[link-layer]] switches?
> no since L2 switched network does not scale
>
> 4 problems:
>
> - can only switch certain link layer technology together
> - switches use a MAC address table, becomes too large for each host
> - change in network topology requires new spanning tree
> - deliver packets to all host on network, sending to one far is not the best

> [!question] netmask is 255.255.128.0 and IPv4 address is 23.45.65.66
> what is IP subnet?
> netmask: 11111111 11111111 10000000 00000000
> IP addr: 00010111 00101101 01000001 00000110
> IP sbnt: 00010111 00101101 00000000 00000000
> IP subnet: 23.45.0.0
>
> how many hosts can you connect?
> netmask: 11111111 11111111 10000000 00000000
> ~netmasks: 00000000 00000000 01111111 11111111
> IP addr: 00010111 00101101 01000001 00000110
> host id: 00000000 00000000 01000001 00000110
> host id: 16646

> [!question] what is the disadvantage of placing IP version number other than the first byte in IP header?
> it will reduce performance since it would add time to process the packet and interpret it

> [!question] network application that prefers datagram based over virtual cicruit network?
> datagram based networking: video streaming since it allows timely delivery of packets and even if packets are lost it can get them again allowing for smooth playback
>
> virtual cicruit network: file transfer since it needs to have a dedicated connection and reliable

> [!question] in virtual cicruit is it possible for packets to arrive out of order?
>
> no since in virtual cicruit they take a single path so it has to go in order, it doesn't contain header to know what order it should be

> [!question] how are we running out of ip addresses?
>
> classful addressing is inefficient when it comes to reserving space, you can have 65k host but only use 2k

> [!question] what is CIDR?
>
> a method for allocating IP addresses that is for efficent than classful
> For example, 192.0.2.0/24 is an IPv4 CIDR address where the first 24 bits, or 192.0.2, is the network address

> [!question] The IPv6 header is 40 bytes long, as opposed to 20 bytes of IPv4 header, while the address size has quadrupled. What functionality has disappeared from the fixed header?
>
> in [[IPv4-IPv6|IPv6]] there is no checksum field i.e no error detection, done on link layer

> [!question] how many bits does IPv4 address have and what is IP subnet?
>
> IPv4 has 32-bits, IP subnet is a segmented piece of a larger network that allows variation of networks

> [!question] how many bits does IPv6 address have and how many bits are used for the interface?
> ![[IPV6.png]]
> IPv6 has 128-bits
> |<------ Network Prefix ------>|<------ Interface ID ------>|
> | 64 bits | 64 bits |
> 2001:0db8:85a3:0000:0000:8a2e:0370:7334

> [!question] List 2 reasons why an organization might have assigned private IPv4 addresses to its hosts.
>
> it reduces the need for multiple public IPs so its more cost effective, and adds a layer of protection by hiding internal network structure

> [!question] What’s a Link Local IPv4 address. What is it used for?
>
> it is an IP range from 169.254.0.0 to 169.254.255.255 for communication only on the local network segment a device is connected to.
>
> allows communication with each other on the same network even when they cant get a global IP address
>
> auto assign link local address if it cant get a IP address

> [!question] What’s a loopback IPv4 address. Is it possible for a packet sent to the loopback IPv4 address to leave the host and sent over the network?
>
> loopback is 127.0.0.0 to 127.255.255.255, 127.0.0.1 is localhost
>
> it is not possible to possible to send over the network, RFC 1122 mandates it so that testing on localhost is secure

> [!question] Give an explanation of why IPv4 does reassembly at the destination rather than at routers.
>
> if you store at the routers you will lost performance and wont be efficent since each packet takes different routes

> [!question] Explain the difference between how IPv4 and IPv6 handle passing packets through sub-networks with MTU (Maximum Transmission Units) smaller than the originating sub-network could handle. Make sure to explain the advantages of each approach.
>
> IPv4 if a packet is larger than the MTU, it traverses the intermediate router with fragments that can fit the MTU.
> it then gets reassembled at the destination
>
> IPv6 relies on the sending host to determine the MTU size, and if its too big it wont send.
> this decreases processing time and lowers memory usage, but also more secure (fragment based attacks)

> [!question] Briefly describe the differences between IPv4 and IPv6 fragmentation.
>
> IPv4 will fragment the packet if size exceeds sub-networks MTU, and reassembled at the router
> IPv6 routers does not segment, only the source host does, and it gets reassembled at the destination host

> [!question] What's an IPv6 anycast address? What is it used for?
>
> it is a type of ip address that is assigned to multiple interfaces (different nodes) within the same network.
> so when a packet is sent it is delivered to the nearest destination
>
> can be used for load balancing, redundancy and high avaliability

> [!question] IPv4 checksum, which is computed over the IPv4 header, is used to protect IPv4 header against bit errors. Why did IPv6 remove this checksum from its header?
>
> the designers consider the error detection on the upper (TCP and UDP) and link layer (ethernet) were good enough
> this is to speed up the packet forwarding

> [!question] List 2 reasons why there are separate intra-domain and inter-domain routing protocols?
>
> for scale since internet routing table can get large and bulky if we seperate them each protocols will handle less information
> optimized for smaller controlled environment for intra domain
> desiged for vast and dynamic internet for inter domain
>
> for policy:
> intra domain focused on optimal path selection based on bandwidth, delays, and hops
> inter domain allows the organization to implement complex routing policies based on business relationship, security

> [!question] What is "count-to-infinity" problem in distance vector protocols? How does RIP solve this problem?
>
> when routers continuously increment their distance metrics to a destination after a network failure, causing routing loops
>
> the routing information protocol may introduce misleading routing information into the table, so it sets the max hops to 16
>
> it is consider unreachable when hops are over 16

> [!question] What's IGMP? What is it used for? Briefly describe.
>
> Internet Group Management Protocol lets multiple devices to share the same IP address to get the same data
>
> used for video games, video conferencing, live streaming video or audio

> [!question] Is it required for a node to join a multicast group to be able to send a packet to that group?
>
> no it doesn't, you are only required to join if you want to recieve data from that multicast group

> [!question] What is the purpose of IP multicasting? Briefly explain
>
> the purpose is to send packets to multiple recievers without creating seperate copies of the packets to optimize bandwidth usage

> [!question] What is the range of IPv4 multicast addresses?
>
> IPv4 multicast falls under [[classful|class D]] range
> range from 224.0.0.0 to 239.255.255.255
>
> - 224.0.0.0 to 224.0.0.255: Reserved for local subnet multicast and protocols like OSPF (Open Shortest Path First) and RIP (Routing Information Protocol).
> - 224.0.1.0 to 238.255.255.255: Allocated for global multicast applications, such as streaming media and IPTV.
> - 239.0.0.0 to 239.255.255.255: Designated for administratively scoped multicast, similar to private IP address ranges, used within organizations or specific networks.

> [!question] Explain how an IPv4 multicast IP address maps to an Ethernet MAC address? What’s the MAC Address prefix used for IP multicast?
>
> ![[mac-broadcast-multicast-bit.png]]
> in the first octal, bit 0 is reserved for the traffic
>
> - 0 for unicast
> - 1 for broadcast or multicast
>
> ![[multicast-mac-address-23-bit.png]]
> for layer 2, we have reserved prefix for multicast
> the first 24 bit: 01-00-5E
> remaining bit is 24 but only 23 bit is usable
>
> since multicast is only 23 bits and IPv4 is 32 bits
> ignore the first 9 bits
> example: 224.0.1.1
> binary: 11100000 00000000 00000001 00000001
> lower 23 bit: 0000000 00000001 0000001
>
> map to ethernet mac address
> append the lower 23 bit to the prefix after converting binary to hexadecimal
> lower 23 bit: 0000000 00000001 00000001 -> 00:01:01
> mac address: 01:00:5E:00:01:01

> [!question] What’s the destination MAC address of an IPv4 packet sent to 227.23.245.2?
>
> prefix is 01:00:5E
> 227.23.245.2
> binary: 11100011 00010111 11110101 00000010
> lower 23:0010111 11110101 00000010
> binary to hex: 17:F5:02
> mac address: 01:00:5E:17:F5:02

> [!question] Compare and contrast the use of multicast, unicast, and broadcast transmission methods in IPv4. Discuss why IP multicast is more efficient than IP broadcast assuming that there are handful of receivers on the link?
> ![[multicast-vs-broadcast.png]]

> [!question] you are a network administrator, given 182.15.11.0/24 IP address range. you are asked to setup 4 IP subnets?
>
> **classful**
>
> | class | starting bits |
> | :---: | :-----------: |
> |   A   |    0 - 127    |
> |   B   |   127 - 191   |
> |   C   |   192 - 223   |
> |   D   |   224 - 239   |
> |   E   |   240 - 255   |
>
> | Prefix size |  Network mask   | Usable hosts per subnet |
> | :---------: | :-------------: | :---------------------: |
> |   class A   |
> |     /1      |    128.0.0.0    |      2,147,483,646      |
> |     /2      |    192.0.0.0    |      1,073,741,822      |
> |     /3      |    224.0.0.0    |       536,870,910       |
> |     /4      |    240.0.0.0    |       268,435,454       |
> |     /5      |    248.0.0.0    |       134,217,726       |
> |     /6      |    252.0.0.0    |       67,108,862        |
> |     /7      |    254.0.0.0    |       33,554,430        |
> |     /8      |    255.0.0.0    |       16,777,214        |
> |   class B   |
> |     /9      |   255.128.0.0   |        8,388,606        |
> |     /10     |   255.192.0.0   |        4,194,302        |
> |     /11     |   255.224.0.0   |        2,097,150        |
> |     /12     |   255.240.0.0   |        1,048,574        |
> |     /13     |   255.248.0.0   |         524,286         |
> |     /14     |   255.252.0.0   |         262,142         |
> |     /15     |   255.254.0.0   |         131,070         |
> |     /16     |   255.255.0.0   |         65,534          |
> |   class C   |
> |     /17     |  255.255.128.0  |         32,766          |
> |     /18     |  255.255.192.0  |         16,382          |
> |     /19     |  255.255.224.0  |          8,190          |
> |     /20     |  255.255.240.0  |          4,094          |
> |     /21     |  255.255.248.0  |          2,046          |
> |     /22     |  255.255.252.0  |          1,022          |
> |     /23     |  255.255.254.0  |           510           |
> |     /24     |  255.255.255.0  |           254           |
> |     /25     | 255.255.255.128 |           126           |
> |     /26     | 255.255.255.192 |           62            |
> |     /27     | 255.255.255.224 |           30            |
> |     /28     | 255.255.255.240 |           14            |
> |     /29     | 255.255.255.248 |            6            |
> |     /30     | 255.255.255.252 |            2            |
> |     /31     | 255.255.255.254 |            0            |
> |     /32     | 255.255.255.255 |            0            |

> > [!question] how many bits would you use for subnetid?
> > we want 4 IP subnets, so 2$^2$ subnets, 2 bits, these will be the 25 and 26 bits (part of the host)
> > what it your new netmask?
> > class c since it starts with
> > so first two octets are our network bits
> > old: 182.15.11.0/24 -> 11111111.11111111.11111111.00000000 (netmask)
> > new: 182.15.11.0/26 -> 11111111.11111111.11111111.11000000 (netmask)
> > R = remaining ones after network bits
> > subnets = 2$^{R}$ -> 2$^{2}$
> > host = 2$^6$ the no. of zeros - 2
> > we have 2$^{2}$ subnets and each have 2$^6$ - 2 hosts?
> > list subnets:
> >
> > | Subnet Number | Network Address  |        Usable IP range        |
> > | :-----------: | :--------------: | :---------------------------: |
> > |       0       |  182.15.11.0/26  |  182.15.11.0 - 182.15.11.63   |
> > |       1       | 182.15.11.64/26  | 182.15.11.64 - 182.15.11.127  |
> > |       2       | 182.15.11.128/26 | 182.15.11.128 - 182.15.11.191 |
> > |       3       | 182.15.11.192/26 | 182.15.11.192 - 182.15.11.255 |
>
> > [!question] what is the maximum no. of host that can be attached to each IP?
> > we have 6 bits remaining (32 - 26)
> > each either 0 or 1: 2$^6$ = 64 - 2 = 62
> > substract 2 for:
> >
> > - one address needs all zeros (network id)
> > - one address needs all ones (broadcast)

> [!question] like above, given 10.10.96.0/20 private address range. setup 16 IPv4 subnets
>
> > [!question] how many bits for subnet id? what is your netmask? list IP subnets?
> > how many bits: 2$^4$ = 16, so 4 bits, the beginning ones in host
> > class C
> > old: 10.10.96.0/20
> > new: 10.10.96.0/24 00001010.00001010.01100000.00000000
> > list of IP subnets:
> >
> > | Subnet Number | Network Address |       Usable IP Range       |
> > | :-----------: | :-------------: | :-------------------------: |
> > |       1       |  10.10.96.0/24  |  10.10.96.1 - 10.10.96.254  |
> > |       2       |  10.10.97.0/24  |  10.10.97.1 - 10.10.97.254  |
> > |       3       |  10.10.98.0/24  |  10.10.98.1 - 10.10.98.254  |
> > |       4       |  10.10.99.0/24  |  10.10.99.1 - 10.10.99.254  |
> > |       5       | 10.10.100.0/24  | 10.10.100.1 - 10.10.100.254 |
> > |       6       | 10.10.101.0/24  | 10.10.101.1 - 10.10.101.254 |
> > |       7       | 10.10.102.0/24  | 10.10.102.1 - 10.10.102.254 |
> > |       8       | 10.10.103.0/24  | 10.10.103.1 - 10.10.103.254 |
> > |       9       | 10.10.104.0/24  | 10.10.104.1 - 10.10.104.254 |
> > |      10       | 10.10.105.0/24  | 10.10.105.1 - 10.10.105.254 |
> > |      11       | 10.10.106.0/24  | 10.10.106.1 - 10.10.106.254 |
> > |      12       | 10.10.107.0/24  | 10.10.107.1 - 10.10.107.254 |
> > |      13       | 10.10.108.0/24  | 10.10.108.1 - 10.10.108.254 |
> > |      14       | 10.10.109.0/24  | 10.10.109.1 - 10.10.109.254 |
> > |      15       | 10.10.110.0/24  | 10.10.110.1 - 10.10.110.254 |
> > |      16       | 10.10.111.0/24  | 10.10.111.1 - 10.10.111.254 |
>
> > [!question] what is the maximum no. of host for each IP subnet?
> > usable bits: 32 - 24 = 8
> > 2$^8$ = 256 - 2 = 254 hosts

> [!question] given 10.10.212.0/24 private address range. subnet this range so it can have up to 30 subnets.
>
> > [!question] how many bits for host and subnet id? whats your netmask?
> >
> > need how many bits to create 30 host:
> > $$ 2^x - 2 >= 30 $$
> > $$ 2^x >= 32 $$
> > $$ 2^5 >= 32 $$
> > host bits needs to be at least 5
> > network bits are 32 - 24 = 8
> > 8 - 5 = 3 bits for the subnet bits
> > new netmask = 10.10.212.0/27 -> 11111111.11111111.11111111.11100000
> > we can create 2$^3$ subnets = 8
> > we can create 2$^5$ host - 2 = 30

> [!question] IPv4 address of host is 192.168.27.154/26. what is the netmask, ip subnets, what is the netmark for each and how many host for each subnet?
> netmask: 11111111.11111111.11111111.11000000 or 255.255.255.192
> IPv4 ad: 11000000.10101000.00011011.10011010
> IP sbnt: 11000000.10101000.00011011.10000000
> IP subnet: 192.168.27.128/26
> class c so 2 remainint bits
> how many host: 32 - 26 = 6 => 2$^6$ - 2 = 62 hosts
> subnet broadcast (host bits are all ones):
> 11000000.10101000.00011011.10111111 or 192.168.27.191

> [!question] organization is given IPv4 address range 45.77.0.0/16 and is asked to create 64 IPv4 subnets. what's the netmask for each subnet, how many hosts can each have?
> we want 64 subnets:
> 2$^x$ - 2 >= 64
> 2$^6$ >= 62, so we have 6 host bits
> new netmask is 16 + 6 = 22
> 45.77.0.0/22
> no. of hosts is 32 - 22 = 10 => 2$^{10}$ - 2 = 1022

> [!question] netmask of one of its IPv4 subnets: 255.255.248.0, how many hosts can be attached?
> netmask is 11111111.11111111.11111000.00000000
> host bits is 32 - 21 = 11
> 2$^{11}$ - 2 = 2046

> [!question] two hosts H1 and H2 follows: H1's IP address is 203.197.2.53 and its netmask is 255.255.128. H2's IP address is 203.197.75.201 and netmask is 255.255.192.0.
>
> > [!question] from H1 perspective, is H2 on the same IP subnet?
> > 255.255.128.0 is /17
> > apply bitwise and on the netmask
> > 11111111.11111111.10000000.00000000 <- netmask
> > 11001011.11000101.00000010.00110101 <- H1
> > 11001011.11000101.00000000.00000000 <- subnet ip for H1
> > 11001011.11000101.01001101.11001001 <- H2
> > 11001011.11000101.00000000.00000000 <- subnet ip for H2
> > from H1's perspective they both are on the same subnet
>
> > [!question] from H2 perspective is H1 on the same subnet
> > 11111111.11111111.11000000.00000000 <- netmask
> > 11001011.11000101.00000010.00110101 <- H1
> > 11001011.11000100.00000000.00000000 <- subnet ip for H1
> > 11001011.11000101.01001101.11001001 <- H2
> > 11001011.11000101.01000000.00000000 <- subnet ip for H2
> > from H2's perspective they are not on the same subnet

> [!question] Two hosts H1 and H2 are configured as follows: H1’s IP address is 10.10.100.120 and its netmask is 255.255.128.0. H2’s IP address is 10.10.100. 129 and its netmask is 255.255.128.0. Are these two hosts on the same IP subnet? Show your work.
> to check we do bitwise and on the IP and netmask to get subnet IP
> 11111111.11111111.10000000.00000000 <- netmask
> 00001010.00001010.01100100.01111000 <- H1
> 00001010.00001010.00000000.00000000 <- subnet ip for h1
> 00001010.00001010.01100100.10000001 <- H2
> 00001010.00001010.00000000.00000000 <- subnet ip for h2
> they are in the same subnet

> [!question] Suppose a router has built up the routing (forwarding) table shown below. The router can deliver packets directly over interfaces 1 and 2, or it can forward packets to routers R1 or R2. Describe what the router does with a packet addressed to each of the following destinations. You must justify your answer. A simple sends here/there answer is NOT acceptable!
> ![[routing table q10.png]]
> 255.255.255.128/25
> 255.255.255.224/27
>
> finding the range for each subnet
> range for first subnet is 2$^{32 - 25}$ = 128
> range for second subnet is 2$^{32 - 27}$ = 32
> range for third subnet is 2$^{32 - 27}$ = 32
> 122.15.10.0 -> 122.15.10.128
> 122.15.10.96 -> 122.15.10.128
>
> do bitwise and to find out what there next hop is
>
> > [!question] a
> > 01111011.00001111.00001010.10000100 <- 122.15.10.132
> > 11111111.11111111.11111111.11100000 <- longest subnet length
> > 01111011.00001111.00001010.10000000
> > 122.15.10.128 <- goes to interface 1 since it matches and has the longest prefix
>
> > [!question] b
> > 01111011.00001111.00001010.01101100 <- 122.15.10.108
> > 11111111.11111111.11111111.11100000 <- longest subnet length
> > 01111011.00001111.00001010.01100000 <- 122.15.10.96
> > 122.15.10.96 <- goes to interface 2 since it matches and it has the longest prefix
>
> > [!question] c
> >
> > 01111011.00001111.00001010.00110110 <- 122.15.10.55
> > 11111111.11111111.11111111.10000000 <- longest subnet length
> > 01111011.00001111.00001010.00000000 <- 122.15.10.0
> > 122.15.10.0 matchs R1
>
> > [!question] d
> > 01111011.00001111.00001010.00100000 <- 122.15.10.32
> > 11111111.11111111.11111111.10000000 <- longest subnet length
> > 01111011.00001111.00001010.00000000 <- 122.15.10.0
> > 122.15.10.0 matchs R1
>
> > [!question] e
> > 122.15.11.32 will go to R2 since it doesn't match with any other subnet

> [!question] What’s the Address Resolution Protocol (ARP) and what is it used for. Does ARP run over the link layer or on top of IPv4? Briefly explain.
> used to map mac address (physical) to known ip address to be used on a local network communication
> ARP runs over the link layer and not the IPv4 layer since IPv4 is needed for communication

> [!question] What’s the Internet Control Message Protocol (ICMP) and what is it used for. Does ICMP run over the link layer or on top of IPv4? Briefly explain.
> internet control message protocol is used for error reporting and diagnositics on a network, TTL and checksum are examples.
> ICMP runs over the IPv4 layer since it relies on the ip to delivery messages
