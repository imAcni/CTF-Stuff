import socket # Import the socket library to handle network communication
# Define the server address and port to connect to
server = "chals.swampctf.com" # The hostname of the CTF challenge server
port = 44254 # The port number specified in the challenge UDP port)
# Define the payload to request "flag.txt" from the server
# - b"\x02" is the command code (possibly indicating a file request)Forensics  Proto Proto1
# - b"\x08" is the length of the filename 8 bytes for "flag.txt")
# - b"\x66\x6c\x61\x67\x2e\x74\x78\x74" is "flag.txt" in HEX ASCII encoding)
payload = b"\x02\x08\x66\x6c\x61\x67\x2e\x74\x78\x74"
# Create a UDP socket object
# - socket.AF_INET specifies the IPv4 address family
# - socket.SOCK_DGRAM specifies UDP (datagram) protocol
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Send the payload to the server via UDP
# - sendto() sends the data to the specified (server, port) tuple
s.sendto(payload, (server, port))
# Receive a response from the server
# - recvfrom(4096) waits for up to 4096 bytes of data and returns the response and sender's address
response, addr = s.recvfrom(4096)
# Print the response in hexadecimal format for raw byte analysis
print("HEX response:", response.hex())
# Attempt to decode the response as ASCII text, ignoring any decoding errors
# - errors='ignore' ensures the script doesn't crash if non-ASCII bytes are present
print("Decoded response:", response.decode(errors='ignore'))
# Close the socket to free up resources
s.close()