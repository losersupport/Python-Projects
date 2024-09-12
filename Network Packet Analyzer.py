from scapy.all import sniff, IP, TCP, Raw

def packet_handler(packet):
    print(f"[*] Packet captured:")
    print(f"    Source IP: {packet[IP].src}")
    print(f"    Destination IP: {packet[IP].dst}")
    print(f"    Protocol: {packet[IP].proto}")

    if packet.haslayer(TCP):
        print(f"    Source Port: {packet[TCP].sport}")
        print(f"    Destination Port: {packet[TCP].dport}")
    else:
        print("    No TCP layer in this packet")

    if packet.haslayer(Raw):
        raw_data = packet[Raw].load
        print(f"    Payload: {raw_data}")
    else:
        print("    No raw data in this packet")

    print("-" * 50)

def start_sniffing(interface):
    print(f"[*] Starting packet sniffing on interface {interface}...")
    sniff(iface=interface, filter="ip", prn=packet_handler)

if __name__ == "__main__":
    interface = input("Enter the network interface to sniff on (e.g., WiFi): ")
    start_sniffing(interface)

