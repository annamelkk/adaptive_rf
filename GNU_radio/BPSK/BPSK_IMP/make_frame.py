import binascii
import struct

TEXT = "0"

PREAMBLE    = bytes([0xAA] * 4) # alternating bits, so that receiver understands message is starting
SYNC        = bytes.fromhex("1ACFFC1D") # 32-bit sync word the RX will search for

payload = TEXT.encode("ascii") # convert to ascii
assert len(payload) <= 255, "messag etoo long for 1-byte length field"

body    = bytes([len(payload)]) + payload # length + payload
crc     = struct.pack(">H", binascii.crc_hqx(body, 0xFFFF)) # 16-bit crc
frame   = PREAMBLE + SYNC + body + crc

with open("message.bin", "wb") as f:
    f.write(frame)

print("Wrote", len(frame), "bytes:")
print(frame.hex(" "))

