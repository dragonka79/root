import pyshark


def print_packet_summary(pkt):
    print("    ", str(pkt)[:120])


# CAPTURE EVERYTHING AND PRINT PACKET SUMMARIES
print("\n----- Packet summaries -----\n")
capture = pyshark.LiveCapture(interface='ens33', only_summaries=True)
capture.sniff(packet_count=10) # It starts to capture here
for packet in capture:
    print_packet_summary(packet)

# CAPTURE DNS AND PRINT PACKETS
print("\n----- DNS packet summaries -----\n")
capture = pyshark.LiveCapture(interface='ens33', only_summaries=True, 
                              bpf_filter='udp port 53')
capture.sniff(packet_count=10)
for packet in capture:
    print_packet_summary(packet)

# CAPTURE AND PRINT COMPLETE PACKETS
print("\n\n----- All packets, complete -----\n")
capture = pyshark.LiveCapture(interface='ens33')
capture.sniff(packet_count=10)
for packet in capture:
    print(packet)

# CAPTURE AND HANDLE HTTPS PACKETS AS THEY ARRIVE
print("\n\n----- Print packets as they are detected -----\n")
capture = pyshark.LiveCapture(interface='ens33', only_summaries=True, 
                              bpf_filter='tcp port https')
capture.apply_on_packets(print_packet_summary, packet_count=10)

# CAPTURE AND HANDLE PACKETS AS THEY ARRIVE USING LAMBDA
print("\n\n----- Print packets as they are detected (lambda version) -----\n")
capture = pyshark.LiveCapture(interface='ens33', only_summaries=True, 
                              bpf_filter='tcp port https')
capture.apply_on_packets(lambda pkt: print("lambda    ", str(pkt)[:114]), 
                         packet_count=10)

# USE sniff_continuously() TO CAPTURE PACKETS AND HANDLE AS THEY ARRIVE
# Same as .sniff, but using generator
print("\n\n----- Print packets as they arrive with sniff_continuously() -----\n")
capture = pyshark.LiveCapture(interface='ens33', only_summaries=True, 
                              bpf_filter='tcp port https')
for packet in capture.sniff_continuously(packet_count=10):
    print_packet_summary(packet)

# ALLOW USER TO ENTER BPF FILTER
print("\n\n----- Input and use BPF filter from user -----\n")
while True:

    bpf_filter = input("\n\nEnter BPF filter:  ")
    if not bpf_filter:
        break

    print(f"\n----- capturing packets with BPF filter: {bpf_filter}")
    capture = pyshark.LiveCapture(interface='ens33', only_summaries=True, 
                                  bpf_filter=bpf_filter)
    try:
        capture.apply_on_packets(print_packet_summary, packet_count=10)
    except KeyboardInterrupt as e:
        continue