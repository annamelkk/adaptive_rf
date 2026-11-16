import numpy as np, binascii, struct

SYNC_BITS = "00011010110011111111110000011101"      # 0x1ACFFC1D, MSB first

bits = np.fromfile("received.bin", dtype=np.uint8) & 1
s = "".join(map(str, bits))

def read_bytes(start, nbytes):
    seg = s[start:start + 8 * nbytes]
    if len(seg) < 8 * nbytes:
        return None
    return bytes(int(seg[i:i+8], 2) for i in range(0, len(seg), 8))

good = bad = 0
i = s.find(SYNC_BITS)
while i != -1:
    p = i + 32
    hdr = read_bytes(p, 1)
    if hdr:
        n = hdr[0]
        body_crc = read_bytes(p, 1 + n + 2)
        if body_crc:
            body, crc = body_crc[:-2], struct.unpack(">H", body_crc[-2:])[0]
            if crc == binascii.crc_hqx(body, 0xFFFF):
                good += 1
                print("OK :", body[1:])
            else:
                bad += 1
    i = s.find(SYNC_BITS, i + 1)

print(f"frames OK: {good}, CRC failures: {bad}")
