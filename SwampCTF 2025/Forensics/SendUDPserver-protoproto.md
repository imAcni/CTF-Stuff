In the pcap file, the user sends a certain hex code to the server, in which the server responds back with a flag (fake). 

Solution: send the nc server the same hex code and relay what the server sends back.

```
import socket 
server = "chals.swampctf.com" 
port = 44254
payload = b"\x02\x08\x66\x6c\x61\x67\x2e\x74\x78\x74"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(payload, (server, port))
    response, addr = s.recvfrom(4096)
    print("HEX response:", response.hex())
    print("Decoded response:", response.decode(errors='ignore'))
s.close()
```
