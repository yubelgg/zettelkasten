---
id: netmask
aliases: []
tags: []
---

# netmask

given an ip address of networkID/hostID

netmask of ip is putting "1"s in the networkID and "0"s in the hostID

IP subnet 200.23.16.0/23
11001000 00010111 00010000 00000000

netmask: 11111111 11111111 11111110 00000000 = 255.255.254.0

## getting ip subnet and hostID

given ip address and netmask
perform bitwise AND

networkID = ip address & netmask
hostID = ip address & ~netmask

![[ip subnet & hostid.png]]

![[ip subnet & hostid 2.png]]