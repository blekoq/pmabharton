from scapy.all import *

ports=[25,80,53,443,445,8080,3306,8442,9000]
for x in range(0,len(ports),1):
    print(ports[x])