import pyshark


def print_packet_summary(pkt):
    print(4 * ' ', str(pkt))


# CAPTURE EVERYTHING AND PRINT PACKET SUMMARIES
print("\n\t\t\t+++ Packet summaries +++\n")
capture = pyshark.LiveCapture(interface='ens33', only_summaries=True)
capture.sniff(packet_count=5) # It starts to capture here, waits until the 
# all the packets counted arrives
for packet in capture:
    print_packet_summary(packet)


# CAPTURE DNS AND PRINT PACKETS
print("\n\t\t\t+++ DNS packet summaries +++\n")
capture = pyshark.LiveCapture(interface='ens33', only_summaries=True, 
                              bpf_filter='udp port 53')
capture.sniff(packet_count=5)
for packet in capture:
    print_packet_summary(packet)

# CAPTURE AND HANDLE HTTPS PACKETS 
# After a packet arrives it is handled
# iterate through the packets, passing in a function to apply to each packet
print("\n\t\t\t+++ Print packets as they are detected +++\n")
capture = pyshark.LiveCapture(interface='ens33', only_summaries=True, 
                              bpf_filter='tcp port https')
capture.apply_on_packets(print_packet_summary, packet_count=5)

# CAPTURE AND PRINT COMPLETE PACKETS
print("\n\t\t\t+++ All packets, complete +++\n")
capture = pyshark.LiveCapture(interface='ens33')
capture.sniff(packet_count=5)
for packet in capture:
    print(packet)
