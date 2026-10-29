### Stage 1 — Fundamentals & SDR Setup

- [x]  Install GNU Radio
- [x] Configure ADALM-Pluto
	- [Setup guide](https://www.sdrstore.eu/pluto-plus-sdr-setup-guide-sdrangel-gnu-radio-ethernet/)
	- Verify Pluto TX/RX
	- [PlutoSDR using Python](https://pysdr.org/content/pluto#pluto-chapter)
	- [PlutSDR using libiio](https://analogdevicesinc.github.io/libiio/main/)
	- [BR2_EXTERNAL framework for Analog Device's PlutoSDR Zynq](https://github.com/oscimp/PlutoSDR)
- [x] Review
	- [I/Q sampling](https://kolegite.com/EE_library/books_and_lectures/%D0%A2%D0%B5%D0%BE%D1%80%D0%B8%D1%8F%20%D0%BD%D0%B0%20%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%D1%82%D0%BE/%D0%9C%D0%A3%D0%A1%D0%A1%D0%9F%D0%98/3.CORRELATION/UIA_correlation.pdf])
	- YouTube [video](https://www.youtube.com/watch?v=h_7d-m1ehoY)on IQ sampling
		- [GNU radio example](https://pysdr.org/content/sampling)
	- sampling and alia[[00 Phases]]sing
- [x] Understand complex baseband
	- [Article on complex sampling](https://www.dsprelated.com/showarticle/192.php)
- [x] Build basic GNU Radio flowgraph
- [GNU Radio wiki](https://wiki.gnuradio.org/index.php?title=Tutorials)
- [ ] Generate/test QPSK 
	- [ ] Modulation/Demodulation 
- [ ] Generate/test BPSK
	- BPSK demodulation example in [GNU wiki](https://wiki.gnuradio.org/index.php/Simulation_example:_BPSK_Demodulation)
	- [ ] Send/receive BPSK with Pluto
- [ ] Measure BER
- [ ] Document Pluto/GNU Radio setup

**Deliverable:**  
A working Pluto-based digital communication link with measurable BER.

Modulation schemes PSK QAM (offset QAM)

---

### Stage 2 — Reference Modem

- [ ] Implement BPSK
- [ ] Implement QPSK
- [ ] Implement 16-QAM
- [ ] Implement pulse shaping
- [ ] Implement matched filtering
- [ ] Implement timing synchronization
- [ ] Implement carrier/frequency synchronization
- [ ] Add FEC
- [ ] Build OFDM transmitter
- [ ] Build OFDM receiver
- [ ] Test AWGN
- [ ] Test multipath
- [ ] Test frequency offset
- [ ] Measure BER
- [ ] Measure EVM
- [ ] Compare modulation schemes

**Deliverable:**  
A reliable reference modem that can be used as the baseline for everything that follows.

---

###  Stage 3 — Extreme RF Conditions & Interference

- [ ] Define extreme RF scenarios
- [ ] Generate controlled interference
- [ ] Test narrowband interference
- [ ] Test wideband interference
- [ ] Test strong in-band interference
- [ ] Test adjacent-channel interference
- [ ] Test multipath/fading
- [ ] Measure spectrum
- [ ] Calculate noise floor
- [ ] Estimate SNR
- [ ] Estimate SINR
- [ ] Calculate EVM
- [ ] Calculate BER under interference
- [ ] Measure throughput
- [ ] Characterize communication failure
- [ ] Determine operating regions for BPSK/QPSK/16-QAM
- [ ] Build a dataset of RF conditions and modem performance

Starting point for collecting structured data.

```text
SNR | SINR | EVM | BER | Modulation | Power | Bandwidth | Throughput
```

That dataset becomes extremely useful later for the NN.

**Deliverable:**  
A quantitative characterization of how the communication system behaves under changing RF conditions.

---

### Stage 4 — Cognitive / Adaptive Communication

- [ ] Define channel-quality metric
- [ ] Define BER target
- [ ] Define throughput objective
- [ ] Define adaptation constraints
- [ ] Implement modulation switching
- [ ] Test BPSK ↔ QPSK
- [ ] Test QPSK ↔ 16-QAM
- [ ] Implement hysteresis
- [ ] Prevent rapid switching
- [ ] Implement adaptive transmit power
- [ ] Investigate adaptive bandwidth
- [ ] Measure adaptation time
- [ ] Measure BER
- [ ] Measure throughput
- [ ] Compare adaptive vs fixed modulation
- [ ] Compare adaptive vs fixed power
- [ ] Generate training/validation datasets
- [ ] Document the rule-based baseline

The system now looks like:

```text
RF conditions
      ↓
 SNR / SINR / EVM
      ↓
Adaptive controller
      ↓
┌──────────┬─────────┬──────────┐
│Modulation│  Power  │Bandwidth │
└──────────┴─────────┴──────────┘
      ↓
   Modem
      ↓
   Pluto
```

**Deliverable:**  
A working adaptive communication system.

---

# Stage 5 — FPGA Implementation

### FPGA preparation

- [ ]  Profile GNU Radio implementation 
- [ ] Connect FPGA processing to SDR data path
- [ ] Verify I/Q streaming
- [ ] Test real-time operation
- [ ] Identify latency-critical blocks
- [ ] Test adaptive controller
- [ ] Compare CPU vs FPGA
- [ ] Optimize fixed-point implementation
- [ ] Perform final experiments
- [ ] Document Pluto/GNU Radio setup
- [ ] Learn HDL/HLS/toolchain

---
## Stage 7 — Thesis

- [ ]  System architecture
- [ ]  SDR theory
- [ ]  OFDM implementation
- [ ]  Interference model
- [ ]  Adaptive algorithm
- [ ]  FPGA architecture
- [ ]  Experimental methodology
- [ ]  Results
- [ ]  FPGA resource analysis
- [ ]  Conclusions

