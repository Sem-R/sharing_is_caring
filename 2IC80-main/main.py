import argparse

ipAttack = "192.168.56.103"
ipVictim = "192.168.56.101"
ipServer = "192.168.56.102"

macAttack = "08:00:27:d0:25:4b"
macVictim = "08:00:27:b7:c4:af"
macServer = "08:00:27:cc:08:6f"

INTERFACE = "enp0s3"

tools = ["arp_spoof", "dns_spoof", "dns_poison"]


def main(args):
    print(f"Running {args.tool}...")

    if args.tool == "arp_spoof":
        import arpSpoof

        print(f"Interface: {args.interface}")
        print(f"Victim IP: {args.ipVictim}")
        print(f"Victim MAC: {args.macVictim}")
        print(f"Server IP: {args.ipServer}")
        print("NOTE: Make sure to turn ip forwarding on")

        arpSpoof.execute(args.interface, ipVictim, macVictim, ipServer)
    # elif args.tool == "dns_spoof":
    # import dnsSpoof

    # dnsSpoof.execute(INTERFACE, ipVictim, macVictim, ipServer)

    else:
        print("Tool not found.")
        print("Available tools: ", tools)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("--tool", type=str, help="tool name")
    parser.add_argument("--interface", type=str, help="interface name")
    parser.add_argument("--ipVictim", type=str, help="victim ip")
    parser.add_argument("--macVictim", type=str, help="victim mac")
    parser.add_argument("--ipServer", type=str, help="server ip")

    args = parser.parse_args()
    main(args)
