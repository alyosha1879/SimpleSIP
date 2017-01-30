import netifaces

def getLocalAddrList():
    for iface_name in netifaces.interfaces():
        for key in netifaces.ifaddresses(iface_name).keys():
            # Each of the numbers refers to a particular address family.
            # 18 is AF_LINK.(link layer interfaces, e.g. Ethernet.)
            # 2 is AF_INET.(IPv4)
            # 30 is AF_INET6.(IPv6)
            if key == 2:               
                print netifaces.ifaddresses(iface_name)[key][0]['addr']

getLocalAddrList()

