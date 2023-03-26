import scapy.all as scapy
import argparse


def get_argements():
    parser = argparse.ArgumentParser()
    parser.add_argument("--t", "--target", dest="target", help="Target IP/ IP range")
    options = parser.parse_args()
    return options


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    client_list = []
    for elem in answered:
        client_dict = {"ip": elem[1].psrc, "mac": elem[1].hwsrc}
        client_list.append(client_dict)
    return client_list


def print_result(result_lists):
    print("IP\t\t\tMAC Address\n---------------------------------------------------------------")
    for client in result_lists:
        print(client["ip"] + "\t\t" + client["mac"])


options = get_argements()
scan_result = scan(options.target)
print_result(scan_result)
