# Fundamentos-de-Redes

Mini-projeto 2018-2019

Objective 1: Definition of the IPv4 and IPv6 addressing scheme of a business network. Configure the
company communication network. Note that x0x1x2x3x4 and x5x6x7x8x9 are the digits of your UA numbers.
Deadline: 8th November

Description:
Consider the communication network of a company depicted in the following figure:
(a) it contains the IPv4 public class C addresses 200.1x3x4.1x8x9.0/24;
(b) it contains the IPv6 global address 2001:x2x7::/60;
(c) it internally uses the range of IPv4 private class C address 10.1x4x9.0.0/16 (several class C networks);
(d) every local network has a private IPv4 and an IPv6 global network;
(e) considering the public IPv4 addressing, there are several equipments in the network that need public addressing: 55 servers at the DMZ, 45 servers at the Internal Datacenter, 5 PCs in the Design VLAN, 9
PCs in the Admin VLAN, 48 PCs in the Marketing VLAN, Router1 needs 11 IPv4 public addresses to configure NAT/PAT mechanisms.
(f) An already existent network (Old Building) has the IPv4 network 192.168.0.0/23 and the terminals must maintain their IPv4 addresses. IPv6 connectivity is not required in the Old Building.

Define the private and public IPv4 sub-networks, and the global IPv6 networks with its network address and mask. Define also the range of IP addresses of the terminals and servers.

Objective 2: Build, test and run the network in GNS3.
Deadline: 3rd January

The Internet is simulated with the IPv4 network 100.0.0.0/24 and the IPv6 network 3000:A:A:A::/64.
1. Configure, in Layer 2 and Layer 3 switches, the different VLANs and the access and inter-switch/trunk ports.
2. Configure the IPv4 and IPv6 addressing in the different equipments.
3. Include and configure (at least) 1 terminal in each VLAN with the corresponding IP addresses and gateway(s).
4. In Router 1, configure the NAT/PAT mechanisms in an appropriate way. Use the range of public IPv4 addresses to configure the translation with the private network.
5. DHCP server must be configured in Router A to assign private addresses to the Old Building equipments.
6. Configure the IPv4 and IPv6 internal routing using an internal routing protocol.
7. Router 1 should announce a default route, both in IPv4 and IPv6.
8. Place a terminal in the “Internet” to test IPv4 and IPv6 connectivity.
9. Develop e client-server application (in python using sockets) that allows a client to periodically notify a central server of its CPU utilization and percentage of memory in use. 
[This task does not have to be integrated in GNS3, but a demonstration of the application in use must be possible.]

Extra Tasks
Configure an IPv4 DHCP server in a single VLAN (you may choose it).
Configure a HTTP/HTTPS server.
Configure a DNS server.
