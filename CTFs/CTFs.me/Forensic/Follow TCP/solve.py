from pcapng import FileScanner
from scapy.all import rdpcap

"""with open('out.pcapng', 'rb') as f :
    scannar = FileScanner(f)
    for block in scannar :
        if block.magic_number == 6 :
            print block.packet_data"""

data = ''

scapy_cap = rdpcap('out.pcapng')
for packet in scapy_cap :
    if 'Raw' in packet.summary() :
        data += str(packet['Raw'])

with open('out', 'wb') as f :
    f.write(data)