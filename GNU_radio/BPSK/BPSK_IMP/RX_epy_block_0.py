import time
import struct
import binascii
import numpy as np
from gnuradio import gr


class blk(gr.sync_block):
    """Finds the sync word in a bit stream, then decodes length + text + CRC16."""

    def __init__(self, sync_hex="1ACFFC1D"):
        gr.sync_block.__init__(self, name="Frame Decoder",
                               in_sig=[np.uint8], out_sig=None)
        sync_bits = np.unpackbits(np.frombuffer(bytes.fromhex(sync_hex), dtype=np.uint8))
        self.sync_pm = 2 * sync_bits.astype(np.int16) - 1   # +1/-1 pattern
        self.n = len(sync_bits)
        self.buf = np.zeros(0, dtype=np.uint8)
        self.good = 0
        self.bad = 0
        self.total = 0
        self.last_print = 0.0
        self.last_status = time.time()

    def work(self, input_items, output_items):
        x = input_items[0]
        self.total += len(x)
        self.buf = np.concatenate((self.buf, x & 1))
        self._scan()
        if time.time() - self.last_status > 1.0:
            self.last_status = time.time()
            print("[status] bits=%d good=%d bad=%d" % (self.total, self.good, self.bad))
        return len(x)

    def _scan(self):
        n = self.n
        while len(self.buf) >= n:
            s = 2 * self.buf.astype(np.int16) - 1
            c = np.correlate(s, self.sync_pm, mode="valid")
            hits = np.where(np.abs(c) >= n - 2)[0]      # allows 1 bit error
            if len(hits) == 0:
                self.buf = self.buf[-(n - 1):]
                return
            h = hits[0]
            start = h + n
            if len(self.buf) < start + 8:               # wait for more bits
                self.buf = self.buf[h:]
                return
            bits = self.buf[start:]
            if c[h] < 0:                                # inverted polarity
                bits = 1 - bits
            length = int(np.packbits(bits[:8])[0])
            total = 8 + 8 * length + 16                 # length + payload + CRC
            if len(bits) < total:
                self.buf = self.buf[h:]
                return
            data = np.packbits(bits[:total]).tobytes()
            body = data[:-2]
            crc = struct.unpack(">H", data[-2:])[0]
            if crc == binascii.crc_hqx(body, 0xFFFF):
                self.good += 1
                self.buf = self.buf[start + total:]
                if time.time() - self.last_print > 0.5:
                    self.last_print = time.time()
                    text = body[1:].decode("ascii", errors="replace")
                    print("[good %d, bad %d] %s" % (self.good, self.bad, text))
            else:
                self.bad += 1
                self.buf = self.buf[h + 1:]