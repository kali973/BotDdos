import nmap


def scan_ports(ip_range, port_range):
    # initialize the port scanner
    nmScan = nmap.PortScanner()

    # scan the specified range of IP addresses for the specified range of ports
    nmScan.scan(ip_range, port_range)

    # run a loop to print all the found result about the ports
    for host in nmScan.all_hosts():
        print('Host : %s (%s)' % (host, nmScan[host].hostname()))
        print('State : %s' % nmScan[host].state())
        for proto in nmScan[host].all_protocols():
            print('Protocol : %s' % proto)
            lport = nmScan[host][proto].keys()
            lport = sorted(lport)
            for port in lport:
                print('port : %s\tstate : %s' % (port, nmScan[host][proto][port]['state']))
                print('----------------------')


# Example usage of the function
ip_range = input("Enter the range of IP addresses to scan (e.g. 192.168.0.1-255): ")
port_range = input("Enter the range of ports to scan (e.g. 21-443): ")
scan_ports(ip_range, port_range)
input("Press Enter to continue...")
